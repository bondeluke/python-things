from math import sin, tau, sqrt
from src.Node import Node
from src.graphics import Point, color_rgb, Line
from src.math.hexagonal_numbers import hexagonal_inverse, hexagonal
from src.string_tools import split, join, repeat
from src.tools.points_around import points_around
from src.tools.points_in_between import points_in_between

def tile_layer(layer_index: int, color):
    if layer_index == 0:
        return [Node(origin, color, 0)]

    distance = (layer_step + layer_padding) * layer_index
    pa = points_around(6, origin, distance, tick_angle + step_angle)

    tiles = []

    hn_prev = hexagonal(layer_index)
    c = 0

    for point_index in range(6):
        current_point = pa[point_index]
        next_point = pa[(point_index + 1) % 6]
        tiles.append(Node(current_point, color, hn_prev + c))
        c += 1
        for p in points_in_between(current_point, next_point, layer_index - 1):
            tiles.append(Node(p, color, hn_prev + c))
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

origin = Point(0, 0)

tile_radius = 5
layer_step = tile_radius * sqrt(3)
layer_padding = 0

radial_unit = 12
tick_angle = tau / radial_unit
step_angle = tau * 2 / radial_unit

sort_order = ["0", "1", "2", "3", "4", "5"]
rotation_order = ["2", "3", "4", "5", "0", "1"]

def long_path_to(index):
    n = int(hexagonal_inverse(index))
    remainder = index - hexagonal(n)
    base = repeat("0", n)
    if remainder == 0:
        return base
    rest = ""
    count = 0
    for c in rotation_order:
        for i in range(n):
            rest += c
            count += 1
            if count == remainder:
                return base + rest

class Equivalence:
    def __init__(self, long: str, short: str):
        self.long = long
        self.short = short

    def get_eqs(self):
        return self.long[0:1], self.long[1:2]

equivalences = [
    # 2 -> 0
    Equivalence("03", ""),
    Equivalence("25", ""),
    Equivalence("41", ""),

    # 2 -> 1
    Equivalence("02", "1"),
    Equivalence("04", "5"),
    Equivalence("35", "4"),
    Equivalence("31", "2"),
    Equivalence("51", "0"),
    Equivalence("24", "3"),
]

def key(word):
    return sort_order.index(word)

def reduce(path_string: str):
    cs = split(path_string)
    cs.sort(key=key)
    path_string = join(cs)
    for e in equivalences:
        e1, e2 = e.get_eqs()
        if e1 in path_string and e2 in path_string:
            return reduce(path_string.replace(e1, "", 1).replace(e2, "", 1) + e.short)

    return path_string

def get_tile_by_path(path, all_tiles):
    for tile in all_tiles:
        if tile.path_index == path:
            tile.visited = True
            return tile

def get_line(path_index_1, path_index_2, all_tiles, color = "nothing"):
    tile1 = get_tile_by_path(path_index_1, all_tiles)
    tile12 = get_tile_by_path(path_index_2, all_tiles)
    if color != "nothing":
        tile1.color = color
        tile12.color = color
    return Line(tile1.center, tile12.center)

def get_path_between(start_index: str, path_index: str, all_tiles):
    steps = []
    diff = reduce(inverse(start_index) + path_index)
    for d in range(len(diff)):
        steps.append(get_line(reduce(start_index + diff[:d]), reduce(start_index + diff[:d + 1]), all_tiles))
    return steps

def inverse(path_str: str):
    inv = ""
    for c in path_str:
        if c == '0':
            inv += '3'
        if c == '3':
            inv += '0'
        if c == '4':
            inv += '1'
        if c == '1':
            inv += '4'
        if c == '5':
            inv += '2'
        if c == '2':
            inv += '5'

    return inv

def rotate(path_str: str, count=1):
    if count == 0: return path_str
    rot = ""
    for c in path_str:
        if c == '0':
            rot += '1'
        if c == '1':
            rot += '2'
        if c == '2':
            rot += '3'
        if c == '3':
            rot += '4'
        if c == '4':
            rot += '5'
        if c == '5':
            rot += '0'

    return rotate(rot, count - 1)

def hexagonal_madness(window):
    layers = 15
    all_tiles = []
    for li in range(layers):
        all_tiles.extend(tile_layer(li, cf(li, layers)))

    lines = []

    for t in all_tiles:
        n = int(hexagonal_inverse(t.index))
        long_path = long_path_to(t.index)
        t.path_index = reduce(long_path)
        t.color = cf(n, layers)
        lines.extend(get_path_between("", t.path_index, all_tiles))

    for line in lines:
        line.setFill(color_rgb(100, 100, 100))
        line.setWidth(3)
        # line.draw(window)

    path_seeds = ["001122", "0011005544",  "0011005544", "00110011222233", "001100110055554444", "0011001100112222223333", "00110011001100555555444444"]
    paths = []

    for path_seed in path_seeds:
        for rotations in range(6):
            rotated_path = rotate(path_seed, rotations)
            for target in range(0, len(rotated_path)):
                infection_color = "nothing"
                if rotations % 2 == 0: infection_color = color_rgb(30, 45, 60)
                p = get_line(reduce(rotated_path[:target]), reduce(rotated_path[:target + 1]), all_tiles, infection_color)
                p.setFill(color_rgb(0, 0, 0))
                p.setWidth(7)
                paths.append(p)

    for path in paths:
        path.draw(window)

    # for i in range(1, 7):
    #     all_tiles[i].color = all_tiles[6].color

    all_tiles[0].color = color_rgb(250, 245, 255)

    for t in all_tiles:
        if t.visited:
            t.get_tile(6, tile_radius).draw(window)
            # t.get_label().draw(window)
