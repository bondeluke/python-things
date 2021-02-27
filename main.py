from create_rectangle import create_rectangle, get_corners, get_corners_from_many
from graphics import Rectangle, Point, color_rgb
from setup import draw_axes, win

draw_axes()

w_modifier = 1/2
h_modifier = 1/2
r_modifier = 2
g_modifier = 3/2
b_modifier = 4/3

def rectangles_from(points, w_r, h_r, r, g, b):
    results = []
    for point in points:
        rect = create_rectangle(point, w_r , h_r, color_rgb(r, g, b))
        results.append(rect)
    return results

def recurse(n, seed, w, h, m, c_v, c_m):
    result = rectangles_from(seed, w, h, c_v[0] % 256, c_v[1] % 256, c_v[2] % 256)
    if n == 1: return result
    return recurse(n - 1, get_corners_from_many(result), w * m, h * m, m, [c_v[0] + c_m[0], c_v[1] + c_m[1], c_v[2] + c_m[2]], c_m) + result

for rectangle in recurse(6, [Point(0, 0)], 10, 8, 1/2, [28, 123, 128], [16, 4, 2]):
    rectangle.draw(win)

win.getMouse()
