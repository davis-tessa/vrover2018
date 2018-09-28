##Using Python 2.7.3

import RPi.GPIO as gpio
import time
import sys
import driveme_tank

##driveme_tank.py Test Code:

##Define the time to drive for (tf)
tf = 3
ts = 0.5

#drive vechicle forward for tf
driveme_tank.forward(tf)
print("driving forward")
time.sleep(0.5)
print("sleeping")
#turn vehicle left while moving forward for tf seconds
driveme_tank.reverse(tf)
print("driving in reverse")
time.sleep(0.5)
print("sleeping")
#turn vehicle left while moving forward for tf seconds
driveme_tank.turn_left_fwd(tf)
print("driving forward and left")
time.sleep(0.5)
print("sleeping")
#turn vehicle right while moving forward for tf seconds
driveme_tank.turn_right_fwd(tf)
print("driving forward and right")
time.sleep(0.5)
print("sleeping")
#turn vehicle left while reversing for tf seconds
driveme_tank.turn_left_rev(tf)
print("reversing to the left")
time.sleep(0.5)
print("sleeping")
#turn vehicle right while reversing for tf seconds
driveme_tank.turn_right_rev(tf)
print("reversing to the right")
time.sleep(0.5)
print("sleeping")
#Pivot vehicle clockwise (right) for tf seconds
driveme_tank.pivot_right(tf)
print("pivoting right (clockwise)")
time.sleep(0.5)
print("sleeping")
#Pivot vehicle counterclockwise (left) while moving forward for tf seconds
driveme_tank.pivot_left(tf)
print("pivoting left (counter clockwise)")
time.sleep(0.5)
print("sleeping")
