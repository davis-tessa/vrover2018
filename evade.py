##Using Python 2.7.3

##Import public library python-RPi.GPIO
#import RPi.GPIO as gpio
##Import public library python-time
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





def stuck_help():
    print("evade.stuck_help   > Help! I'm stuck_get_help and I'm a function without definition: define me!")

def evade_fwd_3(tf):
    print("evade.evade_fwd_3  > Help! I'm evade_fwd_3 and I'm a function without definition: define me!")

def evade_fwd_2(drive_time, drive_burst):
    drive_iterate = int(round(drive_time / drive_burst))
    print("evade.evade_fwd_2  > Too close!\nevade.evade_fwd_2  > Performing 2nd order evasive manouver\n")
    ##Bring the return of the function optimal_direction in from optimal_direction.py
    opt_dir = optimal_direction.optimal_direction()
    ##First, reverse
    print("evade.evade_fwd_2  > Reversing blind, no rear sensor check set up")
    driveme_tank.reverse(drive_time)
    ##If the optimal direction is left, drive forward and left
    if opt_dir == 'left':
        print("evade.evade_fwd_2  > I will proceed forward and left with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_3()
            ##Drive left and forward for drive_burst seconds
            driveme_tank.turn_left_fwd(drive_burst)
    ##If the optimal direction is right, drive forward and right
    elif opt_dir == 'right':
        print("evade.evade_fwd_1  > I will proceed forward and left with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_2()
            ##Drive right and forward for drive_burst seconds
            driveme_tank.turn_right_fwd(drive_burst)
    ##If the optimal direction is reverse, continue to reverse
    elif opt_dir == 'reverse':
        print("evade.evade_fwd_1  > Reversing blind, no rear sensor check set up")
        driveme_tank.reverse(drive_time)
    ##Results should be only 'left', 'right', or 'reverse'. If not, see optimal_direction.py
    else:
        print("evade.evade_fwd_1  > Unexpected result from optimal_direction.py")

def check_fr_2():
    try:
        ##Define the variable f_dist as the distance from the front sensor to the nearest object
        f_dist = sensors.front_distance()
        ##Instruct action: if an object is closer than 15 cm away, check for the optimal direction and take evasive action
        if f_dist < 15:
            evade_fwd_2(1, 1)
        else:
            print("evade.check_fr_2   > All clear in front!")
    except:
        print("evade.check_fr_2   > Unable to check the front - debug evade functions.")

#Define the first order action to take when evading a forward obstacl
def evade_fwd_1(drive_time, drive_burst):
    drive_iterate = int(round(drive_time / drive_burst))
    print("evade.evade_fwd_1  > Too close!\nevade.evade_fwd_1  > Performing 1st order evasive manouver\n")
    ##Bring the return of the function optimal_direction in from optimal_direction.py
    opt_dir = optimal_direction.optimal_direction()
    ##First, reverse
    print("evade.evade_fwd_1  > Reversing blind, no rear sensor check set up")
    driveme_tank.reverse(drive_time)
    ##If the optimal direction is left, drive forward and left
    if opt_dir == 'left':
        print("evade.evade_fwd_1  > I will proceed forward and left with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_2()
            ##Drive left and forward for drive_burst seconds
            driveme_tank.turn_left_fwd(drive_burst)
    ##If the optimal direction is right, drive forward and right
    elif opt_dir == 'right':
        print("evade.evade_fwd_1  > I will proceed forward and left with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_2()
            ##Drive right and forward for drive_burst seconds
            driveme_tank.turn_right_fwd(drive_burst)
    ##If the optimal direction is reverse, continue to reverse
    elif opt_dir == 'reverse':
        print("evade.evade_fwd_1  > Reversing blind, no rear sensor check set up")
        driveme_tank.reverse(drive_time)
    ##Results should be only 'left', 'right', or 'reverse'. If not, see optimal_direction.py
    else:
        print("evade.evade_fwd_1  > Unexpected result from optimal_direction.py")

def check_fr_1():
    try:
        ##Define the variable f_dist as the distance from the front sensor to the nearest object
        f_dist = sensors.front_distance()
        ##Instruct action: if an object is closer than 15 cm away, check for the optimal direction and take evasive action
        if f_dist < 15:
            evade_fwd_1(1, 1)
        else:
            print("evade.check_fr_1   > All clear in front!")

    except:
        print("evade.check_fr_1  > Unable to check the front - debug evade functions.")
