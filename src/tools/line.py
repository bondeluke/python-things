from math import sqrt, atan2, sin, cos
from src.graphics import Line, Point

def components_of(line):
    return line.p1.x, line.p1.y, line.p2.x, line.p2.y

def magnitude_of(line):
    x1, y1, x2, y2 = components_of(line)
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

def angle_of(line):
    x1, y1, x2, y2 = components_of(line)
    return atan2(y2 - y1, x2 - x1)

def vector(p1, p2):
    v = Line(p1, p2)
    v.setWidth(3)
    v.setArrow("last")
    return v

def rotate(line, theta):
    x1, y1, x2, y2 = components_of(line)
    x = x2 - x1  # shift vector to origin
    y = y2 - y1  # shift vector to origin
    new_x = cos(theta) * x - sin(theta) * y + x1  # shift it back
    new_y = sin(theta) * x + cos(theta) * y + y1  # shift it back
    return Line(line.p1, Point(new_x, new_y))

def reflect(line, point):
    d_v = distance_vector(line, point)
    xd = d_v.p2.x - d_v.p1.x
    yd = d_v.p2.y - d_v.p1.y
    return Point(int(point.x + xd * 2), int(point.y + yd * 2))

def angled_line(p1, magnitude, theta):
    return rotate(Line(p1, Point(p1.x + magnitude, p1.y)), theta)

def distance_vector(line, point):
    a = magnitude_of(line)
    b = magnitude_of(Line(line.p1, point))
    c = magnitude_of(Line(line.p2, point))

    m = (a * a + b * b - c * c) / (2 * a)
    return Line(point, angled_line(line.p1, m, angle_of(line)).p2)