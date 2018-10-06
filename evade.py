##Using Python 2.7.3

##Import public library python-RPi.GPIO
#import RPi.GPIO as gpio
##Import public library python-time
import time
##Import public library python-sys
import sys
##Import local library python-sensors: see sensors.py
import sensors
##Import local library python-driveme_tank: see driveme_tank.py
import driveme_tank
##Import public library python-random
import random
##Import local library optimal_direction: see optimal_direction.py
import optimal_direction

##Define the first order action to take when evading a forward obstacle
def evade_fwd_1(tf):
    print("Performing 1st order evasive manouver")
    ##Bring the return of the function optimal_direction in from optimal_direction.py
    opt_dir = optimal_direction.optimal_direction()
    ##First, reverse
    driveme_tank.reverse(tf)
    ##If the optimal direction is left, drive forward and left
    if opt_dir == 'left':
        driveme_tank.turn_left_fwd(tf)
    ##If the optimal direction is right, drive forward and right
    elif opt_dir == 'right':
        driveme_tank.turn_right_fwd(tf)
    ##If the optimal direction is reverse, continue to reverse
    elif opt_dir == 'reverse':
        driveme_tank.reverse(tf)
    ##Results should be only 'left', 'right', or 'reverse'. If not, see optimal_direction.py
    else:
        print("Unexpected result from optimal_direction.py")

def evade_fwd_2(tf):
    print("Help! I'm evade_fwd_2 and I'm a function without definition: define me!")

def evade_fwd_3(tf):
    print("Help! I'm evade_fwd_3 and I'm a function without definition: define me!")

def evade_fwd_4(tf):
    print("Help! I'm evade_fwd_4 and I'm a function without definition: define me!")

def stuck_get_help():
    print("Help! I'm stuck_get_help and I'm a function without definition: define me!")
