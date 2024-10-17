import numpy as np
import random
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


from OpenGL.GLUT import glutStrokeCharacter, GLUT_STROKE_ROMAN



def draw_points(x, y, color):
    glColor(*color)

    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def find_zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx >= 0 and dy <= 0:
            return 7
        elif dx <= 0 and dy >= 0:
            return 3
        elif dx <= 0 and dy <= 0:
            return 4
    else:
        if dx >= 0 and dy >= 0:
            return 1
        elif dx <= 0 and dy >= 0:
            return 2
        elif dx <= 0 and dy <= 0:
            return 5
        elif dx >= 0 and dy <= 0:
            return 6

def to_zone0(zone, x, y):
    if zone == 0:
        return (x, y)
    elif zone == 1:
        return (y, x)
    elif zone == 2:
        return (y, -x)
    elif zone == 3:
        return (-x, y)
    elif zone == 4:
        return (-x, -y)
    elif zone == 5:
        return (-y, -x)
    elif zone == 6:
        return (-y, x)
    elif zone == 7:
        return (x, -y)
    else:
        raise ValueError("Zone must be in [0, 7]")

def to_zoneM(zone, x, y):
    if zone == 0:
        return (x, y)
    elif zone == 1:
        return (y, x)
    elif zone == 2:
        return (-y, x)
    elif zone == 3:
        return (-x, y)
    elif zone == 4:
        return (-x, -y)
    elif zone == 5:
        return (-y, -x)
    elif zone == 6:
        return (y, -x)
    elif zone == 7:
        return (x, -y)
    else:
        raise ValueError("Zone must be in [0, 7]")

def midpoint_line(x1, y1, x2, y2, color):
    zone = find_zone(x1, y1, x2, y2)
    x1, y1 = to_zone0(zone, x1, y1)
    x2, y2 = to_zone0(zone, x2, y2)

    dx = x2 - x1
    dy = y2 - y1

    d = 2 * dy - dx
    incrE = 2 * dy
    incrNE = 2 * (dy - dx)

    x = x1
    y = y1
    x0, y0 = to_zoneM(zone, x, y)

    draw_points(x0, y0, color)
    while x < x2:
        if d <= 0:
            d = d + incrE
            x = x + 1
        else:
            d = d + incrNE
            x = x + 1
            y = y + 1
        x0, y0 = to_zoneM(zone, x, y)

        draw_points(x0, y0, color)


class MidpointCircle:
    def __init__(self, circle_x, circle_y, r=5):
        self.circle_x = circle_x
        self.circle_y = circle_y
        self.r = r

    def circlepoints(self, x, y, color):
        draw_points(self.circle_x + x, self.circle_y + y, color) #oct1
        draw_points(self.circle_x - x, self.circle_y + y, color) #2
        draw_points(self.circle_x - y, self.circle_y + x, color) #3
        draw_points(self.circle_x + y, self.circle_y + x, color)
        draw_points(self.circle_x + y, self.circle_y - x, color)
        draw_points(self.circle_x - y, self.circle_y - x, color)
        draw_points(self.circle_x - x, self.circle_y - y, color)
        draw_points(self.circle_x + x, self.circle_y - y, color) #8

    def draw(self, color):
        x = 0
        y = self.r
        d = 1 - self.r

        self.circlepoints(x, y, color)

        while x < y:
            x += 1
            if d < 0:
                d += 2 * x + 1
            else:
                y -= 1
                d += 2 * (x - y) + 1
            self.circlepoints(x, y, color)

def init():
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 800, 0, 500, 0, 1)  # l,r,b,t,n,f

    glMatrixMode(GL_MODELVIEW)



def treetwnig():
    glPointSize(20)
    # Draw the four sides of the tree trunk using the midpoint line algorithm
    midpoint_line(100, 150, 120, 150,(0.5, 0.35, 0.05))
    midpoint_line(120, 150, 120, 320,(0.5, 0.35, 0.05))
    midpoint_line(120, 320, 100, 320,(0.5, 0.35, 0.05))
    midpoint_line(100, 320, 100, 150,(0.5, 0.35, 0.05))

    glPointSize(7)

