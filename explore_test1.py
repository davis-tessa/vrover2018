##Using Python 2.7.3

##Import public library python-RPi.GPIO
import RPi.GPIO as gpio
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

##Test 1: check the mode_discovery function works
##Input: explore.mode_discovery(x, y)
##x is the time that left or right forward drive will run for
##y is the bias 'left' or 'right''

##How to set up tests that are possible without hardware:
##Pre-set the dictionary values for various scenarios... sensors are in development mode_discovery
##Advanced: Build a map to test the edge and corner cases


##How to set up tests that are possible without hardware:
##Pre-set the dictionary values for various scenarios... sensors are in development mode_discovery
##Advanced: Build a map to test the edge and corner cases

explore.check_front()

##Troubleshooting:

## Error 1:
## <Traceback (most recent call last):
## File "sensors_test.py", line 22, in <module>
## print sensors.front_distance(), "cm"
## File "/home/pi/vforum2018/sensors.py", line 53, in front_distance
## pulse_duration = pulse_end - pulse_start>
## Cause: Theory: The sensor fails to trigger OR Theory: The sensor triggers before the RPi has a chance to capture the pre-trigger state
## Testing: The error appears randomly only on the front sensor (not on the rear sensor) with a frequency of approximately 1 in 3 attempts. Likely to be a faulty sensor or faulty connection
## Resolution: Replace front sensor for production. OR see comment in sensors.py "Give the sensor time to come online" - increase tf in time.sleep(tf)
