from math import tau

from setup import window, draw_axes, bottom, left, top, right
from src.exercises.music_circle import music_circle
from src.fractals.rectangles import rectangle_fractal
from src.fractals.tree import tree_rotate
from src.graphics import Rectangle, Point, color_rgb, Polygon, Line
from src.tools.line import rotate

draw_axes()

def points_around(center: Point, how_many: int = 6, distance: int = 6, ):
    points = []
    reference_line = Line(center, Point(center.x, center.y + distance))
    for i in range(how_many):
        points.append(rotate(reference_line, tau / how_many * i).p2)
    return points

p = Polygon(points_around(Point(0, 0)))
p.setFill(color_rgb(115, 155, 180))
p.draw(window)

window.getMouse()