def tree ():
    glPointSize(45)
    midpoint_circle = MidpointCircle(100, 280, 36)
    glColor(0, 0.4, 0)
    midpoint_circle.draw((0, 0.4, 0))
    midpoint_circle = MidpointCircle(155, 300, 36)
    glColor(0, 0.4, 0)
    midpoint_circle.draw((0, 0.4, 0))
    midpoint_circle = MidpointCircle(60, 330, 36)
    glColor(0, 0.4, 0)
    midpoint_circle.draw((0, 0.4, 0))
    midpoint_circle = MidpointCircle(95, 380, 36)
    glColor(0, 0.4, 0)
    midpoint_circle.draw((0, 0.4, 0))
    midpoint_circle = MidpointCircle(110, 335, 36)
    glColor(0, 0.4, 0)
    midpoint_circle.draw((0, 0.4, 0))
    midpoint_circle = MidpointCircle(150, 360, 30)
    glColor(0, 0.4, 0)
    midpoint_circle.draw((0, 0.4, 0))

    glPointSize(2)

def moon():
    glPointSize(20)
    midpoint_circle = MidpointCircle(600, 400, 50)
    glColor(1, 1, 0.5)
    midpoint_circle.draw((1, 1, 0.5))
    glPointSize(40)
    midpoint_circle = MidpointCircle(600, 400, 25)
    glColor(1, 1, 0.5)
    midpoint_circle.draw((1, 1, 0.5))
    glPointSize(2)


def greenground():
    glPointSize(100)
    midpoint_line(0, 150, 800, 150, (0, 0.4, 0))



def shootsquare():
    #glColor3f,(0,0,0)
    glPointSize(2)
    midpoint_line(770, 40, 690, 40,(0,0,0))
    midpoint_line(690, 40, 690, 10,(0,0,0))
    midpoint_line(690, 10, 770, 10,(0,0,0))
    midpoint_line(770, 10, 770, 40,(0,0,0))


def scoresquare():
    #glColor3f(0,0,0)
    glPointSize(2)
    midpoint_line(500, 40, 420, 40,(0,0,0))
    midpoint_line(420, 40, 420, 10,(0,0,0))
    midpoint_line(420, 10, 500, 10,(0,0,0))
    midpoint_line(500, 10, 500, 40,(0,0,0))


def triessquare():
    #glColor3f(0,0,0)
    glPointSize(2)
    midpoint_line(680, 40, 600, 40,(0,0,0))
    midpoint_line(600, 40, 600, 10,(0,0,0))
    midpoint_line(600, 10, 680, 10,(0,0,0))
    midpoint_line(680, 10, 680, 40,(0,0,0))

def livessquare():     #tries
    #glColor3f(0,0,0)
    glPointSize(2)
    midpoint_line(590, 40, 510, 40,(0,0,0))
    midpoint_line(510, 40, 510, 10,(0,0,0))
    midpoint_line(510, 10, 590, 10,(0,0,0))
    midpoint_line(590, 10, 590, 40,(0,0,0))


def ground2():
    glPointSize(120)
    midpoint_line(0, 60, 800, 60, (0.75,0.75,0.75))


def display1():
    tree()
    moon()
    treetwnig()

    greenground()
    scoresquare()  # score
    shootsquare()  # shuts
    livessquare()  # lives
    triessquare()
    ground2()



