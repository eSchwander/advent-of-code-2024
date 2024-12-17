class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other_coord):
        return Coord(self.x + other_coord.x, self.y + other_coord.y)

    def subtract(self, other_coord):
        return Coord(self.x - other_coord.x, self.y - other_coord.y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(str(self))
