from point import Point
class Node:
    def __init__(self, point):
        self.point = point
        self.next = None


class Tour:

    def __init__(self):
        self.points = []
        self.head = None
        self._size = 0

    def size(self):
        return self._size

    def __str__(self):
        curr = self.head
        temp = []
        while curr:
            temp.append(f"({curr.point.x},{curr.point.y})")
            curr = curr.next

        return " -> ".join(temp)

    def _insert_at(self, p, prev = None):
        if len(self.points) == 0:
            p = Node(p)
            self.points.append(p)
            self.head = p
            self._size += 1
        
        else:
            curr = self.head
            while curr:
                if curr.point == prev.point:
                    p = Node(p)
                    p.next = curr.next
                    curr.next = p
                    self._size += 1
                    self.points.append(p)
                curr = curr.next

    def insert_nearest(self, p):
        curr = None
        minDistance = float("inf")
        if len(self.points) == 0:
            self._insert_at(p)
        else:
            for x in self.points:
                
                currDistance = x.point.distance_to(p)
                
                if currDistance < minDistance:
                    minDistance = currDistance
                    curr = x
            self._insert_at(p, curr)

    def insert_smallest(self, p):
        curr = self.head
        minDistance = float("inf")
        if len(self.points) == 0:
            self._insert_at(p)

        else:
            for x in self.points:
                currDistance = x.point.distance_to(p)
        
                if currDistance < minDistance:
                    minDistance = currDistance
                    curr = x
            self._insert_at(p, curr)

    def distance(self) -> float:
        curr = self.head
        total = 0

        if not curr:
            return 0

        while curr.next:
            total += curr.point.distance_to(curr.next.point)
            curr = curr.next

        total += curr.point.distance_to(self.head.point)
        return total