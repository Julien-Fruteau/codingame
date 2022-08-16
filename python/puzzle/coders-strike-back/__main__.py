import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

has_boost = True
radius_checkpoint = 600
start_decelerate_distance = 1500

# thrust est une fonction variable de la distance au checkpoint de l'angle d'attaque
# thrust diminue lorsque la distance est < à une certaine distance du checkpoint
# thrust
# 100                                  x      x
#                         x
#                    x
#                 x
#               x
# 50
#             x
#
#
#            x
# 0         500          1000        1500                : distance


# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and
    #  the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y,\
        next_checkpoint_dist, next_checkpoint_angle = [
            int(i) for i in input().split()]

    print("distance to next checkpoint = " + str(next_checkpoint_dist),
          file=sys.stderr)

    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    if (next_checkpoint_angle > 90 or next_checkpoint_angle < -90 or
       next_checkpoint_dist < 1500):
        thrust = 0
    elif (has_boost and next_checkpoint_angle == 0 and
          next_checkpoint_dist > 5000):
        thrust = "BOOST"
        has_boost = False
    else:
        thrust = 100

    # To debug: print("Debug messages...", file=sys.stderr)
    # Edit this line to output the target position
    # and thrust (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print('{} {} {}'.format(
        str(next_checkpoint_x),
        str(next_checkpoint_y),
        str(thrust)
    ))

    # Utilisez la commande < x y "BOOST" > au lieu de < x y power > .