s = 30
def Chicken(x, y, z, rwy):
    # Wings (Points and Midpoint Line Algorithm)
    glPointSize(7)
    wing_length = round(s * 0.2)
    wing_height = round(s * 0.1)

    # Right Wing
    wing_start_x_right = x + round(s * 0.4)
    wing_start_y_right = y + round(s * 0.8) - round(s * 0.35)

    wing_end_x_right = wing_start_x_right + wing_length
    wing_end_y_right = wing_start_y_right - wing_height

    draw_points(wing_start_x_right, wing_start_y_right, (0.0, 0.0, 1.0))
    draw_points(wing_end_x_right, wing_end_y_right, (0.0, 0.0, 1.0))

    # Use midpoint line algorithm to draw the right wing
    midpoint_line(wing_start_x_right, wing_start_y_right, wing_end_x_right, wing_end_y_right, (0.0, 0.0, 1.0))

    # Left Wing
    wing_start_x_left = x - round(s * 0.4)
    wing_end_x_left = wing_start_x_left - wing_length

    wing_start_y_left = y + round(s * 0.8) - round(s * 0.35)
    wing_end_y_left = wing_start_y_left - wing_height

    draw_points(wing_start_x_left, wing_start_y_left, (0.0, 0.0, 1.0))
    draw_points(wing_end_x_left, wing_end_y_left, (0.0, 0.0, 1.0))

    # Use midpoint line algorithm to draw the left wing
    midpoint_line(wing_start_x_left, wing_start_y_left, wing_end_x_left, wing_end_y_left, (0.0, 0.0, 1.0))

    # Eyes
    glPointSize(2)
    midpoint_circle = MidpointCircle(x + round(s * 0.15), y + round(s * 0.95), r=round(s * 0.1))
    glColor(1, 1, 1)
    midpoint_circle.draw((1, 1, 1))

    midpoint_circle = MidpointCircle(x - round(s * 0.15), y + round(s * 0.95), r=round(s * 0.1))
    glColor(1, 1, 1)
    midpoint_circle.draw((1, 1, 1))

    midpoint_circle = MidpointCircle(x + round(s * 0.15), y + round(s * 0.95) + round(s * 0.1), r=round(s * 0.05))
    glColor(0, 0, 1)
    midpoint_circle.draw((0, 0, 1))

    midpoint_circle = MidpointCircle(x - round(s * 0.15), y + round(s * 0.95) + round(s * 0.1), r=round(s * 0.05))
    glColor(0, 0, 1)
    midpoint_circle.draw((0, 0, 1))

    # Head
    glPointSize(10)
    midpoint_circle = MidpointCircle(x, y + round(s * 0.8), r=round(s * 0.35))
    glColor(0.8, 0.2, 0.2)
    midpoint_circle.draw((0.8, 0.2, 0.2))

    # Body
    glPointSize(18)
    midpoint_circle = MidpointCircle(x, y, r=round(s * 0.4))
    glColor(0.961, 0.51, 0.031)
    midpoint_circle.draw((0.961, 0.51, 0.031))

    # Legs
    # Right Upper
    glPointSize(6)
    midpoint_circle = MidpointCircle(x - round(s * 0.3), y - round(s * 0.7), r=round(s * 0.2))
    glColor(1.0, 0.0, 0.0)
    midpoint_circle.draw((1.0, 0.0, 0.0))

    # Left Upper
    midpoint_circle = MidpointCircle(x + round(s * 0.4), y - round(s * 0.7), r=round(s * 0.2))
    glColor(1.0, 0.0, 0.0)
    midpoint_circle.draw((1.0, 0.0, 0.0))

    glPointSize(7)
    # Mouth
    midpoint_line(x, y + round(s * 0.8), x, y + round(s * 1.35), (1, 1, 0))


class LINE:
    def __init__(self, left, right, top, bottom):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top

class cir:
    def __init__(self, x, y):
        self.x0 = x
        self.y0 = y



x = 0
y = 0
radius = 10
def draw_circle(circle, num_points=100):
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(2.0)
    glBegin(GL_POINTS)

    x_center, y_center = circle.x0, circle.y0 + 500

    for i in range(num_points):
        angle = 2 * pi * i / num_points
        x = x_center + radius * cos(angle)
        y = y_center + radius * sin(angle)
        glVertex2d(x, y)

    glEnd()


#-------------------------------------------------------------

mouse_x = 0
mouse_y = 0


def MouseMotion(x, y):
    global mouse_x
    global mouse_y
    mouse_x = x
    mouse_y = -y


Hit = False
r = 0
g = 0
b = 0
Score = 0
Level = 1
Tries = 3
Hits = 3


def MouseAction(button, state, x, y):
    global Hit, r, g, b, k, n, Target, mouse_x, mouse_y, movement1, movement2, Score, Level, Hits, Tries, time_interval
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:

            Hits -= 1
            if movement2.top + 510 <= Target.top and movement2.top + 490 >= Target.bottom and movement2.right + 20 / 2 <= Target.right and movement2.left + 20 / 2 >= Target.left:

                Hit = True
                Score += 1
                if Score % 5 == 0:
                    Level += 1
                    time_interval-=3

            else:

                if Hits == 0:
                    Tries -= 1
                    Hits = 3



time_interval = 70
def Timer(v):
    Display()
    glutTimerFunc(time_interval, Timer, 1)


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


animated = 1
Valid = 0
Valid2 = 0


