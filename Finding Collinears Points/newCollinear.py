from collections import defaultdict
from point import Point

class CollinearPointFinder:
  # Takes in a list of points and creates the CollinearPointFinder
  # This method should have O(N^2 log N) runtime.
  # Hint: This method will be the majority of the logic in your code
  # It will include a lot of preprocessing to make the other methods very quick.
  def __init__(self, points: list):
    self.points = points
    self.hmap = defaultdict(list)
    visitedSlopes = set()
  
    p = 0

    while p < len(self.points):
      
      p2 = p + 1
      p3 = p2 + 1
      count = 1
      self.points[p2:] = sorted(self.points[p2:], key=lambda point: point.slope_to(self.points[p]))

      while p3 < len(self.points) and self.points[p].slope_to(self.points[p2]) == self.points[p].slope_to(self.points[p3]):
        if self.points[p].slope_to(self.points[p3]) in visitedSlopes:
          break
        
        count += 1
        p3 += 1

      if count >= 2:
        self.hmap[count + 1].append(self.points[p:p3])
        visitedSlopes.add(self.points[p].slope_to(self.points[p3 - 1]))

      p += 1

    for x in self.hmap:
        for i in self.hmap[x]:
            for z in range(len(i)):
                i[z] = (i[z].x, i[z].y)

    maxValue = max(self.hmap.keys())

    for i in range(maxValue - 1, 2, -1):
      self.hmap[i].extend(self.hmap[i + 1])

  # Returns the number of points in CollinearPointFinder
  # The runtime should be O(1)
  def size(self) -> int:
    return len(self.points)
  # Returns the number of collinear segments with at least length k.
  # The runtime should be O(1)
  def num_segments(self, k: int) -> int:
    if k not in self.hmap:
      return 0
    return len(self.hmap[k])
  
  # Returns a list of all collinear segments with at least length k.
  # The runtime should be O(1)
  def get_segments(self, k: int) -> int:
    if k not in self.hmap:
      return []
    return self.hmap[k]

def main():
  points = [(1000.0, 17000.0), (14000.0, 24000.0), (26000.0, 8000.0), (10000.0, 28000.0), (18000.0, 5000.0), (1000.0, 27000.0), (14000.0, 14000.0), (11000.0, 16000.0), (29000.0, 17000.0), (5000.0, 21000.0), (19000.0, 26000.0), (28000.0, 21000.0), (25000.0, 24000.0), (30000.0, 10000.0), (25000.0, 14000.0), (31000.0, 16000.0), (5000.0, 12000.0), (1000.0, 31000.0), (2000.0, 24000.0), (13000.0, 17000.0), (1000.0, 28000.0), (14000.0, 16000.0), (26000.0, 26000.0), (10000.0, 31000.0), (12000.0, 4000.0), (9000.0, 24000.0), (28000.0, 29000.0), (12000.0, 20000.0), (13000.0, 11000.0), (4000.0, 26000.0), (8000.0, 10000.0), (15000.0, 12000.0), (22000.0, 29000.0), (7000.0, 15000.0), (10000.0, 4000.0), (2000.0, 29000.0), (17000.0, 17000.0), (3000.0, 15000.0), (4000.0, 29000.0), (19000.0, 2000.0)]
  for x in range(len(points)):
    points[x] = Point(points[x][0]/1000, points[x][1]/1000)
  finder = CollinearPointFinder(points)
  print(finder.hmap)

  print(finder.num_segments(3))
  print(finder.get_segments(3))

main()