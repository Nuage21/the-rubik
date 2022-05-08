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

from Cube import *
from Rubik import *

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -40.0)
    glRotate(0, 0, 0, 0)

    rubik = Rubik()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        rubik.display()
        
        pygame.display.flip()
        pygame.time.wait(2)
        glRotate(1, 1, 0, 0)



main()