def keyboard(key, x, y):
    global animated, Valid, Valid2
    if key == b"p":
        animated = 0
        Valid2 = 1
    if key == b"c":
        animated = 1
        Valid2 = 0
    if key == b"r":
        restart_program()


Shift = 0


def Sin(a, Shift):
    y = 200 * sin(a / 16) + Shift
    return y


def Straight(a, Shift):
    y = a + Shift
    return y


def Cos(a, Shift):
    y = 100 * cos(a / 8) + Shift
    return y


def init_start():
    initi = random.randrange(20, 600)
    return initi


def random_path(path_selection, x):
    if path_selection == 0:
        y = Sin(x, Shift)
        return y

    if path_selection == 1:
        y = Straight(x, Shift)
        return y

    if path_selection == 2:
        y = Cos(x, Shift)
        return y


def drawText(string, x, y):
    glLineWidth(1)
    glColor(0.21, 0.21, 0.21)  # Yellow Color
    glLoadIdentity()
    glTranslate(x, y, 0)
    glScale(0.13, 0.13, 1)
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)


Target = LINE(-20, 20, 35, -29)
movement1 = cir(65, 15)
movement2 = LINE(0, 0, 60, 10)
x1 = 0
mov = 0
y1 = 0
z1 = 0
Wing = 0
path = 0
path_selection = 0
speed = 0.1
Disappear = 0


def Display():
    global movement1, movement2, x1, y1, z1, Wing, Hit, Target, r, g, b, animated, path_selection, mov, path, initi, speed, Shift, Disappear, Score, Level, Tries, Hits, Valid, Valid2, WingMov

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    string = "Score: " + str(Score)
    drawText(string, 425, 20)
    string = "Level: " + str(Level)
    drawText(string, 515, 20)
    string = "Tries: " + str(Tries)
    drawText(string, 605, 20)
    string = "Hits: " + str(Hits)
    drawText(string, 695, 20)


    if Tries == 0:
        animated = 0
        string = "Game Over"
        drawText(string, 350, 250)
        string = "press (R) to Restart"
        drawText(string, 300, 225)
        if Valid == 1:
            sys.exit()

    if Valid2 == 1:
        string = "press (C) to Continue"
        drawText(string, 350, 250)

    glLoadIdentity()
    glColor(0.6, 0.3, 5.9)
    # DrawMidpointLine(Target)

    glLoadIdentity()

    movement1.x0 = (mouse_x + 1) * animated
    movement1.y0 = (mouse_y + 1) * animated
    draw_circle(movement1)

    glLoadIdentity()

    movement2.left = (mouse_x - 1) * animated
    movement2.right = (mouse_x + 1) * animated
    movement2.top = (mouse_y + 1) * animated
    movement2.bottom = (mouse_y - 1) * animated


    if mov == 0:
        path_selection = 0

    y1 = random_path(path_selection, mov)

    if Hit is False:
        Chicken(x1 + mov, y1 + 210, z1, Wing)

        mov = mov + (5 + speed) * animated
        Shift = Shift + (2) * animated
        Target.right = x1 + mov + 25
        Target.left = Target.right - 52
        Target.top = y1 + 250
        Target.bottom = Target.top - 64

    if x1 + mov >= 800 or y1 >= 500 or Hit == True:
        Tries -= 1
        if Hit is True:
            Hits = 3
            Tries+=1
            Chicken(x1 + mov, y1 - Disappear, z1, Wing)
            Wing = 0
            Disappear += 30
            if Disappear > 500:
                Hit = False

                mov = 10
                speed = speed + 0.1
                x1 = init_start()
                path_selection = random.randrange(0, 2, 1)
                Shift = 0
                Disappear = 0

        else:
            Hits = 3
            mov = 10
            speed = speed + 0.1
            x1 = init_start()
            path_selection = random.randrange(0, 2, 1)
            Shift = 0
            Hit = False

    glLoadIdentity()
    display1()

    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Bird Shooter")
    glutDisplayFunc(Display)
    glutTimerFunc(time_interval, Timer, 1)
    glutPassiveMotionFunc(MouseMotion)
    glutMouseFunc(MouseAction)
    glutSetCursor(GLUT_CURSOR_NONE)
    glutKeyboardFunc(keyboard)
    init()
    glutMainLoop()


main()