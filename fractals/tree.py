from math import tau

from graphics import Point
from setup import win, angled_line, magnitude_of, angle_of

def repeat(r, d, s, a):
    branch1 = angled_line(r.p2, magnitude_of(r) * s, angle_of(r) + a)
    branch2 = angled_line(r.p2, magnitude_of(r) * s, angle_of(r) - a)

    branch1.draw(win)
    branch2.draw(win)
    if d > 1:
        repeat(branch1, d - 1, s, a)
        repeat(branch2, d - 1, s, a)

def tree():
    origin = Point(0, 0)

    roots = 3
    depth = 9
    rootLength = 15
    scalar = 8 / 13
    angle = tau / 6

    for a in range(roots):
        root = angled_line(origin, rootLength, tau / roots * a + tau / 4)
        root.draw(win)
        repeat(root, depth, scalar, angle)
