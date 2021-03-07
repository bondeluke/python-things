from math import tau, sqrt, sin, cos

from setup import window, draw_axes
from src.graphics import Point, color_rgb, Polygon
from src.tools.points_around import points_around

def rotation(fraction):
    return fraction * tau

layer_step = 2 * sqrt(3)

draw_axes()
unit = 12
tick_angle = tau / unit
step_angle = tau * 2 / unit

def tile(point: Point, color, ta):
    polygon = Polygon(points_around(6, point, 2, ta))
    polygon.setWidth(3)
    polygon.setFill(color)
    return polygon

origin = Point(0, 0)

def tile_layer2(layer_index: int, color, distance, offset: float):
    if layer_index == 0:
        o_tile = tile(origin, color, tick_angle)
        return [o_tile]

    tiles = []

    for point in points_around(6, origin, distance, offset):
        tiles.append(tile(point, color, tick_angle))

    return tiles

def points_in_between(p1, p2, how_many):
    points = []
    dx = (p2.x - p1.x)
    dy = (p2.y - p1.y)
    step_x = dx / (how_many + 1)
    step_y = dy / (how_many + 1)
    for index_from_p1 in range(1, how_many + 1):
        points.append(Point(p1.x + step_x * index_from_p1, p1.y + step_y * index_from_p1))

    return points

def tile_layer(index: int, color):
    if index == 0:
        return [tile(origin, color, tick_angle)]

    distance = layer_step * index
    pa = points_around(6, origin, distance)

    tiles = []

    for point in pa:
        tiles.append(tile(point, color, tick_angle))

    for point_index in range(6):
        current_point = pa[point_index]
        next_point = pa[(point_index + 1) % 6]
        for p in points_in_between(current_point, next_point, index - 1):
            tiles.append(tile(p, color, tick_angle))

    return tiles

def cf(numerator, denominator):
    r_o = 0 * denominator / 3
    g_o = 1 * denominator / 3
    b_o = 2 * denominator / 3
    r = int((sin((numerator + r_o) * tau / denominator) + 1) / 2  * 255)
    g = int((sin((numerator + g_o) * tau / denominator) + 1) / 2  * 255)
    b = int((sin((numerator + b_o) * tau / denominator) + 1) / 2  * 255)
    return color_rgb(r, g, b)

layers = 12
all_tiles = []
for layer_index in range(layers):
    all_tiles.extend(tile_layer(layer_index, cf(layer_index, layers)))

for t in all_tiles:
    t.draw(window)

window.getMouse()
