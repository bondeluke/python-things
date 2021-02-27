from math import tau

from graphics import Point
from setup import rotate, angled_line, magnitude_of, simple_line, draw_axes, angle_of, win

def spoke_it(line, divisions):
    result = []
    for s in range(0, divisions):
        if s % 2 == 0:
            result.append(rotate(line, s * tau / divisions))
        result.append(rotate(line, s * tau / divisions))
    return result

def repeat(n, source, scale, divisions):
    if n == 1: return source
    result = []
    for line in source:
        result.extend(spoke_it(angled_line(line.p2, magnitude_of(line) * scale, angle_of(line)), divisions))
    return source + repeat(n - 1, result, scale, divisions)

draw_axes()

# first_layer = spoke_it(, 4)
# second_layer = repeat(first_layer, 1 / 2, 4)
# third_layer = repeat(second_layer, 1 / 2, 4)

for l in repeat(4, spoke_it(simple_line(Point(0, 0), Point(8, 0)), 6), 1 / 3, 6):
    l.draw(win)

win.getMouse()
win.close()
