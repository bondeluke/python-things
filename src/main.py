from math import tau

from setup import window, draw_axes
from src.graphics import Point, color_rgb, Polygon
from src.tools.points_around import points_around

def rotation(fraction):
    return fraction * tau

draw_axes()
unit = 12
tick_angle = tau / unit
step_angle = tau * 2 / unit

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
all_tiles.extend(tile_layer(0, color_rgb(10, 15, 20)   , 0       , 0         ))
all_tiles.extend(tile_layer(1, color_rgb(215, 155, 110), 3.46    , 0         ))
all_tiles.extend(tile_layer(2, color_rgb(155, 215, 20 ), 6       , rotation(1/12)))
all_tiles.extend(tile_layer(3, color_rgb(10, 15, 155)  , 3.46 * 2, rotation(2/12)))
all_tiles.extend(tile_layer(4, color_rgb(10, 156, 155) , 10.5    , rotation(3/24)))

for t in all_tiles:
    t.draw(window)

window.getMouse()
