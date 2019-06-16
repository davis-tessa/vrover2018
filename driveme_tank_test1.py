##Using Python 3.6.5
import time
import sys
import driveme_tank

##driveme_tank.py Test Code:

##Define the time to drive for (tf)
tf = 3
##Define the time to sleep for (ts)
ts = 1

mode = 'left'

#drive vechicle forward for tf
driveme_tank.forward(tf, mode)
print("driveme_tank_test  > sleeping")
time.sleep(ts)

#turn vehicle left while moving forward for tf seconds
driveme_tank.reverse(tf, mode)
print("driveme_tank_test  > sleeping")
time.sleep(ts)

#turn vehicle left while moving forward for tf seconds
driveme_tank.turn_left_fwd(tf, mode)
print("driveme_tank_test  > sleeping")
time.sleep(ts)

#turn vehicle right while moving forward for tf seconds
driveme_tank.turn_right_fwd(tf, mode)
print("driveme_tank_test  > sleeping")
time.sleep(ts)

#turn vehicle left while reversing for tf seconds
driveme_tank.turn_left_rev(tf, mode)
print("driveme_tank_test  > sleeping")
time.sleep(ts)

#turn vehicle right while reversing for tf seconds
driveme_tank.turn_right_rev(tf, mode)
print("driveme_tank_test  > sleeping")
time.sleep(ts)

#turn vehicle left while reversing for tf seconds
driveme_tank.pivot_left(tf, mode)
print("driveme_tank_test  > sleeping")
time.sleep(ts)

#turn vehicle right while reversing for tf seconds
driveme_tank.pivot_right(tf, mode)
print("driveme_tank_test  > sleeping")
time.sleep(ts)
