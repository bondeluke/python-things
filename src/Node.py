from src.graphics import Polygon, Text
from src.tools.points_around import points_around

class Node:
    def __init__(self, center, color, index, path_index=""):
        self.center = center
        self.color = color
        self.index = index
        self.path_index = path_index
        self.visited = False

    def get_tile(self, how_many_points, tile_radius: float):
        polygon = Polygon(points_around(how_many_points, self.center, tile_radius))
        polygon.setWidth(3)
        polygon.setFill(self.color)
        return polygon

    def get_label(self):
        return Text(self.center, "{}\n{}".format(self.index, self.path_index))