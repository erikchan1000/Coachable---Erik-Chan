import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def distance_to(self, that):
        return math.sqrt((self.x - that.x) ** 2 + (self.y - that.y) ** 2)