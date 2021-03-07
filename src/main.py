from math import tau

from setup import window, draw_axes, bottom, left, top, right
from src.exercises.music_circle import music_circle
from src.fractals.rectangles import rectangle_fractal
from src.fractals.tree import tree_rotate
from src.graphics import Rectangle, Point, color_rgb, Polygon, Line
from src.tools.line import rotate

draw_axes()
tick_angle = tau / 12

def points_around(center: Point, distance: float, offset: float, how_many: int = 6):
    points = []
    reference_line = Line(center, Point(center.x, center.y + distance))
    for i in range(how_many):
        points.append(rotate(reference_line, tau / how_many * i + offset).p2)
    return points

def tile(point: Point, color, ta):
    polygon = Polygon(points_around(point, 2, ta))
    polygon.setWidth(3)
    polygon.setFill(color)
    return polygon

origin = Point(0, 0)

def tile_layer(layer_index: int, color, distance, offset: float):
    if layer_index == 0:
        o_tile = tile(origin, color, tick_angle)
        return [o_tile]

    tiles = []

    for point in points_around(origin, distance, offset):
        tiles.append(tile(point, color, tick_angle))

    return tiles

all_tiles = []
all_tiles.extend(tile_layer(0, color_rgb(10, 15, 20)   , 0   , 0         ))
all_tiles.extend(tile_layer(1, color_rgb(215, 155, 110), 3.46, 0         ))
all_tiles.extend(tile_layer(2, color_rgb(155, 215, 20 ), 6   , tick_angle))
all_tiles.extend(tile_layer(3, color_rgb(10, 15, 155)  , 3.46 * 2, tau / 6   ))

for t in all_tiles:
    t.draw(window)

window.getMouse()
