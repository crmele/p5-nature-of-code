# The Nature of Code
# Daniel Shiffman
# Chapter 01: Vectors - Example 1.5
#
# Python port: Crystal Mele


from p5 import *

def setup():
    size(640, 360)


def draw():
    background(255)

    mouse = Vector(mouse_x, mouse_y)
    center = Vector(width / 2, height / 2)
    mouse = mouse - center

    # access the magnitude using magnitude
    m = mouse.magnitude
    fill(0)
    rect((0,0), m, 10)

    translate(width / 2, height / 2)
    stroke(0)
    line((0, 0), mouse)


if __name__ == '__main__':
    run()
