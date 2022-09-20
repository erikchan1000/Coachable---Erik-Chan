# 2D point in the plane with x,y coordinate.
class Point:
  # Initializes point with x,y coordinates.
  def __init__(self, x, y):
    self.y = y
    self.x = x
  
  # Returns the squared Euclidean distance between self and other point.
  # (x1 - x2)^2 + (y1 - y2)^2
  def distance_to(self, other):
    return (self.x - other.x)**2 + (self.y - other.y)**2
  
  # Comparator function that will sort by x coordinate first and
  # then by y coordinate as a tiebreaker.
  def __cmp__(self, other):
    if self.x == other.x:
      return self.y - other.y
    return self.x - other.x
# Represents a set of points and the closest ones.
class NearestPointSet:
  # Initializes an empty set of points.
  def __init__(self):
    self.points = []
    self.closest = []
    self.closest_distance = float('inf')
    self.closest_points = [None, None]

  # Returns the size of the NearestPointSet
  # Runtime should be O(1)
  def size(self):
    return len(self.points)
  # Inserts a Point p into the NearestPointSet
  # Runtime should be O(log n)
  def insert(self, p: Point):
    self.points.append(p)
    self.points.sort(key = lambda x : (x.x, x.y))

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



  def find_closest(self):
    self.divide(0, len(self.points) - 1)

    return (self.closest_points[0].x, self.closest_points[0].y), (self.closest_points[1].x, self.closest_points[1].y), self.closest_distance

if __name__ == "__main__":
  myClass = NearestPointSet()

  
 

  print(myClass.find_closest())

  for x in myClass.points:
    print(x.x, x.y)

  