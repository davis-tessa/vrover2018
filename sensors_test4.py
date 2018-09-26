##Using Python 2.7.3

##Import the GPIO library
import RPi.GPIO as gpio
##Import the time library
import time
##Import the local sensors library
import sensors

##Test 4: check that distance measurements take place between servo rotations
##Expected result: Servo motor moves to center, prints:
##<Watch me position center, take distance.
##Distance at front:
##Front Sensor Distance Measurement in Progress
#xx.xx cm>
##Servo motor moves to left, prints:
##<Watch me position left, take distance.
##Distance to left:
##Front Sensor Distance Measurement in Progress
#xx.xx cm>
##Servo motor moves to right, prints:
##<Watch me position right, take distance.
##Distance at right:
##Front Sensor Distance Measurement in Progress
#xx.xx cm>
##Servo motor moves to center, prints:
##<Watch me position center, take distance.
##Distance at front:
##Front Sensor Distance Measurement in Progress
#xx.xx cm>
sensors.pan_check_distance_1()

##Troubleshooting:
