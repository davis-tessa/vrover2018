##Using Python 2.7.3

#import RPi.GPIO as gpio
import time
import sys
import driveme_tank

##driveme_tank.py Test Code:

##Define the time to drive for (tf)
tf = 3
ts = 3

#drive vechicle forward for tf
driveme_tank.forward(tf)
print("sleeping")
time.sleep(ts)

#turn vehicle left while moving forward for tf seconds
driveme_tank.reverse(tf)
print("sleeping")
time.sleep(ts)

#turn vehicle left while moving forward for tf seconds
driveme_tank.turn_left_fwd(tf)
print("sleeping")
time.sleep(ts)

#turn vehicle right while moving forward for tf seconds
driveme_tank.turn_right_fwd(tf)
print("sleeping")
time.sleep(ts)

#turn vehicle left while reversing for tf seconds
driveme_tank.turn_left_rev(tf)
print("sleeping")
time.sleep(ts)

#turn vehicle right while reversing for tf seconds
driveme_tank.turn_right_rev(tf)
print("sleeping")
time.sleep(ts)

#Pivot vehicle clockwise (right) for tf seconds
driveme_tank.pivot_right(tf)
print("sleeping")
time.sleep(ts)

#Pivot vehicle counterclockwise (left) while moving forward for tf seconds
driveme_tank.pivot_left(tf)
print("sleeping")
time.sleep(ts)
