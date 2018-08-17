# The Nature of Code
# Daniel Shiffman
# Chapter 01: Vectors - Example 1.10
#
# Python port: Crusyal Mele


# Accelerating towards mouse

from p5 import *

class Mover(object):

    def __init__(self):
        self.position = Vector(width / 2, height / 2)
        self.velocity = Vector(0, 0)
        self.topspeed = 5

    def update(self):
        self.mouse = Vector(mouse_x, mouse_y)
        # compute direction
        self.acceleration = self.mouse - self.position

        self.acceleration.normalize()
        self.acceleration *= (0.2)

        self.velocity = self.velocity + self.acceleration
        self.position = self.position + self.velocity


    def display(self):
        stroke(0)
        fill(127)
        ellipse(self.position, 48, 48)


def setup():
    size(640, 360)
    # create mover object
    global mover
    mover = Mover()

def draw():
    background(255)

    mover.update()
    mover.display()


if __name__ == '__main__':
    run(frame_rate = 60)
