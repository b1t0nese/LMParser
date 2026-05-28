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
    
    def __repr__(self):
        attrs = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        attr_str = ', '.join(v.__repr__() for k, v in attrs.items())
        return f"{self.__class__.__name__}({attr_str})"