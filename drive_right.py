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
##Import local library evade: see evade.py
import evade
##Import local library explore: see explore.py
import explore

def drive_right():
  explore.mode_discovery(1, 1, 'right', 'on')

drive_right()
