#!/usr/bin/env python

import gymnasium as gym
import gymnasium_csv

import numpy as np
import time
import sys
import argparse

import trajectory_alg

"""
# Coordinate Systems for `.csv` and `print(numpy)`

X points down (rows); Y points right (columns); Z would point outwards.

*--> Y (columns)
|
v
X (rows)

"""
UP = 0
UP_RIGHT = 1
RIGHT = 2
DOWN_RIGHT = 3
DOWN = 4
DOWN_LEFT = 5
LEFT = 6
UP_LEFT = 7

def translateKey(k):
      # This is used because usually PCs hace a numeric keyboard with some arrows drawn on it,
      # so we are going to take advantage of these arrows.
      k = str(k)
      keyDict = {
            "8": UP,
            "9": UP_RIGHT,
            "6": RIGHT,
            "3": DOWN_RIGHT,
            "2": DOWN,
            "1": DOWN_LEFT,
            "4": LEFT,
            "7": UP_RIGHT
      }
      if k in keyDict.keys():
            return keyDict[k]
      else:
            return 2 

def translateInstruction(instruction):
      # This is necessary to use trajectory_alg, due to the fact that it returns an array of strings (instructions)
      # so we translate it to the new asked format.
      if instruction == "up":
            return 0
      elif instruction == "down":
            return 4
      elif instruction == "right":
            return 2
      elif instruction == "left":
            return 6

parser = argparse.ArgumentParser()
parser.add_argument("--start_x", type=int, default=1)
parser.add_argument("--start_y", type=int, default=1)
parser.add_argument("--end_x", type=int, default=7)
parser.add_argument("--end_y", type=int, default=7)
parser.add_argument("--custom_map", type=str, default='map1.csv')
parser.add_argument("--sim_speed", type=float, default=1)
args = parser.parse_args()

START_X = args.start_x
START_Y = args.start_y
END_X = args.end_x
END_Y = args.end_y

SIM_PERIOD_MS = int(500.0 / args.sim_speed) # Here we limit the simmulation period values
if SIM_PERIOD_MS < 20:
      SIM_PERIOD_MS = 20
elif SIM_PERIOD_MS > 2000:
      SIM_PERIOD_MS = 2000


env = gym.make('gymnasium_csv-v0',
               render_mode='human',  # "human", "text", None
               inFileStr='../assets/' + args.custom_map,
               initX=START_X,
               initY=START_Y,
               goalX=END_X,
               goalY=END_Y)

answer = input("Do you want to play? (0=No, 1=Yes): ")
if answer == "0":
      instructions, objectives_coords = trajectory_alg.executeAlgorithm('../assets/' + args.custom_map, START_X, START_Y, END_X, END_Y)
      print("START: " + str((START_X, START_Y)) + " --------> GOAL: " + str((END_X, END_Y)))
      input("Press a key to continue....")
      print ("Instructions to follow: ", instructions)
      print ("Objective targets:", objectives_coords)

      observation, info = env.reset()

      print("observation: "+str(observation)+", info: "+str(info))
      env.render()
      time.sleep(0.5)

      terminated = False
      instr_completed = 0
      while not terminated:
            STEP_DIRECTION = translateInstruction(instructions[instr_completed])
            observation, reward, terminated, truncated, info = env.step(STEP_DIRECTION)
            env.render()
            print("observation: " + str(observation)+", reward: " + str(reward) + ", terminated: " + str(terminated) + ", truncated: " + str(truncated) + ", info: " + str(info))
            if not terminated:
                  if all(np.array(objectives_coords[instr_completed]) == observation):
                        instr_completed += 1
            time.sleep(SIM_PERIOD_MS/1000.0)
      if all(np.array(objectives_coords[instr_completed]) == observation):
            print ("\nGOAAAAAAAAAAAAAL!!!")
      else:
            print ("\nOh, no...")

else:
      print("\n\t    CONTROLS   ")
      print("\t  7    8    9  ")
      print("\t   ^   ^   ^   ")
      print("\t    \  |  /    ")
      print("\t     \ | /     ")
      print("\t4 <--- o ---> 6")
      print("\t     / | \     ")
      print("\t    /  |  \    ")
      print("\t   v   V   v   ")
      print("\t  1    2    3  \n")

      observation, info = env.reset()

      print("observation: "+str(observation)+", info: "+str(info))
      env.render()
      print("You have to use the controls above to move your robot to the objective.")
      input("Ready? Press a key to continue...")
      terminated = False
      instr_completed = 0
      while not terminated:
            k = input()
            STEP_DIRECTION = translateKey(k)
            observation, reward, terminated, truncated, info = env.step(STEP_DIRECTION)
            env.render()
      
      if all(np.array([END_X, END_Y]) == observation):
            print ("\nGOAAAAAAAAAAAAAL!!!")
      else:
            print ("\nOh, no... GAME OVER")
