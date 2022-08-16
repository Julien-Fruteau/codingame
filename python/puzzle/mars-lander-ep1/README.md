## SUMMARY

Exercise has been made using physics. Hence gathering "so called" instruments metrics, predictions can be made to both mitigate fuel consumption and ensure landing speed is as close as possible to vertical speed 0 m/s

The landing process being devided in 3 stages :

- Stage 1 : starting at an initial speed (of 0 m/s), forecast the minimum altitude going full thrust at each compute iteration (being 1sec)
- Stage 2 : powering to full thrust
- Stage 3 : adjusting power between max thrust and max thrust - 1 to ensure landing as close as possible to vertical speed = 0 m/s

## GAME RULES

### INPUT for one game turn

A single line with 7 integers: X Y hSpeed vSpeed fuel rotate thrust

### OUTPUT

- 2 ≤ surfaceN < 30
- 0 ≤ X < 7000
- 0 ≤ Y < 3000
- -500 < hSpeed, vSpeed < 500
- 0 ≤ fuel ≤ 2000
- -90 ≤ rotate ≤ 90  (+/- 15 beetween each time)
0 ≤ thrust ≤ 4      (+/- 1  beetween each time)
Response time per turn ≤ 100ms

### Landing conditions to be successful :

- land on flat ground
- land in a vertical position(tilt angle=0°)
- vertical speed must be limited(≤ 40m/s in absolute valExpect)
- horizontal speed must be limited(≤ 20m/s in absolute valExpect)

**NB** : 
- game time is every second,
- h_speed: the horizontal speed (in m/s), can be negative.
- v_speed: the vertical speed (in m/s), can be negative.
- h_speed < 0: moves right
- fuel: the quantity of remaining fuel in lcounts.
- rotate: the rotation angle in degrees (-90 to 90).
-15 tilt clockwise, with thrust will move right and vice versa
thrust: the thrust thrust (0 to 4) in m/s-2
 consumes 0 to 4 lcounts of fuel