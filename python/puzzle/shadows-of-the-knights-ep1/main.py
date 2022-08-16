import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
batman = [int(i) for i in input().split()]
xRange = [0, w]
yRange = [0, h]

print("xRange : %s" % xRange, file=sys.stderr)
print("yRange : %s" % yRange, file=sys.stderr)
print("Init Bat : %s" % batman, file=sys.stderr)

# game loop
while True:
    # the direction of the bombs from batman's current location
    # (U, UR, R, DR, D, DL, L or UL)
    bomb_dir = input()
    print("bomb_dir : %s" % bomb_dir, file=sys.stderr)
    for direction in bomb_dir:
        if direction == "U":
            yRange[1] = batman[1] - 1
        elif direction == "D":
            yRange[0] = batman[1] + 1
        elif direction == "R":
            xRange[0] = batman[0] + 1
        elif direction == "L":
            xRange[1] = batman[0] - 1

    batman = [math.floor(sum(xRange) / 2), math.floor(sum(yRange) / 2)]

    print("xRange : %s" % xRange, file=sys.stderr)
    print("yRange : %s" % yRange, file=sys.stderr)
    print("New Bat : %s" % batman, file=sys.stderr)

    # the location of the next window Batman should jump to.
    print("{} {}".format(str(batman[0]), batman[1]))
