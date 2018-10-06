import time
import sys
import random
import sensors

def optimal_direction():
    ## Return the contents of the distance_table created by running the pan_check_distance function
    distance_table = sensors.pan_check_distance()
    print("front distance", distance_table['front'])
    front_dist = distance_table['front']
    print("left distance", distance_table['left'])
    left_dist = distance_table['left']
    print("right distance", distance_table['right'])
    right_dist = distance_table['right']

    ## If there are obstacles on both sides of the vehicle, the optimal direction is 'reverse'
    if left_dist < 20 and right_dist < 20:
        optimal_direction = 'reverse'
    else:
        dist_diff = left_dist - right_dist
    ## If the distance on the left is greater than the distance on the right, the optimal direction is 'left'
        if dist_diff > 0:
            optimal_direction = 'left'
    ## If the distance on the right is greater than the distance on the left, the optimal direction is 'right'
        elif dist_diff < 0:
            optimal_direction = 'right'
    ## The remaining condition is equal distance
        else:
            optimal_direction = 'either right or left'
    #Return Optimal Direction
    print(optimal_direction, "is optimal")

    return optimal_direction
