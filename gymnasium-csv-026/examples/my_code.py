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

def translateInstruction(instruction):
      UP = 0
      UP_RIGHT = 1
      RIGHT = 2
      DOWN_RIGHT = 3
      DOWN = 4
      DOWN_LEFT = 5
      LEFT = 6
      UP_LEFT = 7
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
args = parser.parse_args()

START_X = args.start_x
START_Y = args.start_y
END_X = args.end_x
END_Y = args.end_y

SIM_PERIOD_MS = 500.0


env = gym.make('gymnasium_csv-v0',
               render_mode='human',  # "human", "text", None
               inFileStr='../assets/map1.csv',
               initX=START_X,
               initY=START_Y,
               goalX=END_X,
               goalY=END_Y)

instructions, objectives_coords = trajectory_alg.executeAlgorithm(START_X, START_Y, END_X, END_Y)
print("START: " + str((START_X, START_Y)) + " --------> GOAL: " + str((END_X, END_Y)))
input()
print ("Instructions to follow: ", instructions)
input()

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
      if all(np.array(objectives_coords[instr_completed]) == observation):
            instr_completed += 1
      time.sleep(SIM_PERIOD_MS/1000.0)
print ("\nGOAAAAAAAAAAAAAL!!!")