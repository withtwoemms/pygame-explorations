import pygame

from core import addVectors
from math import pi as Pi, sin, cos, hypot, atan2
from surface import screen, width, height


#-- PARTICLE DEFINITION ---------------------------->>>
class Particle:
    '''
    All you need to is a coordinate tuple and a radius to instantiate.
    e.g. particle = Particl((50, 50), 10)
    '''

    def __init__(self, (x, y), radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (255, 0, 0)
        self.thickness = 2
        self.speed = 1
        self.angle = 0 #EAST
        self.x_border = width - self.radius
        self.y_border = height - self.radius
        #-- constants --------------------------->>>
        self.gravity = (3*Pi/2, -0.4)
        self.drag = 0.9999
        self.elasticity = 0.5

    def move(self):
        '''
        A particle.angle of Pi/2, orients vertically at a given speed.
        Use the unit circle for all other motions:
            right => 0 rad.
            left => Pi rad.
            up => Pi/2 rad.
            down => 3 * Pi/2 rad. ...
        and all the angles betwixt
        '''
        self.x += cos(self.angle) * self.speed
        self.y += sin(self.angle) * self.speed
        (self.angle, self.speed) = addVectors((self.angle, self.speed), self.gravity)
        self.speed *= self.drag

    def bounce(self):
        '''
        The collision border is width|height - radius.
        Displacement beyond the border is e.g. dx = x - x_border.
        If position is beyond the border, displacement is positive...
        To accomplish the "bounce", we essentially subtract displacement from border.
        This effectively restores the position to the boundary.
        Also, the angle needs to be inverted.
        '''
        if self.x > self.x_border:
            self.x = 2 * (self.x_border) - self.x
            self.angle = Pi - self.angle
            self.speed *= self.elasticity
        elif self.x < self.radius:
            self.x = 2 * (self.radius) - self.x
            self.angle = Pi - self.angle
            self.speed *= self.elasticity

        if self.y > self.y_border:
            self.y = 2 * (self.y_border) - self.y
            self.angle = - self.angle
            self.speed *= self.elasticity
        elif self.y < self.radius:
            self.y = 2 * (self.radius) - self.y
            self.angle = - self.angle
            self.speed *= self.elasticity


    def display(self, screen):
        '''
        Renders a particle on a `screen`.
        '''
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius, self.thickness)

