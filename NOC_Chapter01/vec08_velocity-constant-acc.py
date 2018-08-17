# The Nature of Code
# Daniel Shiffman
# Chapter 01: Vectors - Example 1.8
#
# Python port: Crystal Mele


# Motion 101 (velocity and constant acceleration)

from p5 import *

class Mover(object):
    def __init__(self):
        # object has a location, velocity and acceleration vector
        self.location = Vector(width / 2, height / 2)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(-0.001, 0.01)
        self.topspeed = 10


    def update(self):
        # change velocity by acceleration
        self.velocity = self.velocity + self.acceleration
        # limit velocity by topspeed
        self.velocity.limit(self.topspeed)
        # change location by velocity
        self.location = self.location + self.velocity

    def display(self):
        stroke(0)
        fill(127)
        ellipse(self.location, 48, 48)

    def check_edges(self):
        if self.location.x > width:
            self.location.x = 0
        elif self.location.x < 0:
            self.location.x = width
        if self.location.y > height:
            self.location.y = 0
        elif self.location.y < 0:
            self.location.y = height



def setup():
    size(640, 360)
    # create mover object
    global mover
    mover = Mover()

def draw():
    background(255)
    # call functions on mover object
    mover.update()
    mover.check_edges()
    mover.display()


if __name__ == '__main__':
    run(frame_rate = 60)
