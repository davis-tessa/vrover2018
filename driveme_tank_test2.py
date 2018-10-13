##Using Python 3.6.5
import time
import sys
import driveme_tank

##driveme_tank.py Test Code:

##Test the function of the mode indicator LEDs

##Test function of Left mode LED:

driveme_tank.mode_lft_LED()
print("The left mode indicator light should be turned on")

time.sleep(3)

driveme_tank.mode_rt_LED()
print("The right mode indicator light should be turned on")
