# The Nature of Code
# Daniel Shiffman
# Chapter 01: Vectors - Example 1.1
#
# Python port: Crystal Mele


# Bouncing ball with no Vector

from p5 import *

# variables for location and speed of ball
x = 100
y = 100
x_speed = 1
y_speed = 3.3


def setup():
    size(640, 360)
    background(255)
   

def draw():
    background(255)
    # move the ball according to its speed
    global x, y, x_speed, y_speed
    x += x_speed
    y += y_speed
    # check for bouncing
    if (x > width) or (x < 0):
        x_speed *= (-1)
    if (y > height) or (y < 0):
        y_speed *= (-1)
    # display the ball
    stroke(0)
    fill(175)
    ellipse((x, y), 16, 16)


if __name__ == "__main__":
    run(frame_rate=60)
