from math import sqrt, tau

from src.graphics import Circle, Point, color_rgb, Text, Line
from src.setup import window, draw_axes

import json

from src.tools.line import rotate

class Node:
    def __init__(self, text: str, center: Point, color: str, radius: int = 2):
        self.text = text
        self.center = center
        self.color = color
        self.radius = radius

    def draw(self, w):
        c = Circle(self.center, self.radius)
        c.setFill(self.color)
        c.draw(w)

        t = Text(self.center, self.text)
        t.draw(w)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_unit(self):
        return self.scale(1 / self.get_magnitude())

    def scale(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def to_line(self, p0: Point):
        line = Line(p0, Point(p0.x + self.x, p0.y + self.y))
        line.setArrow("last")
        return line

class Edge:
    def __init__(self, n0: Node, n1: Node, text: str):
        self.vector = Vector(n1.center.x - n0.center.x, n1.center.y - n0.center.y)
        self.n0 = n0
        self.n1 = n1
        self.text = text

    def draw(self, w):
        r0, r1 = self.n0.radius, self.n1.radius
        m = self.vector.get_magnitude()
        sm = m - r0 - r1
        p0 = self.vector.scale(r0 / m).to_line(self.n0.center).p2
        line = self.vector.scale(sm / m).to_line(p0)
        line.setWidth(3)
        line.draw(w)

        c = self.vector.scale(1 / 2).to_line(self.n0.center).p2
        text = Text(c, self.text)
        circ = Circle(c, 1)
        circ.setFill(color_rgb(255, 255, 255))
        circ.draw(w)
        text.draw(w)

draw_axes()

dictionary = json.loads('{"zero": 0 ,"one": "simple", "two":{ "21" : 3, "22": "Hello!", "23": {"four": 4, "five": 5, "six": 6} }, "three": "Ahoy!" }')
print(dictionary)

def handle_object(obj, p: Point, d: float, angle_offset=0, name=""):
    n = Node(name, p, color_rgb(200, 220, 255))

    if type(obj) == str:
        n = Node(obj, p, color_rgb(255, 220, 200))
        n.draw(window)
        return n
    if type(obj) == int:
        n = Node(str(obj), p, color_rgb(255, 220, 200))
        n.draw(window)
        return n

    num_keys = len(obj)
    n.draw(window)

    step = tau / num_keys
    tick = step / 2
    index = 0
    for key in obj:
        x = rotate(Line(p, Point(p.x + d, p.y)), step * index + angle_offset + tick).p2
        print(key, index)
        index += 1
        moon = handle_object(obj[key], x, d * 2 / 3, step * index + angle_offset, "")
        e = Edge(n, moon, key)
        e.draw(window)

    return n

handle_object(dictionary, Point(0, 0), 16, 0, "")

window.getMouse()
