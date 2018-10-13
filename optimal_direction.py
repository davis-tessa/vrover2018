##Using python3.6.5

import sys
import random
import sensors
import time

def optimal_direction():
##Toggle test mode:
#    optimal_direction = 'test_mode'
#Toggle comments to come out of test mode:
    ## Return the contents of the distance_table created by running the pan_check_distance function
    distance_table = sensors.pan_check_distance()
    print("optimal_direction  > Distance Summary:")
    print("\noptimal_direction  > >> front distance", distance_table['front'])
    front_dist = distance_table['front']
    print("optimal_direction  > >> left distance", distance_table['left'])
    left_dist = distance_table['left']
    print("optimal_direction  > >> right distance", distance_table['right'], "\n")
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
    ## The remaining condition is equal distance, choose a direction at random
        else:
            print("optimal_direction  > It's all the same to me.. my gut says")
            x = random.randrange(0, 2)
            if x == 0:
                optimal_direction = 'left'
            elif x == 1:
                optimal_direction = 'right'
            else:
                print("optimal_direction  > Something went wrong in random number generation.")
    #Return Optimal Direction
    time.sleep(1)
    print("optimal_direction  > ", optimal_direction, "is optimal\n")


    return optimal_direction

optimal_direction()
