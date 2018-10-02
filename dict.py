import time
import sys
import random

def front_distance():
    options = [2000, 60, 80, 21, 15, 64, 18, 33, 9]
    front_distance = random.choice(options)
    return front_distance

def pan_center():
##BREAKTHROUGH: Really simplify the functions in the sensors script!
##DEFINE ONLY single action functions here??
##Create the table in the explore file??

def pan_check_distance():
    distance_table = {}

    print("Watch me position center, take distance.")
    print ("Distance at front:")
    front_dist = front_distance()
    print(front_dist, "cm")
    distance_table['front'] = front_dist

##Take left distance
    print("Watch me position left, take distance.")
    print ("Distance to left:")
    left_dist = front_distance()
    print(left_dist, "cm")
    distance_table['left'] = left_dist

##Take right distance
    print("Watch me position right, take distance.")
    right_dist = front_distance()
    print(right_dist, "cm")
    distance_table['right'] = right_dist
#    print("front distance", distance_table['front'])
#    print("left distance", distance_table['left'])
#    print("right distance", distance_table['right'])
    if left_dist < 20 and right_dist < 20:
        optimal_direction = 'reverse'
    else:
        dist_diff = left_dist - right_dist
        if dist_diff >= 0:
            optimal_direction = 'left'
        elif dist_diff <= 0:
            optimal_direction = 'right'
        else:
            optimal_direction = 'either right or left'
##Return Optimal Direction
    return optimal_direction
    print(optimal_direction, "is optimal")
##    print(optimal_direction, "is optimal")

pan_check_distance()

'''    if left_dist < 20 and right_dist < 20:
        optimal_direction = 'reverse'
    else:
        dist_diff = left_dist - right_dist
        if dist_diff >= 0:
            optimal_direction = 'left'
        elif dist_diff <= 0:
            optimal_direction = 'right'
        else:
            optimal_direction = 'both'
##Return Optimal Direction
    return optimal_direction'''
