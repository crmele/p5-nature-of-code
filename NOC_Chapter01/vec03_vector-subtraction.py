# The Nature of Code
# Daniel Shiffman
# Chapter 01: Vectors - Example 1.3
#
# Python port: Crystal Mele


# Vector subtraction

from p5 import *


def setup():
    size(640, 360)


def draw():
    background(255)
    # create vector for mouse location
    mouse = Vector(mouse_x, mouse_y)
    # create vector for center of the window
    center = Vector(width / 2, height / 2)
    # subtract vectors
    mouse = mouse - center

    # draw line to represent vector
    translate(center.x, center.y)
    line((0, 0), (mouse))


if __name__ == '__main__':
    run()
