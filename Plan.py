# * * * * * * * * * * * * * * * * * * * * * * * * #
#                                                 #
#   @Programmer: Hakim Beldjoudi                  #
#   @email: ih_beldjoudi@openfox.com              #
#   @Date: May 15th, 2022                         #
#   -> Meow                                       #
#                                                 #
# * * * * * * * * * * * * * * * * * * * * * * * * #

from OpenGL.GL import *
from OpenGL.GLU import *

class Plan:

    def __init__(self):
        self.x_show = True
        self.y_show = True
        self.z_show = True
        
        self.d = 10

        self.edge_color = (0.7, 0.7, 0.7, 0)
    
    def display(self):
        x_edge = (
            (-self.d, 0, 0),
            (self.d, 0, 0) 
        )

        y_edge = (
            (0, -self.d, 0),
            (0, self.d, 0)
        )

        z_edge = (
            (0, 0, -self.d),
            (0, 0, self.d)
        )

        edges = [x_edge, y_edge, z_edge]

        glBegin(GL_LINES)
        glColor4fv(self.edge_color)
        for edge in edges:
            for vx in edge:
                glVertex3fv(vx)
        glEnd()
