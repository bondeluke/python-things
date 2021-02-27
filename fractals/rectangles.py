from create_rectangle import create_rectangle, get_corners_from_many
from graphics import Point, color_rgb
from setup import draw_axes, win

def rectangles_from(points, w_r, h_r, r, g, b):
    results = []
    for point in points:
        rect = create_rectangle(point, w_r, h_r, color_rgb(r, g, b))
        results.append(rect)
    return results

def recurse(n, seed, w, h, m, c_v, c_m):
    result = rectangles_from(seed, w, h, c_v[0] % 256, c_v[1] % 256, c_v[2] % 256)
    if n == 1: return result
    return recurse(n - 1, get_corners_from_many(result), w * m, h * m, m, [c_v[0] + c_m[0], c_v[1] + c_m[1], c_v[2] + c_m[2]], c_m) + result

def rectangle_fractal(layers):
    draw_axes()

    for rectangle in recurse(layers, [Point(0, 0)], 9, 8, 1/2, [35 * 7, 25 * 7, 24 * 7 + 56], [-35, -25, -24]):
        rectangle.draw(win)

    win.getMouse()
