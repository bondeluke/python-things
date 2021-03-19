from graphics import Line, Point, GraphWin, color_rgb

## Window has a 16:9 aspect ratio
_xScale = 16 # The horizontal value of the aspect ratio.
_yScale = 9  # The vertical value of the aspect ratio.
_gridScalar = 8   # The scale of the grid: Adjust as needed
_windowScalar = 7 # The scale of the window: Adjust as needed

left = _gridScalar * -_xScale
right = _gridScalar * _xScale
bottom = _gridScalar * -_yScale
top = _gridScalar * _yScale

window = GraphWin('Fractal', _xScale * _windowScalar * 20, _yScale * _windowScalar * 20)
window.setCoords(left, bottom, right, top)

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
    _x_axis.draw(window)
    _y_axis.draw(window)

    for tick in _ticks:
        tick.draw(window)