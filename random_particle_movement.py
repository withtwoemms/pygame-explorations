import math
import pygame
import random


pygame.init()
Pi = math.pi

#-- SCREEN CHARACTERISTICS ------------------------->>>
background_color = (255,255,255)
(width, height) = (300, 200)

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

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius, self.thickness)

#-- RENDER SCREEN ---------------------------------->>>
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)

number_of_particles = 20
particles = []
for n in range(number_of_particles):
    radius = random.randint(5, 20)
    x = random.randint(radius, width - radius)
    y = random.randint(radius, height - radius)

    particle = Particle((x, y), radius)
    particle.speed = random.random()
    particle.angle = random.uniform(0, Pi*2)

    particles.append(particle)


#-- RUN LOOP --------------------------------------->>>
running = True
while running:

    #-- move particles -------------------------->>>
    '''
    A particle.angle of 0 moves particles vertically at a given speed.
    Directions chosen arbitrarily, defined in the particle.move(), and subject are to change.
    Use the unit circle for all other motions:
        down => 0 rad.
        up => Pi rad.
        right => Pi/2 rad.
        left => 3 * Pi/2 rad.
        ... and all the angles betwixt
    '''
    for particle in particles:
        particle.move()
        particle.display()
    pygame.display.flip()
    screen.fill(background_color)

    #-- detect pygame events -------------------->>>
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
