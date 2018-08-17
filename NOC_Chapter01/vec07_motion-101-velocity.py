# The Nature of Code
# Daniel Shiffman
# Chapter 01: Vectors - Example 1.7
#
# Python port: Crystal Mele


from p5 import *

class Mover(object):
    def __init__(self):
        # create object with the position and velocity vectors
        self.position = Vector(random_uniform(width), random_uniform(height))
        self.velocity = Vector(random_uniform(low=-2, high=2), random_uniform(low=-2, high=2))

    def update(self):
        # change position by the mover's velocity
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
    # call functions on mover object
    mover.update()
    mover.check_edges()
    mover.display()


if __name__ == '__main__':
    run(frame_rate = 60)
