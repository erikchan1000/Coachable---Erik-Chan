class Point:
    # Initializes 2D point with x,y coordinate/
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Built in comparator sorting Points by y-coordinate first and using x-coordinate for ties.
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x

        return self.y < other.y

    def slope_to(self, other) -> float:
        if self == other:
            return float("-inf")

        elif self.x == other.x:
            return float("inf")

        elif self.y - other.y == 0:
            return 0

        else:
            return float((other.y - self.y) / (other.x - self.x))
