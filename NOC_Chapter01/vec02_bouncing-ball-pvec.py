# The Nature of Code
# Daniel Shiffman
# Chapter 01: Vectors - Example 1.2
#
# Python port: Crystal Mele


# Bouncing ball with Vector

from p5 import *

# vectors for location and speed of ball
position = Vector(100, 100)
velocity = Vector(2.5, 5)

def setup():
    size(640, 360)
    background(255)

    
def draw():
    no_stroke()
    fill(255,10)
    rect((0,0), width, height)

    global position, velocity
    # move the ball according to its speed
    position += velocity
    # check for bouncing
    if (position.x > width) or (position.x < 0):
        velocity.x *= (-1)
    if (position.y > height) or (position.y < 0):
        velocity.y *= (-1)
    # display the ball
    stroke(0)
    fill(175)
    ellipse(position, 16, 16)

run()
