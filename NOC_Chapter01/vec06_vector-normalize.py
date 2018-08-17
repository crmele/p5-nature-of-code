# The Nature of Code
# Daniel Shiffman
# Chapter 01: Vectors - Example 1.6
#
# Python port: Crystal Mele


# Demonstration of normalizing a vector
# Normalizing a vector sets its length to 1


from p5 import *

def setup():
    size(360, 360)


def draw():
    background(255)

    # vector that point to the mouse position
    mouse = Vector(mouse_x, mouse_y)
    # vector that points to center of the window
    center = Vector(width / 2, height / 2)
    # Vector that point from center to mouse
    mouse = mouse - center

    # Normalize the vector
    mouse.normalize()
    
    mouse = mouse * 50

    translate(width / 2, height / 2)
    # draw the resulting vector
    stroke(0)
    line((0, 0), mouse)


if __name__ == '__main__':
    run()
