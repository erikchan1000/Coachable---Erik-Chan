from point import Point

# Represents a set of points and the closest ones.
class NearestPointSet:
  # Initializes an empty set of points.
  def __init__(self):
    self.points = []
    self.closest = []
    self.closest_distance = float('inf')
    self.closest_points = [None, None]
    self._size = 0

  # Returns the size of the NearestPointSet
  # Runtime should be O(1)
  def size(self):
    return self._size
  # Inserts a Point p into the NearestPointSet
  # Runtime should be O(log n)
  def insert(self, p: Point):
    if p not in self.points:
      self.points.append(p)
      self._size += 1

  # Returns the 2 closest points as well as the distance between them.
  # Output is in format (p1, p2, distance between p1 and p2)
  # Runtime should be O(n) in the average case

  def divide(self, lo, hi):
    if lo >= hi:
      return

    mid = (lo + hi) // 2

    self.divide(lo, mid)

    self.divide(mid + 1, hi)

    self.merge(lo, mid, hi)

  def merge(self, lo, mid, hi):
    p1 = lo

    p2 = mid + 1

    while p1 <= mid and p2 <= hi:
      if self.points[p1].distance_to(self.points[p2]) < self.closest_distance:
        self.closest_distance = self.points[p1].distance_to(self.points[p2])

        self.closest_points[0] = self.points[p1]

        self.closest_points[1] = self.points[p2]

      if self.points[p1].y < self.points[p2].y:
        p1 += 1
      
      else:
        p2 += 1

  # Returns the 2 closest points as well as the distance between them.
  # Output the distance between the 2 closest points.
  # Runtime should be O(n log n) in the worst case
  def find_closest(self) -> float:

    self.divide(0, len(self.points) - 1)

    return None if self.closest_distance == float('inf') else self.closest_distance

