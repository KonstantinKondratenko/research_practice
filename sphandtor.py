from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np


def draw_torus(inner_radius, outer_radius, x, y, z, segments=16, fill=True):

    glPushMatrix()
    glTranslatef(x, y, z)
    
    angles = [90,0,90]
    glRotatef(angles[0], 1, 0, 0)
    glRotatef(angles[1], 0, 1, 0)
    glRotatef(angles[2], 0, 0, 1)

    dlat = np.pi * 1.0 / segments
    dlon = np.pi * 2.0 / segments

    if not fill:
        glColor3fv((1, 0, 0))
        glBegin(GL_QUAD_STRIP)
        for lat in np.arange(0, np.pi, dlat):
            p1 = ((outer_radius + inner_radius * np.cos(lat))  * np.cos(0),
                   (outer_radius + inner_radius * np.cos(lat))  * np.sin(0),
                   inner_radius * np.sin(lat)
            )
            p2 = ((outer_radius + inner_radius * np.cos(lat + dlat))  * np.cos(0),
                   (outer_radius + inner_radius * np.cos(lat + dlat))  * np.sin(0),
                   inner_radius * np.sin(lat + dlat)
            )
            glVertex3fv(p1)
            glVertex3fv(p2)
            for lon in np.arange(0, 2 * np.pi, dlon):
                p1 = ((outer_radius + inner_radius * np.cos(lat))  * np.cos(lon),
                       (outer_radius + inner_radius * np.cos(lat))  * np.sin(lon),
                       inner_radius * np.sin(lat)
                )
                p2 = ((outer_radius + inner_radius * np.cos(lat + dlat))  * np.cos(lon),
                       (outer_radius + inner_radius * np.cos(lat + dlat))  * np.sin(lon),
                       inner_radius * np.sin(lat + dlat)
                )
                glVertex3fv(p1)
                glVertex3fv(p2)
        glEnd()
    else:
        glColor3fv((1, 1, 1))
        for lat in np.arange(0, np.pi + dlat, dlat):
            glBegin(GL_LINE_LOOP)
            for lon in np.arange(0, 2 * np.pi + dlon, dlon):
                p = ((outer_radius + inner_radius * np.cos(lat))  * np.cos(lon),
                     (outer_radius + inner_radius * np.cos(lat))  * np.sin(lon),
                     inner_radius * np.sin(lat)
                )
                glVertex3fv(p)
            glEnd()

    glColor3fv((1, 1, 1))

    glPopMatrix()


def draw_sphere(radius, x, y, z, segments=16, fill=True):
    
    glPushMatrix()
    glTranslatef(x, y, z)

    dlat = np.pi * 1.0 / segments
    dlon = np.pi * 2.0 / segments

    if not fill:
        glColor3fv((1, 0, 1)) 
        for lat in np.arange(0, np.pi + dlat, dlat):
            for lon in np.arange(0, 2 * np.pi + dlon, dlon):
                p1 = (radius * np.sin(lat) * np.cos(lon),
                       radius * np.sin(lat) * np.sin(lon),
                       radius * np.cos(lat))
                p2 = (radius * np.sin(lat + dlat) * np.cos(lon),
                       radius * np.sin(lat + dlat) * np.sin(lon),
                       radius * np.cos(lat + dlat)
                      )
                glBegin(GL_TRIANGLES)
                glVertex3fv(p1)
                glVertex3fv(p2)
                glVertex3fv((0, 0, 0))
                glEnd()

                p3 = (radius * np.sin(lat + dlat) * np.cos(lon + dlon),
                       radius * np.sin(lat + dlat) * np.sin(lon + dlon),
                       radius * np.cos(lat + dlat)
                      )
                glBegin(GL_TRIANGLES)
                glVertex3fv(p1)
                glVertex3fv(p3)
                glVertex3fv((0, 0, 0))
                glEnd()
    else:
        glColor3fv((1, 1, 1)) 
        for lat in np.arange(0, np.pi + dlat, dlat):
            glBegin(GL_LINE_LOOP)
            for lon in np.arange(0, 2 * np.pi + dlon, dlon):
                p = (radius * np.sin(lat) * np.cos(lon),
                     radius * np.sin(lat) * np.sin(lon),
                     radius * np.cos(lat)
                    )
                glVertex3fv(p)
            glEnd()

    glColor3fv((1, 1, 1))  

    glPopMatrix()