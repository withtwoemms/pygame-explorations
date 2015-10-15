from math import pi as Pi, sin, cos, hypot, atan2


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

