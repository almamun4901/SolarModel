# Author: Md Al Mamun
# Date: 10/22/2022
# Purpose: Lab 3 checkpoint

# the system class draw each item and update them
import math # math class to use math functions
class System:
    def __init__(self, body):
        self.body = body

    def compute_acceleration(self, n):
        G = 6.67384e-11 # gravitational constant

        # initial acceleration
        ax = 0
        ay = 0

        for i in range(0, len(self.body)):
            if i != n:
                dx = self.body[i].x - self.body[n].x
                dy = self.body[i].y - self.body[n].y

                r = math.sqrt((dx * dx) + (dy * dy))

                a = (G * self.body[i].mass) / (r * r)

                ax = ax + ((a * dx) / r)
                ay = ay + ((a * dy) / r)


        return (ax, ay)


    # update function
    def update(self, timestep):
        # update velocity
        for index in range (0, len(self.body)):
            ax, ay = self.compute_acceleration(index)
            self.body[index].update_velocity(ax, ay, timestep)

        # updating position
        for item in self.body:
            item.update_position(timestep)


    #drawing function
    def draw(self,cx,cy,pixels_per_meter):

        for item in self.body:
            item.draw(cx,cy,pixels_per_meter)