import pygame
import random


pygame.init()

#-- SCREEN CHARACTERISTICS ------------------------->>>
background_color = (255,255,255)
(width, height) = (300, 200)

class Particle:
    def __init__(self, (x, y), radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (255, 0, 0)
        self.thickness = 1

    def display(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.thickness)

#-- RENDER SCREEN ---------------------------------->>>
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)

number_of_particles = 10
particles = []
for n in range(number_of_particles):
    radius = random.randint(5, 20)
    x = random.randint(radius, width - radius)
    y = random.randint(radius, height - radius)
    particles.append(Particle((x, y), radius))

for particle in particles:
    particle.display()

#-- RUN LOOP --------------------------------------->>>
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

