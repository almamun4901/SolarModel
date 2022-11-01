# solar.py
# Example for CS 1 Lab Assignment 2.
# db, thc; 2011-2016

# Author: Md Al Mamun
# Date: 10/28/2022
# Purpose: Lab 3 solar system

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 3.0e6         # real seconds per simulation second
PIXELS_PER_METER = 7 / 1e10  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    #Draw the system in its current state.
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)

# creating sun and planets objects using Body class

sun = Body(1.98892e30, 0, 0, 0, 0, 24, 1, 1, 0)
mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 4, 0, 0.8, 0.5)
venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 9, 1, 0, 1)
earth = Body(5.97e24, -149.6e9, 0, 0, 29790, 10, 0, 0.5, 1)
mars = Body(0.642e24, -227.9e9, 0, 0, 24140, 5, 1, 0, 0)

solar_system = System([sun, mercury, venus, earth, mars])

start_graphics(main, 2400, framerate=FRAMERATE)