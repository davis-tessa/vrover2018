##Using Python 2.7.3

##Import public library python-RPi.GPIO
import RPi.GPIO as gpio
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
##Import local library evade
import evade

## Test: Test base level evade logic - change x to lowest level evade_fwd_x used in script
print("\n\nStarting Test: evade_fwd_test6\n\n")
evade.evade_fwd_1(1, 1)
