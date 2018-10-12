##Using Python 3.6.5

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

def seg_test():
    opt_dir = optimal_direction.optimal_direction()
    if opt_dir == 'left':
        print("Hi")
    ##If the optimal direction is right, drive forward and right
    elif opt_dir == 'right':
        print("Bye")
    else:
        stuck_help("evade.evade_rev_2  > Ooops!\nevade.evade_rev_2  > I don\'t know how to solve this problem")
    f_dist = sensors.front_distance()
    if f_dist > 15:
        print("Clear")
    else:
        print("Blocked")
seg_test()
