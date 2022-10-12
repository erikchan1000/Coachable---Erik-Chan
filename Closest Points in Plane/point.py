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