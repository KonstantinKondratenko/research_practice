from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def get_pyramid_vertices(cx, cy, cz, base_size, height):
    half_base_size = base_size / 2
    vertices = (
        (cx, cy + height, cz),  # верхняя вершина пирамиды
        (cx + half_base_size, cy, cz + half_base_size),  # правая нижняя вершина пирамиды
        (cx - half_base_size, cy, cz + half_base_size),  # левая нижняя вершина пирамиды
        (cx - half_base_size, cy, cz - half_base_size),  # задняя нижняя вершина пирамиды
        (cx + half_base_size, cy, cz - half_base_size)   # передняя нижняя вершина пирамиды
    )
    return vertices

def draw_pyramid(cx, cy, cz, base_size, height, FLAG):
    pyramid_edges = (
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 1)
    )
    pyramid_vertices = get_pyramid_vertices(cx, cy, cz, base_size, height)
    if FLAG:
        glColor3fv((1, 1, 1)) 
        glBegin(GL_LINES)
        for edge in pyramid_edges:
            for vertex in edge:
                glVertex3fv(pyramid_vertices[vertex])
        glEnd()
    else:
        #/ Создаем список треугольных граней из списка ребер
        pyramid_faces = []
        for i in range(len(pyramid_edges)):
            if i % 4 == 0:  # Начинаем новую грань
                pyramid_faces.append([])
            pyramid_faces[-1].append(pyramid_edges[i][0])  # Добавляем вершину в текущую грань
        for face in pyramid_faces:
            glColor3fv((.9, .6, .5)) 
            glBegin(GL_TRIANGLES)
            for vertex in face:
                glVertex3fv(pyramid_vertices[vertex])
            glEnd()
        # Рисуем нижнюю грань пирамиды
        glBegin(GL_TRIANGLE_FAN)
        glVertex3fv(pyramid_vertices[0])  # Верхняя вершина пирамиды
        for vertex in pyramid_vertices[1:]:  # Все остальные вершины пирамиды
            glVertex3fv(vertex)
        glEnd()
        glColor3fv((1, 1, 1)) 