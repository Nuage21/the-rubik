# * * * * * * * * * * * * * * * * * * * * * * * * #
#                                                 #
#   @Programmer: Hakim Beldjoudi                  #
#   @email: ih_beldjoudi@openfox.com              #
#   @Date: May 8th, 2022                          #
#   -> Meow                                       #
#                                                 #
# * * * * * * * * * * * * * * * * * * * * * * * * #

from OpenGL.GL import *
from OpenGL.GLU import *

from Cube import *


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
        


    def display(self):
        for face in [self.face_o, self.face_a, self.face_b]:
            for cube in face:
                cube.display()

