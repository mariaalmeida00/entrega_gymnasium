#!/usr/bin/env python

import gymnasium as gym
import gymnasium_csv

import numpy as np
import time
import sys

import trajectory_alg

"""
# Coordinate Systems for `.csv` and `print(numpy)`

X points down (rows); Y points right (columns); Z would point outwards.

*--> Y (columns)
|
v
X (rows)

"""


START_X = 1
START_Y = 1
END_X = 7
END_Y = 7

print(f"Arguments count: {len(sys.argv)}")
for i, arg in enumerate(sys.argv):
      print(f"Argument {i:>6}: {arg}")
      arg = arg.lower()
      if "start_x=" in arg:
            arg = arg.replace("start_x=", "")
            START_X = int(arg)
      elif "start_y=" in arg:
            arg = arg.replace("start_y=", "")
            START_Y = int(arg)
      elif "end_x=" in arg:
            arg = arg.replace("end_x=", "")
            END_X = int(arg)
      elif "end_y=" in arg:
            arg = arg.replace("end_y=", "")
            END_Y = int(arg)

UP = 0
UP_RIGHT = 1
RIGHT = 2
DOWN_RIGHT = 3
DOWN = 4
DOWN_LEFT = 5
LEFT = 6
UP_LEFT = 7

SIM_PERIOD_MS = 500.0


env = gym.make('gymnasium_csv-v0',
               render_mode='human',  # "human", "text", None
               inFileStr='../assets/map1.csv',
               initX=START_X,
               initY=START_Y,
               goalX=END_X,
               goalY=END_Y)

observation, info = env.reset()

instructions, objectives_coords = trajectory_alg.executeAlgorithm(START_X, START_Y, END_X, END_Y)

print (instructions, objectives_coords)

print("observation: "+str(observation)+", info: "+str(info))
env.render()
time.sleep(0.5)

for i in range(5):
    observation, reward, terminated, truncated, info = env.step(DOWN_RIGHT)
    env.render()
    print("observation: " + str(observation)+", reward: " + str(reward) + ", terminated: " +
          str(terminated) + ", truncated: " + str(truncated) + ", info: " + str(info))
    time.sleep(SIM_PERIOD_MS/1000.0)
