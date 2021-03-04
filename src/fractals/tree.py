from math import tau

from src.graphics import Point
from src.tools.line import angled_line, magnitude_of, angle_of

def tree(window, r, d, s, a):
    branch1 = angled_line(r.p2, magnitude_of(r) * s, angle_of(r) + a)
    branch2 = angled_line(r.p2, magnitude_of(r) * s, angle_of(r) - a)

    branch1.setWidth(3)
    branch2.setWidth(3)

    branch1.draw(window)
    branch2.draw(window)
    if d > 1:
        tree(window, branch1, d - 1, s, a)
        tree(window, branch2, d - 1, s, a)

def tree_rotate(window, roots = 3):
    for a in range(roots):
        root = angled_line(Point(0, 0), 15, tau / roots * a + tau / 4)
        root.setWidth(3)
        root.draw(window)
        tree(window, root, 9, 8 / 13, tau / 5)
