from math import tau, sqrt, sin, cos, floor

from setup import window, draw_axes
from src.graphics import Point, color_rgb, Polygon, GraphicsObject, GraphWin, Text
from src.tools.points_around import points_around

def rotation(fraction):
    return fraction * tau

tile_radius = 4
layer_step = tile_radius * sqrt(3)
layer_padding = layer_step / 3

draw_axes()
radial_unit = 12
tick_angle = tau / radial_unit
step_angle = tau * 2 / radial_unit

class HexNode:
    def __init__(self, center, color, index, label=""):
        self.center = center
        self.color = color
        self.index = index
        self.label = label

    def get_tile(self):
        return hex_tile(self.center, self.color)

    def get_label(self):
        return Text(self.center, self.label)

def hex_tile(point: Point, color):
    polygon = Polygon(points_around(6, point, tile_radius))
    polygon.setWidth(3)
    polygon.setFill(color)
    return polygon

origin = Point(0, 0)

def points_in_between(p1, p2, how_many):
    points = []
    dx = (p2.x - p1.x)
    dy = (p2.y - p1.y)
    step_x = dx / (how_many + 1)
    step_y = dy / (how_many + 1)
    for index_from_p1 in range(1, how_many + 1):
        points.append(Point(p1.x + step_x * index_from_p1, p1.y + step_y * index_from_p1))

    return points

def h(n):
    if n == 0: return 0
    return 3 * n * (n - 1) + 1

def tile_layer(index: int, color):
    if index == 0:
        return [HexNode(origin, color, 0)]

    distance = (layer_step + layer_padding) * index
    pa = points_around(6, origin, distance, tick_angle + step_angle)

    tiles = []

    hn_prev = h(index)
    c = 0

    for point_index in range(6):
        current_point = pa[point_index]
        next_point = pa[(point_index + 1) % 6]
        tiles.append(HexNode(current_point, color, hn_prev + c))
        c += 1
        for p in points_in_between(current_point, next_point, index - 1):
            tiles.append(HexNode(p, color, hn_prev + c))
            c += 1

    return tiles

def cf(numerator, denominator):
    r_o = 0 * denominator / 3
    g_o = 1 * denominator / 3
    b_o = 2 * denominator / 3
    r = int((sin((numerator + r_o) * tau / denominator) + 1) / 2 * 255)
    g = int((sin((numerator + g_o) * tau / denominator) + 1) / 2 * 255)
    b = int((sin((numerator + b_o) * tau / denominator) + 1) / 2 * 255)
    return color_rgb(r, g, b)

layers = 6
all_tiles = []
for layer_index in range(layers):
    all_tiles.extend(tile_layer(layer_index, cf(layer_index, layers)))

def root(x):
    if x == 0: return 0
    return (3 + sqrt(12 * x - 3)) / 6

order = ["f", "d", "l", "b", "u", "r"]

def long_path_to(index):
    n = int(root(index))
    remainder = index - h(n)
    base = repeat("u", n)
    if remainder == 0:
        return base
    rest = ""
    count = 0
    for c in order:
        for i in range(n):
            rest += c
            count += 1
            if count == remainder:
                return base + rest

def repeat(string, how_many_times):
    result = ""
    for i in range(how_many_times):
        result += string
    return result

class Equivalence:
    def __init__(self, long, short):
        self.long = long
        self.short = short

equivalences = [
    # 2 -> 0
    Equivalence("ud", ""),
    Equivalence("rl", ""),
    Equivalence("fb", ""),

    # 2 -> 1
    Equivalence("uf", "r"),
    Equivalence("ul", "b"),
    Equivalence("db", "l"),
    Equivalence("dr", "f"),

    Equivalence("rd", "f"),
    Equivalence("rb", "u"),
    Equivalence("lu", "b"),
    Equivalence("lf", "d"),

    Equivalence("br", "u"),
    Equivalence("bd", "l"),
    Equivalence("fl", "d"),
    Equivalence("fu", "r"),
    #
    # # 3 -> 2
    # Equivalence("fru", "rr"),
    # Equivalence("urf", "rr"),
    #
    # Equivalence("dlb", "ll"),
    # Equivalence("bld", "ll"),
    #
    # Equivalence("rub", "uu"),
    # Equivalence("bur", "uu"),
    #
    # Equivalence("fdl", "dd"),
    # Equivalence("ldf", "dd"),
    #
    # Equivalence("dfr", "ff"),
    # Equivalence("rfd", "ff"),
    #
    # Equivalence("lbu", "bb"),
    # Equivalence("ubl", "bb")
]

def split(word):
    return [str(char) for char in word]

def reduce(path_string: str):
    for e in equivalences:
        eqs = split(e.long)
        e1 = eqs[0]
        e2 = eqs[1]
        if e1 in path_string and e2 in path_string:
            p1 = path_string.replace(e1, "", 1)
            p1 = p1.replace(e2, "", 1)
            p1 = p1 + e.short
            indexes = [path_string.find(e1), path_string.find(e2)]
            indexes.sort()
            result = path_string[:indexes[0]] + path_string[indexes[0] + 1:indexes[1]] + path_string[indexes[1] + 1:] + e.short
            # print(path_string, e1, e2, result)
            return reduce(result)

    return path_string

def draw():
    for t in all_tiles:
        n = int(root(t.index))
        long_path = long_path_to(t.index)
        t.label = "{}".format(reduce(long_path).upper())
        t.color = cf(n, layers)
        t.get_tile().draw(window)
        t.get_label().draw(window)

draw()

window.getMouse()
