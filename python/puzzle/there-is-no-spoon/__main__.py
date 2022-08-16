import sys
import math


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []

    def __call__(self, x, y):
        try:
            return self.grid[y][x]
        except IndexError:
            return None

    def Append(self, newList):
        self.grid.append(newList)

    def IterCoor(self, axis=0):
        for row in range(self.height):
            for col in range(self.width):
                yield (col, row)

    def NextLowerNeighboor(self, x, y):
        y += 1
        while y < self.height:
            if grid(x, y) == '0':
                return (x, y)
            y += 1
        return None

    def NextRightNeighboor(self, x, y):
        x += 1
        while x < self.width:
            if grid(x, y) == '0':
                return (x, y)
            x += 1
        return None


width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
# initiliaze grid
grid = Grid(width, height)

for i in range(height):
    line = input()  # width characters, each either 0 or .
    print("line :" + line, file=sys.stderr)
    grid.Append([c for c in line])

for (x, y) in grid.IterCoor():
    # print(x, y, grid(x, y), file = sys.stderr)
    if grid(x, y) == "0":
        line = "{} {}".format(x, y)
    else:
        continue
    if grid.NextRightNeighboor(x, y):
        line += " {} {}".format(*grid.NextRightNeighboor(x, y))
    else:
        line += " -1 -1"
    if grid.NextLowerNeighboor(x, y):
        line += " {} {}".format(*grid.NextLowerNeighboor(x, y))
    else:
        line += " -1 -1"
    print(line)
