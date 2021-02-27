from math import tau
from setup import *
from graphics import *

draw_axes()

def draw_wheel(position, number_of_spokes, radius, color):
    # Draw the circle and the initial line
    c = Circle(position, radius)
    c.setWidth(3)
    c.setOutline(color)
    c.draw(win)

    line = Line(position, Point(position.x + radius, position.y))

    for n in range(0, number_of_spokes):
        rl = rotate(line, n * tau / number_of_spokes)
        rl.setFill(color)
        rl.draw(win)

draw_wheel(Point(0, 0), 12, 7, color_rgb(128, 0, 0))
draw_wheel(Point(-16, 8), 25, 8, color_rgb(0, 128, 0))
draw_wheel(Point(18, -5), 15, 9, color_rgb(0, 0, 128))
draw_wheel(Point(-16, -8), 27, 5, color_rgb(128, 64, 0))
draw_wheel(Point(18, 13), 8, 3, color_rgb(0, 64, 128))

win.getMouse()