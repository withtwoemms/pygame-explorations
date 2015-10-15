import pygame


pygame.init()

#-- SCREEN CHARACTERISTICS ------------------------->>>
background_color = (255,255,255)
(width, height) = (300, 200)

#-- RENDER SCREEN ---------------------------------->>>
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)
pygame.display.flip()

#-- RUN LOOP --------------------------------------->>>
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
