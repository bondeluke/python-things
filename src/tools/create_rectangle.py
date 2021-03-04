from src.graphics import Rectangle, Point

def create_rectangle(center_point, width_radius, height_radius, color):
    bottom_left = Point(center_point.x - width_radius, center_point.y - height_radius)
    top_right = Point(center_point.x + width_radius, center_point.y + height_radius)
    rect = Rectangle(bottom_left, top_right)
    rect.setFill(color)
    return rect

def get_corners(rect):
    return [rect.p1, Point(rect.p1.x, rect.p2.y), rect.p2, Point(rect.p2.x, rect.p1.y)]

def get_corners_from_many(rectangles):
    corners = []
    for rect in rectangles:
        corners.extend(get_corners(rect))
    return corners

def get_center(rect):
    half_x = (rect.p2.x - rect.p1.x) / 2
    half_y = (rect.p2.y - rect.p1.y) / 2
    return Point(rect.p1.x + half_x, rect.p1.y + half_y)
