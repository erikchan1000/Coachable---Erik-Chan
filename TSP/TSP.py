import math

file = open("tsp2.txt", "r+")

file2 = open("tsp1000.txt", "r+")

lines = file.readlines()

lines2 = file2.readlines()

def setify(input):

    for x in range(len(input)):
        input[x] = input[x].strip("\n")

        input[x] = input[x].split(" ")


        input[x] = list(filter(lambda item : item != "", input[x]))

        for y in range(len(input[x])):
            input[x][y] = float(input[x][y])
setify(lines)

setify(lines2)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distanceTo(self, that):
        return math.sqrt((self.x - that.x) ** 2 + (self.y - that.y) ** 2)

    
class Node:
    def __init__(self, point):
        self.point = point

        self.next = None

        

class Tour:

    #must pass p as point object

    def __init__(self):
        self.points = []
        self.head = None
        self.size = 0

    def __str__(self):
        curr = self.head
        temp = []
        while curr:
            temp.append(f"({curr.point.x}, {curr.point.y})")
            curr = curr.next

        return " -> ".join(temp)

    def _insert_at(self, p , prev = None):
        if len(self.points) == 0:
            p = Node(p)
            self.points.append(p)
            self.head = p
            self.size += 1
        
        else:
            curr = self.head
            while curr:
                if curr.point == prev.point:
                    p = Node(p)
                    p.next = curr.next
                    curr.next = p
                    self.size += 1
                    self.points.append(p)

                curr = curr.next

    def insertNearest(self, p):

        curr = None
        minDistance = float("inf")

        if len(self.points) == 0:
            self._insert_at(p)

        else:
            for x in self.points:
                
                currDistance = x.point.distanceTo(p)
                
                if currDistance < minDistance:
                    minDistance = currDistance
                    curr = x

            self._insert_at(p, curr)

    def insertSmallest(self, p):
        minIncrease = float("inf")

        if len(self.points) == 0:
            self._insert_at(p)
            

        elif len(self.points) == 1:
            self._insert_at(p, self.head)

        else:
            curr = self.head
            insertion = None

            while curr:

                if curr.next is None:
                    currIncrease = curr.point.distanceTo(p)

                else:
                    currIncrease = curr.point.distanceTo(curr.next.point)

                if minIncrease > currIncrease:
                        minIncrease = currIncrease
                        insertion = curr

                curr = curr.next
            
            self._insert_at(p, insertion)

            

myTour = Tour()
myTour2 = Tour()
myPoints = [Point(x[0], x[1]) for x in lines]
myPoints.pop(0)

for x in myPoints:
    myTour.insertNearest(x)
    myTour2.insertSmallest(x)

print(myTour)

print(myTour2)



myPoints2 = [Point(x[0], x[1]) for x in lines2]
myPoints2.pop(0)

tour1000 = Tour()
tour1001 = Tour()

for x in myPoints2:
    tour1000.insertNearest(x)
    tour1001.insertSmallest(x)

print(tour1000)

curr = tour1000.head

temp = 0

while curr.next:
    temp += curr.point.distanceTo(curr.next.point)
    curr = curr.next

print(temp)