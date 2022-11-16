from point import *
from figure import *
from segment import *
from turtle import *


def drawPoint(t,p):
    t.up()
    t.width(10)
    t.pencolor(0, 0, 1)
    t.goto(p.get_cords()[0],p.get_cords()[1])
    t.dot()


def drawLine(t, p1, p2):
    t.up()
    t.width(10)
    t.pencolor(1, 0, 0)  # red
    t.goto(p1.get_cords()[0], p1.get_cords()[1])
    t.down()
    t.goto(p2.get_cords()[0], p2.get_cords()[1])


def drawFigure(t,figure):
    pts = figure.get_points()
    for i in range(0,len(pts)-1):
        drawLine(t,pts[i],pts[i+1])
    drawLine(t,pts[len(pts)-1],pts[0])


def main():
    # Generating figure and X-point:
    point1 = Point(10, 20)
    point2 = Point(30, 30)
    point3 = Point(20, 70)
    point4 = Point(60, 10)
    point5 = Point(80, 100)
    point6 = Point(110, 20)
    point7 = Point(130, 60)
    point8 = Point(170, -30)
    point9 = Point(140, -50)
    point10 = Point(110, -10)
    point11 = Point(90, -60)
    figure1 = Figure([point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11])
    X_point = Point(80,40)
    #Drawwing:
    t1 = Turtle()
    drawFigure(t1, figure1)
    drawPoint(t1, X_point)
    # Stage 1
    segments = []
    all_points = figure1.get_points()
    Rango = list(i for i in range(len(all_points) - 1))
    Rango.append(-1)
    Rango.append(0)
    for i in Rango:
        segments.append(Segment(all_points[i], all_points[i+1]))
    # Stage 2
    X_dots, Y_dots = [], []
    for segment in segments:
        x = segment.get_segmentDOT(X_point.get_cords()[0], 'x')
        y = segment.get_segmentDOT(X_point.get_cords()[1], 'y')
        if x is not None:
            Y_dots.append([x])
        if y is not None:
            X_dots.append([y])
    Y_dots.sort(key= lambda x: x[0])
    X_dots.sort(key= lambda x: x[0])
    for L in [Y_dots, X_dots]:
        for i in range(len(L)):
            L[i].append(i%2)
    # Stage 3
    if len(X_dots) <= 1  or len(Y_dots) <= 1\
    or X_point.get_cords()[0] < X_dots[0][0]\
    or X_point.get_cords()[0] > X_dots[-1][0]\
    or X_point.get_cords()[1] < Y_dots[0][0]\
    or X_point.get_cords()[1] > Y_dots[-1][0] :
        print(False)
        return
    trigger = [False, False]
    i = 0
    for dots in [X_dots, Y_dots]:
        for cord in dots:
            if cord[0] >= X_point.get_cords()[i]:
                if cord[1] == 1:
                    trigger[i] = True
                else:
                    print(False)
                    return
                break
        i = 1
    # Stage Finish
    if trigger[0] and trigger[1]:
        print(True)
        return
    print(False)

if __name__ == '__main__':
    main()
