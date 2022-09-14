# 2D point in the plane with x,y coordinate.
class Point:
  # Initializes point with x,y coordinates.
  def __init__(self, x, y):
    self.y = y
    self.x = x
  
  # Returns the squared Euclidean distance between self and other point.
  # (x1 - x2)^2 + (y1 - y2)^2
  def distance_to(self, other):
  
  # Comparator function that will sort by x coordinate first and
  # then by y coordinate as a tiebreaker.
  def __cmp__(self, other):

# Represents a set of points and the closest ones.
class NearestPointSet:
  # Initializes an empty set of points.
  def __init__(self):
    
  # Returns the size of the NearestPointSet
  # Runtime should be O(1)
  def size(self):
    
  # Inserts a Point p into the NearestPointSet
  # Runtime should be O(log n)
  def insert(self, p: Point):
    
  # Returns the 2 closest points as well as the distance between them.
  # Output is in format (p1, p2, distance between p1 and p2)
  # Runtime should be O(n) in the average case
  def find_closest(self):