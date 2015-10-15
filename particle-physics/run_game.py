import pygame
import random

from core import addVectors, findParticle
from math import pi as Pi, sin, cos, hypot, atan2
from surface import screen, background_color, width, height
from game_objects import Particle


pygame.init()

#-- instantiate particles ---------------------->>>
number_of_particles = 10
particles = []
for n in range(number_of_particles):

    #-- assign random in-bounds position ------->>>
    radius = random.randint(5, 20)
    x = random.randint(radius, width - radius)
    y = random.randint(radius, height - radius)
    particle = Particle((x, y), radius)

    #-- assign random speed & angle ------------>>>
    particle.color = (0, 0, 255)
    particle.speed = random.random()
    particle.angle = random.uniform(0, 2*Pi)

    particles.append(particle)


#-- GAME LOOP -------------------------------------->>>
selected_particle = None
running = True
while running:

    #-- detect pygame events -------------------->>>
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            selected_particle = findParticle(particles, mouseX, mouseY)
        if event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None

    #-- particle motion ------------------------->>>
    for particle in particles:
        if particle != selected_particle:
            particle.move()
            particle.bounce()
        particle.display(screen)

    if selected_particle:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        selected_particle.color = (255,0,0)
        dx = mouseX - selected_particle.x
        dy = mouseY - selected_particle.y
        selected_particle.angle = atan2(dy, dx)
        selected_particle.speed = hypot(dx, dy) * 0.1
        #-- update particle position w mouse ---->>>
        selected_particle.x = mouseX
        selected_particle.y = mouseY

    pygame.display.update()
    screen.fill(background_color)
