from graphics import Line

def vector(p1, p2):
    v = Line(p1, p2)
    v.setWidth(3)
    v.setArrow("last")
    return v