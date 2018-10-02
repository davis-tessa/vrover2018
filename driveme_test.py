##Using Python 2.7.3

import RPi.GPIO as gpio
import time
import sys
import driveme

##Driveme.py Test Code:

##Define the time to drive for (tf)
tf = 3

#drive vechicle forward for tf
driveme.forward(tf)
#turn vehicle left while moving forward for tf seconds
driveme.reverse(tf)
#turn vehicle left while moving forward for tf seconds
driveme.turn_left_fwd(tf)
#turn vehicle right while moving forward for tf seconds
driveme.turn_right_fwd(tf)
#turn vehicle left while reversing for tf seconds
driveme.turn_left_rev(tf)
#turn vehicle right while reversing for tf seconds
driveme.turn_right_rev(tf)
#Pivot vehicle clockwise (right) for tf seconds
driveme.pivot_right(tf)
#Pivot vehicle counterclockwise (left) while moving forward for tf seconds
driveme.pivot_left(tf)
