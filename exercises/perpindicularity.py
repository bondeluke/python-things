from graphics import Circle, Text, Oval
from setup import *
from vector import vector

draw_axes()

def slope(v):
    return (v.p2.x - v.p1.x), (v.p2.y - v.p1.y)

cp = Point(12, 17)
c = Circle(cp, 2)
c.setFill(color_rgb(30, 120, 150))
c.draw(win)

line1 = vector(Point(0, 0), Point(-12, 12))
line1.draw(win)

line2 = vector(cp, Point(10, 10))
line2.draw(win)

t1 = Text(Point(5, -5), "waiting..")
t1.draw(win)

while True:
    mp = win.getMouse()
    mp = Point(int(mp.x), int(mp.y))
    line1.undraw()
    line2.undraw()
    t1.undraw()

    line1.p2 = mp
    line1.p1 = Point(0, 0)
    x, y = slope(line1)
    line1.p1 = Point(-mp.x, -mp.y)
    line2.p2 = Point(cp.x - y, cp.y + x)
    t1.setText("{0}y = {1}x".format(x, y))

    line1.draw(win)
    line2.draw(win)
    t1.draw(win)




