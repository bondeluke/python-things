from src.graphics import Polygon, Text, color_rgb
from src.tools.points_around import points_around

class Node:
    def __init__(self, center, color, index, path_index=""):
        self.center = center
        self.color = color
        self.index = index
        self.path_index = path_index
        self.visited = False

    def get_tile(self, layers, inverse, how_many_points, tile_radius: float):
        r, g, b = self.getRGB(layers, inverse)
        polygon = Polygon(points_around(how_many_points, self.center, tile_radius))
        polygon.setWidth(3)
        polygon.setFill(color_rgb(r, g, b))
        return polygon

    def getRGB(self, layers, inverse):
        r, g, b = 0, 0, 0
        for c in self._inner_id():
            if c == 'R': r += 1
            if c == 'G': g += 1
            if c == 'B': b += 1
        if inverse:
            return 255 - int(r * 255 / (layers - 1)), 255 - int(g * 255 / (layers - 1)), 255 - int(b * 255 / (layers - 1))
        else:
            return int(r * 255 / (layers - 1)), int(g * 255 / (layers - 1)), int(b * 255 / (layers - 1))


    def _inner_id(self):
            return self.path_index.replace("0", "R").replace("3", "BG").replace("2", "G").replace("5", "RB").replace("4", "B").replace("1", "RG")

    def get_label(self, layers, inverse):
        r, g, b = self.getRGB(layers, inverse)
        return Text(self.center, "{}\n({}, {}, {})\n{}".format(self.index,r, g, b, self._inner_id()))
