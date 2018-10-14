##Using Python 3.6.5

##Import the local sensors library
import sensors

##Test: Test that the pan_check_distance function works by returning the contents of the dictionary created in the function

print("\n\nStarting Test: sensors_test5\n\n")
distance_table = sensors.pan_check_distance()
print("distance table is", distance_table)
print("front distance", distance_table['front'])
front_dist = distance_table['front']
print("left distance", distance_table['left'])
left_dist = distance_table['left']
print("right distance", distance_table['right'])
right_dist = distance_table['right']
##Troubleshooting:
