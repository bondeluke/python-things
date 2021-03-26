from src.graphics import Rectangle, Point, Text

class Button:
    def __init__(self, bottom_left: Point, value, width=12, height=6):
        self.bottom_left = bottom_left
        self.left = bottom_left.x
        self.bottom = bottom_left.y
        self.right = self.bottom_left.x + width
        self.top = self.bottom_left.y + height
        self.center = Point(self.left + width / 2, self.bottom + height / 2)
        self.width = width
        self.height = height
        self.value = value

    def draw(self, window):
        rect = Rectangle(self.bottom_left, Point(self.right, self.top))
        rect.draw(window)
        t = Text(self.center, str(self.value))
        t.draw(window)

    def point_within(self, p: Point):
        if self.left <= p.x <= self.right and self.bottom <= p.y <= self.top:
            print("in")
            return True
        print("in")
        return False
