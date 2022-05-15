# * * * * * * * * * * * * * * * * * * * * * * * * #
#                                                 #
#   @Programmer: Hakim Beldjoudi                  #
#   @email: ih_beldjoudi@openfox.com              #
#   @Date: May 8th, 2022                          #
#   -> Meow                                       #
#                                                 #
# * * * * * * * * * * * * * * * * * * * * * * * * #

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from Plan import *
from Cube import *
from Rubik import *
from Transformation import *

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -40.0)
    glRotate(0, 0, 0, 0)

    glEnable(GL_BLEND)
    glDisable(GL_DEPTH_TEST)

    rubik = Rubik()
    plan = Plan()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        reload_display([rubik, plan])
        pygame.display.flip()

        rubik.q_transformation(Transformation(TRANSFORMATION_ROTATION, 1, 1, 2, 0))
        pygame.time.wait(10)
        

 
def reload_display(objs):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    for obj in objs:
        obj.display()

main()