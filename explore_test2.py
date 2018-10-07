##Using Python 2.7.3

##Import public library python-RPi.GPIO
#import RPi.GPIO as gpio
##Import public library python-time
import time
##Import public library python-sys
import sys
##Import local library python-sensors: see sensors.py
import sensors
##Import local library python-driveme: see driveme.py
import driveme_tank
##Import public library python-random
import random
##Import local library explore
import explore

##Test: Add sensor check collision_avoidance() to the test
##Input: explore.mode_discovery(x, y, z, u)
##x is the time that left or right forward drive will run for assuming no obstacles
##y is the time that the vehicle should run for before checking input from the sensor
##z is the bias 'left' or 'right'
##u is the check status 'on' or 'off'

##How to set up tests that are possible without hardware:
##Pre-set the dictionary values for various scenarios... sensors are in development mode_discovery
##Advanced: Build a map to test the edge and corner cases

print("\n\nStarting Test: explore_test2\n\n")

for z in range(1):
    explore.mode_discovery(1, 1, 'left', 'on')

for z in range(1):
    explore.mode_discovery(1, 1, 'right', 'on')
