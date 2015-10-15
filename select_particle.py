import pygame
import random

from math import pi as Pi, sin, cos, hypot, atan2


pygame.init()

#-- SCREEN CHARACTERISTICS ------------------------->>>
background_color = (255,255,255)
(width, height) = (600, 600)

#-- RENDER SCREEN ---------------------------------->>>
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)

#-- HELPER FUNCTIONS ------------------------------->>>
def findParticle(particles, x,y):
    for particle in particles:
        if hypot(particle.x - x, particle.y - y) <= particle.radius:
            return particle
    return None

def addVectors((ang1, len1), (ang2, len2)):
    '''
    Adds two vectors together component-wise.
    [Trig. func.] of an angle times its length (hypotenuse)
    gives the appropriate compenent.
    Components of the resultant are the sum of each component's components
    '''
    x = cos(ang1) * len1 + cos(ang2) * len2
    y = sin(ang1) * len1 + sin(ang2) * len2
    length = hypot(x, y)
    angle =  atan2(y, x)
    return (angle, length)

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
        selected_particle.color = (255,0,0)

    pygame.display.update()
    screen.fill(background_color)
