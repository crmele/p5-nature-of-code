# The Nature of Code
# Daniel Shiffman
# Chapter 01: Vectors - Example 1.4
#
# Python port: Crystal Mele


# Vector multiplication

from p5 import *

def setup():
    size(640, 360)

def draw():
    background(255)
    # create vectors
    mouse = Vector(mouse_x, mouse_y)
    center = Vector(width / 2, height / 2)
    
    mouse = mouse - center
    # multiply a vector
    mouse = mouse * (0.5)

    # display vector
    translate(width / 2, height / 2)
    line((0, 0), mouse)


if __name__ == '__main__':
    run()
