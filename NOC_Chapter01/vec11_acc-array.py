# The Nature of Code
# Daniel Shiffman
# Chapter 01: Vectors - Example 1.11
#
# Python port: Crystal Mele


# Array of movers accelerating towards the mouse

from p5 import *

class Mover(object):

    def __init__(self):
        """Create object with two vectors"""
        self.position = Vector(random_uniform(width), random_uniform(height))
        self.velocity = Vector(0, 0)
        self.topspeed = 5

        
    def update(self):
        """Calculates acceleration and updates position"""
        self.mouse = Vector(mouse_x, mouse_y)
        self.acceleration = self.mouse - self.position

        self.acceleration.normalize()
        self.acceleration *= (0.2)

        self.velocity = self.velocity + self.acceleration
        self.velocity.limit(self.topspeed)
        self.position = self.position + self.velocity

        
    def check_edges(self):
        """Checks edges """
        if self.position.x > width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = width
        if self.position.y > height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = height

        
    def display(self):
        stroke(0)
        fill(127, 200)
        ellipse(self.position, 16, 16)

        
# create an array of 20 items
movers = [0] * 20

def setup():
    size(640, 360)
    # create mover object in the array
    for i in range(len(movers)):
        movers[i] = Mover()


def draw():
    background(255)
    no_stroke()
    fill(175, 10)
    rect((0, 0), width, height)

    for i in range(len(movers)):
        movers[i].update()
        movers[i].check_edges()
        movers[i].display()


if __name__ == '__main__':
    run()
