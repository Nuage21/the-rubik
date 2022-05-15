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

# define Transformation Types

TRANSFORMATION_ROTATION = 0
TRANSFORMATION_TRANSLATION = 1
TRANSFORMATION_SCALE = 2

TRANSFORMATION_TYPES = [TRANSFORMATION_ROTATION, TRANSFORMATION_TRANSLATION, TRANSFORMATION_SCALE]

class Transformation:

    def __init__(self, type, x=0, y=0, z=0, t=0):
        if type not in TRANSFORMATION_TYPES:
            raise TypeError("Error: Invalid Transformation Type!")

        self.type = type
        self.x = x
        self.y = y
        self.z = z
        self.t = t

    # caller should handle glob Matrix push|pop
    def apply(self):
        if self.type == TRANSFORMATION_ROTATION:
            glRotate(self.x, self.y, self.z, self.t)
        elif self.type == TRANSFORMATION_TRANSLATION:
            glTranslate(self.x, self.y, self.z)
        elif self.type == TRANSFORMATION_SCALE:
            glScale(self.x, self.y, self.x)
        else:
            pass