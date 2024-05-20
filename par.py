from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def get_parallelepiped_vertices(cx, cy, cz, a, b, c):
    vertices = (
        (cx + a/2, cy - b/2, cz - c/2),
        (cx + a/2, cy + b/2, cz - c/2),
        (cx - a/2, cy + b/2, cz - c/2),
        (cx - a/2, cy - b/2, cz - c/2),
        (cx + a/2, cy - b/2, cz + c/2),
        (cx + a/2, cy + b/2, cz + c/2),
        (cx - a/2, cy - b/2, cz + c/2),
        (cx - a/2, cy + b/2, cz + c/2)
    )
    return vertices

def draw_parallelepiped(cx, cy, cz, a, b, c, FLAG):

    vertices = get_parallelepiped_vertices(cx, cy, cz, a, b, c)
    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        (5, 7)
        )

    if FLAG:
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()
    else:
        glColor3fv((.1, .7, .2))
        glBegin(GL_POLYGON)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()
    glColor3fv((1, 1, 1))
