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

class Cube:

    def init_props(self):
        self.color = (0.0, 0.7, 0.1)
        self.edge_color = (1, 1, 1)
        self.pos = (0, 0, 0)
        self.length = 2

        self.verticies = (
            (1, 1, 1),
            (1, 1, -1),
            (1, -1, 1),
            (1, -1, -1),
            (-1, 1, 1),
            (-1, 1, -1),
            (-1, -1, 1),
            (-1, -1, -1),
        )

        self.edges = (
            (0, 1),
            (0, 4),
            (0, 2),
            (1, 5),
            (2, 6),
            (2, 3),
            (3, 7),
            (3, 1),
            (4, 6),
            (4, 5),
            (5, 7),
            (6, 7),
        )

        self.surfaces = (
            (0, 1, 2, 3),
            (0, 1, 4, 5),
            (0, 2, 6, 4),
            (1, 5, 3, 7),
            (2, 3, 7, 6),
            (4, 5, 6, 7),
        )

    def __init__(self, x = 0, y = 0, z = 0, l = 2):
        self.init_props()
        self.pos = (x, y, z)
        self.length = l

        new_pos = []
        for vx in self.verticies:
            new_pos.append(Cube.tuple_add(vx, (x, y, z)))
        self.verticies = tuple(new_pos)
    
    def move(self, x, y, z):
        new_pos = []
        for vx in self.verticies:
            new_vx = Cube.tuple_add(vx, (x, y, z))
            new_pos.append(new_vx)
        self.verticies = tuple(new_pos)

        # update position
        self.pos = Cube.tuple_add(self.pos, (x, y, z))

    def display(self):
        glBegin(GL_QUADS)
        glColor3fv(self.color)
        for surface in self.surfaces:
            for vertex in surface:
                glVertex3fv(self.verticies[vertex])
        glEnd()

        glBegin(GL_LINES)
        glColor3fv(self.edge_color)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.verticies[vertex])
        glEnd()

    def set_color(self, color):
        self.color = color

    @staticmethod
    def tuple_add(t1, t2):
        l = len(t1)
        ret = []
        for i in range(l):
            ret.append(t1[i] + t2[i])
        return tuple(ret)