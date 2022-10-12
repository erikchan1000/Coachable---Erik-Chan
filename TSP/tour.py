from point import Point


class Node:
    def __init__(self, point: Point) -> None:
        self.point = point
        self.next = None


class Tour:
    def __init__(self) -> None:
        self.head = None
        self.points = []
        self._size = 0

    def __str__(self) -> str:
        curr = self.head
        string = ""

        if curr is None:
            return string

        while curr.next is not None:
            string += str(curr.point) + " -> "
            curr = curr.next
        string += str(curr.point)

        return string

    def size(self) -> int:
        return self._size
    # Computes and returns the distance of entire tour

    def distance(self) -> float:
        curr = self.head
        total = 0
        if curr is None:
            return 0

        while curr.next is not None:
            total += curr.point.distance_to(curr.next.point)
            curr = curr.next

        total += curr.point.distance_to(self.head.point)

        return total

    def _insert_at(self, p: Point, prev: Node) -> None:
        new_node = Node(p)
        if self.head is None:
            self.head = new_node
            self.points.append(p)
            self._size += 1
            return
        new_node.next = prev.next
        prev.next = new_node
        self.points.append(p)
        self._size += 1

    def insert_nearest(self, p: Point) -> None:
        if self.head is None:
            return self._insert_at(p, self.head)

        curr = self.head
        smallest = curr.point.distance_to(p)
        prev = curr
        
        while curr.next is not None:
            if curr.point.distance_to(p) < smallest:
                smallest = curr.point.distance_to(p)
                prev = curr
            curr = curr.next

        if curr.point.distance_to(p) < smallest:
            self._insert_at(p, curr)
        else:
            self._insert_at(p, prev)

    def insert_smallest(self, p: Point) -> None:
        if self.head is None:
            return self._insert_at(p, self.head)

        curr = self.head
        smallest = float("inf")
        prev = curr

        while curr.next is not None:
            distance = (curr.point.distance_to(p) + curr.next.point.distance_to(p)
                - curr.point.distance_to(curr.next.point))
            if  distance < smallest:
                smallest = distance
                prev = curr
            curr = curr.next

        distance = (curr.point.distance_to(p) + self.head.point.distance_to(p)
            - curr.point.distance_to(self.head.point))

        if distance < smallest:
            self._insert_at(p, curr)
        else:
            self._insert_at(p, prev)
