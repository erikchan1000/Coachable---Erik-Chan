class Point:
  # Initializes 2D point with x,y coordinate/
  def __init__(self, x: float, y: float):
    self.x = x
    self.y = y
    
  # Built in comparator sorting Points by y-coordinate first and using x-coordinate for ties.
  def __cmp__(self, other: Point) -> bool:
    if self.y == other.y:
        return self if self.x < other.x else other

    else:
        return self if self.y< other.y else other

  # Calculates the slope between this point and other point.
  # Computed as (y1 - y0) / (x1 - x0)
  # Horizontal lines have 0 slope.
  # Veritcal lines have infinity slope.
  # If self == other, then return negative infinity.
  def slope_to(self, other: Point) -> float:
    if self == other:
        return float("-inf")
    
    elif self.x - other.x == 0:
        return float("inf")

    elif self.y - other.y == 0:
        return 0

    else:
        return (other.y - self.y) / (other.x - self.x)

class CollinearPointFinder:
  # Takes in a list of points and creates the CollinearPointFinder
  # This method should have O(N^2 log N) runtime.
  # Hint: This method will be the majority of the logic in your code
  # It will include a lot of preprocessing to make the other methods very quick.
  def __init__(self, points: List[Point]):
    
  
  # Returns the number of points in CollinearPointFinder
  # The runtime should be O(1)
  def size(self) -> int:
    
  # Returns the number of collinear segments with at least length k.
  # The runtime should be O(1)
  def num_segments(self, k: int) -> int:
  
  # Returns a list of all collinear segments with at least length k.
  # The runtime should be O(1)
  def get_segments(self, k: int) -> int: