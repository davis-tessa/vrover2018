##Using Python 2.7.3

import RPi.GPIO as gpio
import time
import sys
import driveme_tank

##driveme_tank.py Test Code:

##Define the time to drive for (tf)
tf = 3

#drive vechicle forward for tf
driveme_tank.init()
driveme_tank.forward(tf)
#turn vehicle left while moving forward for tf seconds
driveme_tank.init()
driveme_tank.reverse(tf)
#turn vehicle left while moving forward for tf seconds
driveme_tank.init()
driveme_tank.turn_left_fwd(tf)
#turn vehicle right while moving forward for tf seconds
driveme_tank.init()
driveme_tank.turn_right_fwd(tf)
#turn vehicle left while reversing for tf seconds
driveme_tank.init()
driveme_tank.turn_left_rev(tf)
#turn vehicle right while reversing for tf seconds
driveme_tank.init()
driveme_tank.turn_right_rev(tf)
#Pivot vehicle clockwise (right) for tf seconds
driveme_tank.init()
driveme_tank.pivot_right(tf)
#Pivot vehicle counterclockwise (left) while moving forward for tf seconds
driveme_tank.init()
driveme_tank.pivot_left(tf)
