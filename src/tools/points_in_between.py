from src.graphics import Point

def points_in_between(p1, p2, how_many):
    points = []
    dx = (p2.x - p1.x)
    dy = (p2.y - p1.y)
    step_x = dx / (how_many + 1)
    step_y = dy / (how_many + 1)
    for index_from_p1 in range(1, how_many + 1):
        points.append(Point(p1.x + step_x * index_from_p1, p1.y + step_y * index_from_p1))

    return points