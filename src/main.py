from math import tau, sin, sqrt

from src.graphics import color_rgb, Text, Point, Circle, Line
from src.hexagon_madness import hexagonal_madness
from src.setup import window, draw_axes

window.setBackground(color_rgb(255, 255, 255))

draw_axes()

hexagonal_madness(window, Point(0, 0))

window.getMouse()
