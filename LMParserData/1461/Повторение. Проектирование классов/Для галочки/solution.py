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

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.name, self.x, self.y) < (other.name, other.x, other.y)

    def __gt__(self, other):
        return (self.name, self.x, self.y) > (other.name, other.x, other.y)

    def __le__(self, other):
        return (self.name, self.x, self.y) <= (other.name, other.x, other.y)

    def __ge__(self, other):
        return (self.name, self.x, self.y) >= (other.name, other.x, other.y)

    def __str__(self):
        return f"{self.name}{(self.x, self.y)}"

    def __repr__(self):
        attrs = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        attr_str = ", ".join(v.__repr__() for k, v in attrs.items())
        return f"{self.__class__.__name__}({attr_str})"


class CheckMark:
    def __init__(self, p1, p2, p3):
        self.p1, self.p2, self.p3 = p1, p2, p3

    def __str__(self):
        return "".join([p.name for p in [self.p1, self.p2, self.p3]])

    def __bool__(self):
        return (self.p2.x - self.p1.x) * (self.p3.y - self.p1.y) != \
            (self.p3.x - self.p1.x) * (self.p2.y - self.p1.y)

    def __eq__(self, other):
        if self.p2 != other.p2:
            return False
        else:
            return (self.p1 == other.p1 and self.p3 == other.p3) or \
                (self.p1 == other.p3 and self.p3 == other.p1)