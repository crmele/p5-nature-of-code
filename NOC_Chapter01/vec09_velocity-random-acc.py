# The Nature of Code
# Daniel Shiffman
# Chapter 01: Vectors - Example 1.9
#
# Python port: Crystal Mele


# Motion 101 (velocity and random acceleration)

from p5 import *


class Mover(object):

    def __init__(self):
        self.position = Vector(width / 2, height / 2)
        self.velocity = Vector(0, 0)
        self.topspeed = 6

    def update(self):
        # create a vector of length 1 pointing at random direction
        self.acceleration = Vector.random_2D()
        self.acceleration = self.acceleration * random_uniform(2)

        self.velocity = self.velocity + self.acceleration
        self.velocity.limit(self.topspeed)

        self.position = self.position + self.velocity

    def display(self):
        stroke(0)
        fill(127)
        ellipse(self.position, 48, 48)

    def check_edges(self):
        if self.position.x > width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = width
        if self.position.y > height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = height

        
def setup():
    size(640, 360)
    # create mover object
    global mover
    mover = Mover()

def draw():
    background(255)
    # call functions on mover objects
    mover.update()
    mover.check_edges()
    mover.display()


if __name__ == '__main__':
    run(frame_rate = 60)
