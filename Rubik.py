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
from Transformation import *


class Rubik:

    def __init__(self):

        # face O - center face
        self.cube_000 = Cube()  # center cuber
        self.cube_100 = Cube(2.1, 0, 0)
        self.cube_f00 = Cube(-2.1, 0, 0)
        self.cube_001 = Cube(0, 0, 2.1)
        self.cube_00f = Cube(0, 0, -2.1)
        self.cube_101 = Cube(2.1, 0, 2.1) 
        self.cube_10f = Cube(2.1, 0, -2.1)
        self.cube_f01 = Cube(-2.1, 0, 2.1)
        self.cube_f0f = Cube(-2.1, 0, -2.1)  

        self.face_o = [self.cube_000, self.cube_100, self.cube_f00, self.cube_001, self.cube_00f, self.cube_101, self.cube_10f, self.cube_f01, self.cube_f0f]

        # face A - rotates over y-axis
        self.cube_0f0 = Cube(0, -2.1, 0)
        self.cube_1f0 = Cube(2.1, -2.1, 0)
        self.cube_ff0 = Cube(-2.1, -2.1, 0)
        self.cube_0f1 = Cube(0, -2.1, 2.1)
        self.cube_0ff = Cube(0, -2.1, -2.1)
        self.cube_1f1 = Cube(2.1, -2.1, 2.1) 
        self.cube_1ff = Cube(2.1, -2.1, -2.1)
        self.cube_ff1 = Cube(-2.1, -2.1, 2.1)
        self.cube_fff = Cube(-2.1, -2.1, -2.1)  

        self.face_a = [self.cube_0f0, self.cube_1f0, self.cube_ff0, self.cube_0f1, self.cube_0ff, self.cube_1f1, self.cube_1ff, self.cube_ff1, self.cube_fff]

        # face B - rotates over y-axis
        self.cube_010 = Cube(0, 2.1, 0)
        self.cube_110 = Cube(2.1, 2.1, 0)
        self.cube_f10 = Cube(-2.1, 2.1, 0)
        self.cube_011 = Cube(0, 2.1, 2.1)
        self.cube_01f = Cube(0, 2.1, -2.1)
        self.cube_111 = Cube(2.1, 2.1, 2.1) 
        self.cube_11f = Cube(2.1, 2.1, -2.1)
        self.cube_f11 = Cube(-2.1, 2.1, 2.1)
        self.cube_f1f = Cube(-2.1, 2.1, -2.1)  

        self.face_b = [self.cube_010, self.cube_110, self.cube_f10, self.cube_011, self.cube_01f, self.cube_111, self.cube_11f, self.cube_f11, self.cube_f1f]
        
        # fifo of applied transformations to be displayed|applied on next frame
        self.transforms_q = []

        self.gl_matrix = glGetDoublev(GL_MODELVIEW_MATRIX)
    
    def get_cube_at(self, x, y, z):
        pos = [x, y, z]
        for p in pos:
            if p not in [-1, 0, 1]:
                raise TypeError(f"{p} not in [-1, 0, 1]")
        
        def _(_x):
            if(_x == -1):
                return "f"
            return str(_x)

        prop = "cube_" + _(x) + _(y) + _(z)
        return getattr(self, prop)

    def display(self):
        
        glMatrixMode(GL_MODELVIEW);
        glPushMatrix()
        glLoadMatrixd(self.gl_matrix)

        while len(self.transforms_q) > 0:
            transformation = self.transforms_q.pop(0)
            transformation.apply()
        
        for face in [self.face_o, self.face_a, self.face_b]:
            for cube in face:
                cube.display()
        
        self.gl_matrix = glGetDoublev(GL_MODELVIEW_MATRIX)
        glPopMatrix()
        glFlush()

    def q_transformation(self, transform):
        self.transforms_q.append(transform)

