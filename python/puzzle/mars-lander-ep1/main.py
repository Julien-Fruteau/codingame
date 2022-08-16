import sys
import math

# ================== INIT VARIABLES

thrust_min = 0
thrust_max = 4
gMars = -3.711

thrust = 0
rotate = 0
land_X1 = land_X2 = 0
land_Y = 0
previous_land_x = previous_land_y = 0
landerY0 = 0
landerV0 = 0

t0 = 0
time = 0
stage = "STAGE_1"


# ================== FUNCTION DEFINITION


def Ay(thrust=0):
    return thrust + gMars


def Vy(t, thrust=0, v0=0):
    return Ay(thrust)*t + v0


def Y(t, thrust=0, y0=0, v0=0):
    return Ay(thrust)*(t ** 2)/2 + v0 * t + y0


def Ymin(thrust=0, y0=0, v0=0):
    """return the minimum value of the function Y for Vy(t) = 0
    """
    return -v0 ** 2 / (2 * (thrust + gMars)) + y0


# ! below function only valid if t0 <= t <= t0 + 4
# used to simulate going from 0 to full thrust as :
#  power(t) = t - t0 for t0 <= t <= t0 + 4
def AyInitLand(t, t0):
    return t - t0 + gMars


def VyInitLand(t, t0, v0):
    return ((t - t0) ** 2)/2 + gMars * t + v0


def YInitLand(t, t0, y0, v0):
    return ((t - t0) ** 3)/6 + (gMars * (t ** 2))/2 + v0 * t + y0


def controlDisplay(time, thrust=0, y0=0, v0=0):
    print("Phys Vs Instrum Control > diff [speed : {}, alti : {}]".format(
        str(v_speed - Vy(time, thrust, v0)),
        str(y - Y(time, thrust, y0, v0))
    ), file=sys.stderr)


def power_up(thrust, consigne=thrust_max):
    if thrust < consigne:
        thrust += 1
    return thrust


def power_down(thrust, consigne=thrust_min):
    if thrust > consigne:
        thrust -= 1
    return thrust


# ================== INIT

surface_n = int(input())
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point.
    #  By linking all the points together in a sequential fashion,
    #  you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

    # found the plane landinf surface ? :
    if land_y == previous_land_y:
        land_X1 = previous_land_x
        land_X2 = land_x
        land_Y = land_y

    previous_land_y = land_y
    previous_land_x = land_x

print("{}:{}, {}".format(land_X1, land_X2, land_Y), file=sys.stderr)


# ================== MAIN

while True:
    x, y, h_speed, v_speed, fuel, rotate, thrust = [
        int(i) for i in input().split()]

    if time == 0:
        landerY0 = y
        landerV0 = v_speed
        print("landerY0={} / landerV0={}".format(landerY0, landerV0),
              file=sys.stderr)

    if stage == "STAGE_1":
        print("%s: forecasting minimum altitude going full thrust now" % stage,
              file=sys.stderr)
        landYsup = Ymin(thrust=thrust_max,
                        y0=YInitLand(time + 4, time, landerY0, landerV0),
                        v0=VyInitLand(time + 4, time, landerV0))
        landYinf = Ymin(thrust=thrust_max,
                        y0=YInitLand(time + 5, time + 1, landerY0, landerV0),
                        v0=VyInitLand(time + 5, time + 1, landerV0))

        print("landYinf={} - land_Y={} - lanYsup={}".format(
              landYinf, land_Y, landYsup), file=sys.stderr)
        if (landYinf <= land_Y <= landYsup):
            stage = "STAGE_2"

    if stage == "STAGE_2":
        print("%s: powering up to full thrust [%s/%s]" % (
            stage, str(thrust), str(thrust_max)), file=sys.stderr)
        if thrust < thrust_max:
            thrust = power_up(thrust)
        else:
            landerV0 = v_speed
            landerY0 = y
            stage = "STAGE_3"

    if stage == "STAGE_3":
        print("%s: adjusting power till landing" % stage,
              file=sys.stderr)

        if thrust == thrust_max:
            print("current Ymin_forecast={}".format(
                Ymin(thrust, y0=landerY0, v0=landerV0)
            ), file=sys.stderr)

            print("forecasting min altitude for thrust=3 for :",
                  file=sys.stderr)

            endTimePowerDown = time
            t = 1
            while True:
                landYsup = Ymin(
                    thrust=thrust_max,
                    y0=Y(t, thrust=3, y0=landerY0, v0=landerV0),
                    v0=Vy(t, thrust=3, v0=landerV0)
                )
                landYinf = Ymin(
                    thrust=thrust_max,
                    y0=Y(t + 1, thrust=3, y0=landerY0, v0=landerV0),
                    v0=Vy(t + 1, thrust=3, v0=landerV0)
                )
                print(
                    "> {} sec : landYinf={} - land_Y={} - lanYsup={}".format(
                        t, landYinf, land_Y, landYsup),
                    file=sys.stderr
                )
                if landYsup <= land_Y:
                    break
                elif (landYinf <= land_Y <= landYsup):
                    endTimePowerDown = time + t
                    break

                t += 1

        if time < endTimePowerDown:
            print(">> going at thrust=3 for : {} sec".format(
                endTimePowerDown - time
            ), file=sys.stderr)
            thrust = power_down(thrust, consigne=3)
        else:
            print(">> going full thrust", file=sys.stderr)
            thrust = power_up(thrust, consigne=thrust_max)
            landerV0 = v_speed
            landerY0 = y

    print("0 " + str(thrust))
    time += 1
