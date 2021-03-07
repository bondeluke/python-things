from math import tau

from src.graphics import Point, Line
from src.tools.line import rotate

def points_around(how_many: int, center: Point, distance: float, offset: float = 0):
    points = []
    reference_line = Line(center, Point(center.x, center.y + distance))
    for i in range(how_many):
        points.append(rotate(reference_line, tau / how_many * i + offset).p2)
    return points