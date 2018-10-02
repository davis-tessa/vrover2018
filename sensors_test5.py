##Using Python 2.7.3

##Import the GPIO library
import RPi.GPIO as gpio
##Import the time library
import time
##Import the local sensors library
import sensors

##Test 4: Test that the optimal_direction function works
distance_table = sensors.pan_check_distance()
print("front distance", distance_table['front'])
front_dist = distance_table['front']
print("left distance", distance_table['left'])
left_dist = distance_table['left']
print("right distance", distance_table['right'])
right_dist = distance_table['right']
##Troubleshooting:
