import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from pyramid import draw_pyramid
from cube import draw_cube
from sphandtor import draw_sphere, draw_torus
from par import draw_parallelepiped

class Sphere:
    def __init__(self, r, x, y, z, seg):
        self.r = r
        self.x = x 
        self.y = y 
        self.z = z 
        self.seg = seg
    
    def parse_xyz(self, sting):
        string = sting.split()
        self.x = float(string[0])
        self.y = float(string[1])
        self.z = float(string[2])


class Torus:
    def __init__(self, r_i, r_o, x, y, z, seg):
        self.r_i = r_i
        self.r_o = r_o
        self.x = x 
        self.y = y 
        self.z = z 
        self.seg = seg

    def parse_xyz(self, sting):
        string = sting.split()
        self.x = float(string[0])
        self.y = float(string[1])
        self.z = float(string[2])


class Pyr:
    def __init__(self, x, y, z, bs, h):
        self.x = x 
        self.y = y 
        self.z = z 
        self.bs = bs
        self.h = h 

    def parse_xyz(self, sting):
        string = sting.split()
        self.x = float(string[0])
        self.y = float(string[1])
        self.z = float(string[2])


class Cube:
    def __init__(self, x, y, z, size):
        self.x = x 
        self.y = y 
        self.z = z 
        self.size = size
    
    def parse_xyz(self, sting):
        string = sting.split()
        self.x = float(string[0])
        self.y = float(string[1])
        self.z = float(string[2])


def draw_coordinates():
    # вершины для системы координат
    coordinate_vertices = (
    (0, 0, 0), (10, 0, 0),  # ось x
    (0, 0, 0), (0, 10, 0),  # ось y
    (0, 0, 0), (0, 0, 10)   # ось z  
    )

    # цвета для системы координат
    coordinate_colors = (
        (1, 0, 0),  # красный для оси x
        (0, 1, 0),  # зеленый для оси y
        (0, 0, 1)   # синий для оси z
    )
    for i in range(3):  # для каждой оси (x, y, z)
        glColor3fv(coordinate_colors[i])  # установить цвет
        glBegin(GL_LINES)
        for vertex in range(2):  # для каждой вершины в оси
            glVertex3fv(coordinate_vertices[i * 2 + vertex])
        glEnd()
        glColor3fv((1,1,1))

def on_key_press(event):
    ret_array_pos = [0,0,0,0]

    zoom = None
    view = None
    coorflag = None
    reset = None

    if pygame.key.name(event.key) == 'left ctrl':
        reset = 1

    if pygame.key.name(event.key) == 'c':
        coorflag = 1

    if pygame.key.name(event.key) == 'v':
        view = 1

    if pygame.key.name(event.key) == 'z':
        ret_array_pos[0] += .3

    if pygame.key.name(event.key) == 'x':
        ret_array_pos[0] -= .3

    if pygame.key.name(event.key) == 'q':
        ret_array_pos[1] += 1

    if pygame.key.name(event.key) == 'a':
        ret_array_pos[1] -= 1

    if pygame.key.name(event.key) == 'w':
        ret_array_pos[2] += 1

    if pygame.key.name(event.key) == 's':
        ret_array_pos[2] -= 1

    if pygame.key.name(event.key) == 'e':
        ret_array_pos[3] += 1

    if pygame.key.name(event.key) == 'd':
        ret_array_pos[3] -= 1

    if pygame.key.name(event.key) == '[':
        zoom = 1

    if pygame.key.name(event.key) == ']':
        zoom = -1

    if pygame.key.name(event.key) == '`':
        ret_array_pos =  None
    

    print(f'Нажата клавиша {(pygame.key.name(event.key))}')
    return ret_array_pos, zoom, coorflag, view, reset


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    sphere = Sphere(.7, 0, 1, 0, 16)
    torus = Torus(.2, .4, 0, -3, 0, 16)
    pyramid = Pyr(0,-1, 0, 1, -3)
    cube = Cube(0,0,0,2)

    gluPerspective(100, (display[0] / display[1]), 0.1, 50.0)

    camera_zoom = 5
    zoom = None # это с клавы задавать чтобы зум
    cf = None # это с клавы задавать чтобы отрисовку координат
    vf = None
    res = None
    glTranslatef(0.0, 0.0, -camera_zoom)
    pos = [0.5, 0, 0, 0]

    coord_flag = False
    view_flag = False
    while True:

        key_pos = [0,0,0,0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                key_pos, zoom, cf, vf, res = on_key_press(event)
                if key_pos is None:
                    print('End of program!')
                    pygame.quit()
                    quit()
                    

        if cf is not None:
            coord_flag = not coord_flag
            cf = None    

        if vf is not None:
            view_flag = not view_flag
            vf = None        

        if res is not None:
            command = input('\
                            To resize cube press 1 \n \
                            To resize pyramid press 2 \n \
                            To resize torus press 3 \n \
                            To resize sphere press 4 \n \
                            ')
            if command == '1':
                command2 = input('\
                                 To set new pos press 1 \n \
                                 To set new seze press 2\n \
                                 ')
                if command2 == '1':
                    cube.parse_xyz(input("input x y z sep by space \n"))
                elif command2 == '2':
                    cube.size = float(input("input size \n"))
                else:
                    print('Unknown value!\n')
                    exit(1)
                    

            elif command == '2':
                command2 = input('\
                                 To set new pos press 1 \n \
                                 To set new base size press 2\n \
                                 To set new hieght press 3\n \
                                 ')
                if command2 == '1':
                    pyramid.parse_xyz(input("input x y z sep by space \n"))
                elif command2 == '2':
                    pyramid.bs = float(input("input size \n"))
                elif command2 == '3':
                    pyramid.h = -float(input("input hieght \n"))
                else:
                    print('Unknown value!\n')
                    exit(1)
                    
            elif command == '3': 
                command2 = input('\
                                 To set new pos press 1 \n \
                                 To set new insert radius press 2\n \
                                 To set new out radius press 3\n \
                                 ')
                if command2 == '1':
                    torus.parse_xyz(input("input x y z sep by space \n"))
                elif command2 == '2':
                    torus.r_i = float(input("input insert radius \n"))
                elif command2 == '3':
                    torus.r_o = float(input("input out radius \n"))
                else:
                    print('Unknown value!\n')
                    exit(1)

            elif command == '4':
                command2 = input('\
                                 To set new pos press 1 \n \
                                 To set new radius press 2\n \
                                 ')
                if command2 == '1':
                    sphere.parse_xyz(input("input x y z sep by space \n"))
                elif command2 == '2':
                    sphere.r = float(input("input insert radius \n"))
                else:
                    print('Unknown value!\n')
                    exit(1)
            else:
                print('Unknown value!\n')
                continue
            
            res = None

        for i in range(4):
            pos[i] += key_pos[i]
        glRotatef(*pos)
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        draw_sphere(sphere.r, sphere.x , sphere.y, sphere.z, sphere.seg, fill = view_flag)
        draw_pyramid(pyramid.x,pyramid.y, pyramid.z, pyramid.bs, pyramid.h, view_flag)
        draw_torus(torus.r_i, torus.r_o, torus.x, torus.y, torus.z, torus.seg, fill=view_flag)
        draw_cube(cube.x, cube.y, cube.z, cube.size, view_flag)
        draw_parallelepiped(cube.x + cube.size , cube.y, cube.z, cube.size/5 , cube.size, cube.size, view_flag)
        draw_parallelepiped(cube.x + cube.size - cube.size/3 , cube.y, cube.z, cube.size/5 , cube.size, cube.size, view_flag)



        if coord_flag:
            draw_coordinates() 


        if zoom is not None :
            camera_zoom += zoom
            print(f'set zoom {camera_zoom}')
            zoom = None
            glLoadIdentity()  # сбрасываем предыдущие преобразования
            gluPerspective(100, (display[0] / display[1]), 0.1, 50.0)  # повторно применяем перспективную проекцию
            glTranslatef(0.0, 0.0, -camera_zoom)  # применяем преобразование с учетом текущего значения camera_zoom


        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
