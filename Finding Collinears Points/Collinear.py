from re import L


class Point:
  # Initializes 2D point with x,y coordinate/
  def __init__(self, x: float, y: float):
    self.x = x
    self.y = y
    
  # Built in comparator sorting Points by y-coordinate first and using x-coordinate for ties.
  def __cmp__(self, other) -> bool:
    if self.y == other.y:
        return self if self.x < other.x else other

    else:
        return self if self.y< other.y else other

  # Calculates the slope between this point and other point.
  # Computed as (y1 - y0) / (x1 - x0)
  # Horizontal lines have 0 slope.
  # Veritcal lines have infinity slope.
  # If self == other, then return negative infinity.
  def slope_to(self, other) -> float:
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
  def __init__(self, points: list[Point]):

    self.points = points

    self.hmap = {}
    
    for p in range(len(points)):
        temp = points[:p] + points[p + 1 :]
        
        temp.sort(key = lambda x : points[p].slope_to(x))
        
        p1 = 0

        p2 = 0

        while p1 < len(temp):
            slope = points[p].slope_to(temp[p1])
            if p2 != p1:
                
                slope2 = points[p].slope_to(temp[p2])

                if slope == slope2 and p2 < len(points) - 1:
                    p2 += 1

                else:
                    p1 += 1

            elif p2 < len(temp) - 1:
                p2 += 1

            else: 
                p1 += 1

            if p2 - p1 + 1 not in self.hmap:
                self.hmap[p2 - p1 + 1] = [[points[p]] + temp[p1 : p2]]

            else:
                self.hmap[p2 - p1 + 1].append([points[p]] + temp[p1 : p2])

    for x in self.hmap:
        for i in self.hmap[x]:
            for z in range(len(i)):
                i[z] = (i[z].x, i[z].y)

    for x in self.hmap:
        print(x)

        print(self.hmap[x])


  # Returns the number of points in CollinearPointFinder
  # The runtime should be O(1)
  def size(self) -> int:
    return len(self.points)
  # Returns the number of collinear segments with at least length k.
  # The runtime should be O(1)
  def num_segments(self, k: int) -> int:
    return len(self.hmap[k])
  
  # Returns a list of all collinear segments with at least length k.
  # The runtime should be O(1)
  def get_segments(self, k: int) -> int:
    return self.hmap[k]




points = [(1, 2), (3, 9), (2, 3), (4, 5), (2, 6), (3, 4), (1, 3), (10, 3), (4, 12)]

for x in range(len(points)):
    points[x] = Point(points[x][0], points[x][1])

test = CollinearPointFinder(points)