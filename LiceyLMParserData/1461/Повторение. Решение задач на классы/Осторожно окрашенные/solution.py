class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x, self.y = x, y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y

    def __str__(self):
        return f"{self.name}{(self.x, self.y)}"

    def __invert__(self):
        return Point(self.name, self.y, self.x)


class ColoredPoint(Point):
    def __init__(self, name, x, y, color=(0, 0, 0)):
        super().__init__(name, x, y)
        self.color = color

    def get_color(self):
        return self.color

    def __invert__(self):
        return ColoredPoint(
            self.name,
            self.y,
            self.x,
            (
                abs(self.color[0] - 255),
                abs(self.color[1] - 255),
                abs(self.color[2] - 255),
            ),
        )