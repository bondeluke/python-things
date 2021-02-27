from graphics import Line, Point, GraphWin, color_rgb
from math import cos, sin, sqrt, atan2

## Window has a 16:9 aspect ratio
_xScale = 16 # The horizontal value of the aspect ratio.
_yScale = 9  # The vertical value of the aspect ratio.
_gridScalar = 2   # The scale of the grid: Adjust as needed
_windowScalar = 7 # The scale of the window: Adjust as needed

left = _gridScalar * -_xScale
right = _gridScalar * _xScale
bottom = _gridScalar * -_yScale
top = _gridScalar * _yScale

win = GraphWin('Fractal', _xScale * _windowScalar * 20, _yScale * _windowScalar * 20)
win.setCoords(left, bottom, right, top)

_grey = color_rgb(200, 200, 200)
_darker_grey = color_rgb(180, 180, 180)
_x_axis = Line(Point(left, 0), Point(right, 0))
_x_axis.setFill(_grey)
_y_axis = Line(Point(0, bottom), Point(0, top))
_y_axis.setFill(_grey)

_ticks = []
for x in range(1, right, 1):
    if x % 5 == 0:
        t = Line(Point(x, -1), Point(x, 1))
        t.setFill(_darker_grey)
    else:
        t = Line(Point(x, -0.5), Point(x, 0.5))
        t.setFill(_grey)
    _ticks.append(t)

for x in range(-1, left, -1):
    if x % 5 == 0:
        t = Line(Point(x, -1), Point(x, 1))
        t.setFill(_darker_grey)
    else:
        t = Line(Point(x, -0.5), Point(x, 0.5))
        t.setFill(_grey)
    _ticks.append(t)

for y in range(1, top, 1):
    if y % 5 == 0:
        t = Line(Point(-1, y), Point(1, y))
        t.setFill(_darker_grey)
    else:
        t = Line(Point(-0.5, y), Point(0.5, y))
        t.setFill(_grey)
    _ticks.append(t)

for y in range(-1, bottom, -1):
    if y % 5 == 0:
        t = Line(Point(-1, y), Point(1, y))
        t.setFill(_darker_grey)
    else:
        t = Line(Point(-0.5, y), Point(0.5, y))
        t.setFill(_grey)
    _ticks.append(t)

# Draw the x-axis and y-axis to the window.
def draw_axes():
    _x_axis.draw(win)
    _y_axis.draw(win)

    for tick in _ticks:
        tick.draw(win)

## Utility functions ##
def simple_line(p1, p2):
    l = Line(p1, p2)
    l.setWidth(3)
    return l

def angled_line(p1, magnitude, theta):
    return rotate(Line(p1, Point(p1.x + magnitude, p1.y)), theta)

def parts_of(line):
    return line.p1.x, line.p1.y, line.p2.x, line.p2.y

def magnitude_of(line):
    x1, y1, x2, y2 = parts_of(line)
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

def angle_of(line):
    x1, y1, x2, y2 = parts_of(line)
    return atan2(y2 - y1, x2 - x1)

def rotate(line, theta):
    x1, y1, x2, y2 = parts_of(line)
    x = x2 - x1  # shift vector to origin
    y = y2 - y1  # shift vector to origin
    new_x = cos(theta) * x - sin(theta) * y + x1  # shift it back
    new_y = sin(theta) * x + cos(theta) * y + y1  # shift it back
    return simple_line(line.p1, Point(new_x, new_y))