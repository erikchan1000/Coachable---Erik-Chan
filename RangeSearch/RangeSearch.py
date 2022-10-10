import math

class Node:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def x(self):
        return self.x
    
    def y(self):
        return self.y

    def distanceSquaredTo(self, other) -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 2

    def __lt__(self, other):
        if self.x() == other.x():
            return self.y() < other.y()

        else:
            return self.x() < other.x()

    def __gt__(self, other):
        if self.x() == other.x():
            return self.y() > other.y()

        else:
            return self.x() > other.x()

    def __eq__(self, other):
        return self.x() == other.x() and self.y() == other.y()

    def __str__(self):
        return f"{self.x}, {self.y}"

class Rectangle:
    def __init__(self, xmin: float, ymin: float, xmax: float, ymax: float):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def xmin(self) -> float:
        return self.xmin

    def ymin(self) -> float:
        return self.ymin

    def xmax(self) -> float:
        return self.xmax

    def ymax(self) -> float:
        return self.ymax

    def contains(self, p: Point) -> bool:
        return p.x() >= self.xmin and p.x() <= self.xmax and p.y() >= self.ymin and p.y() <= self.ymax

    def intersects(self, other) -> bool:
        if (self.xmax > other.xmin and self.xmax < other.xmax) or (self.xmin > other.xmin and self.xmin < other.xmin):
            if (self.ymax > other.ymin and self.ymax < other.ymax) or (self.ymin > other.ymin and self.ymin < other.ymax):
                return True

        return False

    def pointIntersects(self, point) -> bool:
        return point.x() >= self.xmin and point.x() <= self.xmax and point.y() >= self.ymin and point.y() <= self.ymax


    #1. Bisect (check both branch)
    #2. > right 
    #3. < left

class TwoDimensionalTree:
    def __init__(self):
        self.points = set()
        self.head = None

    def is_empty(self):
        return len(self.points) == 0

    def size(self):
        return len(self.points)

    def insert(self, p: Point):
        myNode = Node(p)
        self.points.add(p)

        if not self.head:
            self.head = myNode

        self.dfsInsert(self.head, myNode)

    def dfsInsert(self, curr: Node, node, level = 1):
        if curr is None:
            return node

        if level % 2 == 1:
            if node.point.x() < curr.point.x():
                curr.left = self.dfsInsert(curr.left, node, level + 1)

            else:
                curr.right = self.dfsInsert(curr.right, node, level + 1)
        else:
            if node.point.y() < curr.point.y():
                curr.left = self.dfsInsert(curr.left, node, level + 1)

            else:
                curr.right = self.dfsInsert(curr.right, node, level + 1)

        return curr

    def contains(self, p):
        return True if p in self.points else False

    def nearestNeighborSearch(self, p: Point):
        res = []
        self.dfsNearestNeighborSearch(self.head, p, res)
        return res

    def dfsNearestNeighborSearch(self, curr: Node, p: Point, res):
        if not curr:
            return

        if not res:
            res.append(curr.point)

        elif p.distanceSquaredTo(curr.point) < p.distanceSquaredTo(res[0]):
            res[0] = curr.point

        else:
            return

        self.dfsNearestNeighborSearch(curr.left, p, res)
        self.dfsNearestNeighborSearch(curr.right, p, res)

    def rangeSearch(self, rectangle: Rectangle):
        res = []
        self.dfsRangeSearch(self.head, rectangle, res)
        return res

    def dfsRangeSearch(self, curr: Node, rectangle: Rectangle, res, isX = True):
        if not curr:
            return

        if rectangle.contains(curr.point):
            res.append(curr.point)

        if isX:
            if curr.point.x() > rectangle.xmin:
                self.dfsRangeSearch(curr.left, rectangle, res, False)

            if curr.point.x() < rectangle.xmax:
                self.dfsRangeSearch(curr.right, rectangle, res, False)

        else:
            if curr.point.y() > rectangle.ymin:
                self.dfsRangeSearch(curr.left, rectangle, res, True)

            if curr.point.y() < rectangle.ymax:
                self.dfsRangeSearch(curr.right, rectangle, res, True)

