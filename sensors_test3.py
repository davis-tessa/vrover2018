##Using Python 3.6.5

##Import the local sensors library
import sensors

##Test: check that the servo motor is correctly wired and functional
##Expected result: Servo motor moves to center, left ~30 degrees, right ~30 degrees, back to center
print("\n\nStarting Test: sensors_test3\n\n")
sensors.front_pan()

##Troubleshooting:
