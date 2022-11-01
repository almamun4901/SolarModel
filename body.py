# Author: Md Al Mamun
# Date: 10/22/2022
# Purpose: Lab 3 checkpoint

#this is the body class to draw plantes and set their velocity

from cs1lib import *

class Body:
    def __init__(self, mass, x, y, v_x, v_y, pixels_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = v_x
        self.vy = v_y
        self.pixels_radius = pixels_radius
        self.r = r
        self.g = g
        self.b = b

    # draw function to draw planets
    def draw(self, cx,cy, pixels_per_meter):
        set_fill_color(self.r, self.g, self.b)
        draw_circle(cx + self.x * pixels_per_meter, cy - self.y * pixels_per_meter, self.pixels_radius)

    # function to update the position
    def update_position(self, timestep):
        self.x = self.x + self.vx * timestep
        self.y = self.y + self.vy * timestep

    # function to update velocity
    def update_velocity(self, ax, ay, timestep):
        self.vx = self.vx + ax * timestep
        self.vy = self.vy + ay * timestep