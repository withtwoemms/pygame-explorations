import pygame
import random

from math import pi as Pi, sin, cos


pygame.init()

#-- SCREEN CHARACTERISTICS ------------------------->>>
background_color = (255,255,255)
(width, height) = (400, 400)

#-- PARTICLE DEFINITION ---------------------------->>>
class Particle:
    def __init__(self, (x, y), radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (255, 0, 0)
        self.thickness = 1
        self.speed = 0.1
        self.angle = 0
        self.x_border = width - self.radius
        self.y_border = height - self.radius

    def move(self):
        '''
        A particle.angle of 0, moves particles vertically at a given speed.
        Use the unit circle for all other motions:
            down => 0 rad.
            up => Pi rad.
            right => Pi/2 rad.
            left => 3 * Pi/2 rad. ...
        and all the angles betwixt
        '''
        self.x += sin(self.angle) * self.speed
        self.y += cos(self.angle) * self.speed

    def bounce(self):
        '''
        Initial position for a Particle is its radius from 0
        up to its radius from the screen edge.
        Being such, the collision border is width|height - radius.
        Displacement beyond the border is e.g. dx = x - x_border.
        If position is beyond the border, displacement is positive...
        To accomplish the "bounce", we essentially subtract displacement from border.
        This effectively restores the position to the boundary.
        Also, the angle needs to be inverted.
        '''
        if self.x > self.x_border:
            self.x = 2 * (self.x_border) - self.x
            self.angle = -self.angle
        elif self.x < self.radius:
            self.x = 2 * (self.radius) - self.x
            self.angle = -self.angle

        if self.y > self.y_border:
            self.y = 2 * (self.y_border) - self.y
            self.angle = Pi - self.angle
        elif self.y < self.radius:
            self.y = 2 * (self.radius) - self.y
            self.angle = Pi - self.angle


    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius, self.thickness)

#-- RENDER SCREEN ---------------------------------->>>
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)

#-- instantiate particles ----------------------->>>
number_of_particles = 10
particles = []
for n in range(number_of_particles):
    radius = random.randint(5, 20)
    x = random.randint(radius, width - radius)
    y = random.randint(radius, height - radius)

    particle = Particle((x, y), radius)
    particle.speed = random.random()
    particle.angle = random.uniform(0, 2*Pi)

    particles.append(particle)


#-- RUN LOOP --------------------------------------->>>
running = True
while running:

    #-- move particles -------------------------->>>
    for particle in particles:
        particle.move()
        particle.bounce()
        particle.display()
    pygame.display.flip()
    screen.fill(background_color)

    #-- detect pygame events -------------------->>>
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

