##Using Python 2.7.3

import RPi.GPIO as gpio
import time
import sys
import driveme_tank

##driveme_tank.py Test Code:

##Define the time to drive for (tf)
tf = 3

#drive vechicle forward for tf
driveme_tank.forward(tf)
print("driving forward")
#turn vehicle left while moving forward for tf seconds
driveme_tank.reverse(tf)
print("driving in reverse")
#turn vehicle left while moving forward for tf seconds
driveme_tank.turn_left_fwd(tf)
print("driving forward and left")
#turn vehicle right while moving forward for tf seconds
driveme_tank.turn_right_fwd(tf)
print("driving forward and right")
#turn vehicle left while reversing for tf seconds
driveme_tank.turn_left_rev(tf)
print("reversing to the left")
#turn vehicle right while reversing for tf seconds
driveme_tank.turn_right_rev(tf)
print("reversing to the right")
#Pivot vehicle clockwise (right) for tf seconds
driveme_tank.pivot_right(tf)
print("pivoting right (clockwise)")
#Pivot vehicle counterclockwise (left) while moving forward for tf seconds
driveme_tank.pivot_left(tf)
print("pivoting left (counter clockwise)")
