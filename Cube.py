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
        self.color = (0.0, 0.7, 0.1 )
        self.edge_color = (1, 1, 1)
        self.pos = (0, 0, 0)
        self.length = 2

        self.verticies = (
            (1, 1, 1),    # 0
            (1, 1, -1),   # 1
            (1, -1, 1),   # 2
            (1, -1, -1),  # 3
            (-1, 1, 1),   # 4
            (-1, 1, -1),  # 5
            (-1, -1, 1),  # 6
            (-1, -1, -1), # 7
        )

        self.edges = (
            (0, 1),  # 0 -> e6
            (0, 4),  # 1 -> e8
            (0, 2),  # 2 -> e7
            (1, 5),  # 3 -> e12
            (2, 6),  # 4 -> e2
            (2, 3),  # 5 -> e1
            (3, 7),  # 6 -> e4
            (3, 1),  # 7 -> e5
            (4, 6),  # 8 -> e9
            (4, 5),  # 9 -> e10
            (5, 7),  # 10 -> e11
            (6, 7),  # 11 -> e3
        )

        self.surfaces = (
            (5, 4, 11, 6), # face a
            (4, 2, 1, 8), # face b
            (0, 1, 9, 3), # face c
            (6, 7, 10, 3), # face d
            (5, 7, 0, 2), # face e
            (11, 8, 9, 10), # face f
        )

    def __init__(self, x = 0, y = 0, z = 0, l = 2):
        self.init_props()
        self.pos = (x, y, z)
        self.length = l

        self.move(x, y, z)
        
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
            for edge in surface:
                for vertex in self.edges[edge]:
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
    
    # face E {'a' 'b' 'c' 'd' 'e' 'f'}
    def get_face(self, face):
        faces = ['a', 'b', 'c', 'd', 'e', 'f']

        if face not in faces:
            raise TypeError(f"Error: face should be in {faces}")
        


    @staticmethod
    def tuple_add(t1, t2):
        l = len(t1)
        ret = []
        for i in range(l):
            ret.append(t1[i] + t2[i])
        return tuple(ret)