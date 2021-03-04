from math import tau, sin
from src.graphics import Point, Line, Circle, color_rgb, Text
from src.tools.line import angled_line

def f(shift):
    return (sin(tau / 12 * (shift + .4)) + 1) / 2

def get_color(n, v = 1):
    if len(n) == v:
        return "black"
    return "white"

def music_circle(window):
    notes = ["C", "F", "Bb", "Eb", "Ab", "Db", "F#", "B", "E", "A", "D", "G"]
    circles = []
    lines = []
    text = []

    d1 = 20
    d2 = 14
    c_width = 4
    e_width = 4

    for i in range(12):
        r = f(i)
        g = f(i + 4)
        b = f(i + 8)
        note = notes[(i - 3) % 12]
        note2 = notes[(i + 6) % 12]

        c1 = Circle(angled_line(Point(0, 0), d1, tau / 12 * i).p2, d1 / 12 * 2)
        c1.setWidth(c_width)
        c1.setFill(color_rgb(int(255 * r), int(255 * g), int(255 * b)))
        c1b2 = Circle(c1.getCenter(), d1 / 12)
        c1b2.setWidth(0)
        c1b2.setFill(get_color(note, 2))

        c2 = Circle(angled_line(Point(0, 0), d2, tau / 12 * i + tau / 24).p2, d2 / 12 * 2)
        c2.setWidth(c_width)
        c2.setFill(color_rgb(int(255 * f(i + 9)), int(255 * f(i + 1)), int(255 * f(i + 5))))
        c2b2 = Circle(c2.getCenter(), d2 / 12)
        c2b2.setWidth(0)
        c2b2.setFill(get_color(note2, 2))

        circles.extend([c1, c2, c1b2, c2b2])

        t1, t2 = Text(c1.getCenter(), note), Text(c2.getCenter(), note2)
        t1.setFill(get_color(note))
        t1.setSize(30)
        t2.setFill(get_color(note2))
        t2.setSize(25)
        text.extend([t1, t2])

        e1 = Line(c1.getCenter(), angled_line(Point(0, 0), d2, tau / 12 * i + tau / 24).p2)
        e1.setWidth(e_width)
        e2 = Line(c1.getCenter(), angled_line(Point(0, 0), d2, tau / 12 * i - tau / 24).p2)
        e2.setWidth(e_width)
        e3 = Line(c1.getCenter(), angled_line(Point(0, 0), d1, tau / 12 * (i + 1)).p2)
        e3.setWidth(e_width)
        e4 = Line(c2.getCenter(), angled_line(Point(0, 0), d2, tau / 12 * (i + 1) + tau / 24).p2)
        e4.setWidth(e_width)
        lines.extend([e1, e2, e3, e4])

    for l in lines:
        l.draw(window)

    for c in circles:
        c.draw(window)

    for t in text:
        t.draw(window)
