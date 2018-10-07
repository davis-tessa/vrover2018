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


def abort_drive(why):
    print(why, "\n\nEXITING... \nI suggest you work out Remote Control Override to avoid this in future!\n")
    sys.exit()

def stuck_help(why):
    print("evade.stuck_help   > Still too close!")
    print("evade.stuck_help   > Help! I'm Stuck!! rescue me!!\n")
    abort_drive(why)

def check_fr_4():
    ##Define the variable f_dist as the distance from the front sensor to the nearest object
    f_dist = sensors.front_distance()
    ##Instruct action: if an object is closer than 15 cm away, check for the optimal direction and take evasive action
    if f_dist < 15:
        stuck_help('Still too close at front on 4th check')
    else:
        print("evade.check_fr_4   > All clear in front!")


def evade_fwd_3(drive_time, drive_burst):
    drive_iterate = int(round(drive_time / drive_burst))
    print("evade.evade_fwd_3  > Still Too close!\nevade.evade_fwd_3  > Performing 3rd order evasive manouver\n")
    ##Bring the return of the function optimal_direction in from optimal_direction.py
    opt_dir = optimal_direction.optimal_direction()
    ##First, reverse
    print("evade.evade_fwd_3  > Reversing blind, no rear sensor check set up")
    driveme_tank.reverse(drive_time)
    ##If the optimal direction is left, drive forward and left
    if opt_dir == 'left':
        print("evade.evade_fwd_3  > I will proceed forward and left with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_4()
            ##Drive left and forward for drive_burst seconds
            driveme_tank.turn_left_fwd(drive_burst)
    ##If the optimal direction is right, drive forward and right
    elif opt_dir == 'right':
        print("evade.evade_fwd_3  > I will proceed forward and right with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_4()
            ##Drive right and forward for drive_burst seconds
            driveme_tank.turn_right_fwd(drive_burst)
    ##If the optimal direction is reverse, continue to reverse
    elif opt_dir == 'reverse':
        print("evade.evade_fwd_3  > Reversing blind, no rear sensor check set up")
        driveme_tank.reverse(drive_time)
    ##If the optimal direction is test_mode (manually configured), drive forward
    elif opt_dir == 'test_mode':
        print("evade.evade_fwd_3  > Test mode: driving forward ")
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_4()
            ##Drive right and forward for drive_burst seconds
            print("Evade 3: Action after checking")
    ##Results should be only 'left', 'right', or 'reverse'. If not, see optimal_direction.py
    else:
        print("evade.evade_fwd_3  > Unexpected result from optimal_direction.py")

def check_fr_3():
    ##Define the variable f_dist as the distance from the front sensor to the nearest object
    f_dist = sensors.front_distance()
        ##Instruct action: if an object is closer than 15 cm away, check for the optimal direction and take evasive action
    if f_dist < 15:
        evade_fwd_3(1, 1)
    else:
        print("evade.check_fr_3   > All clear in front!")

def evade_fwd_2(drive_time, drive_burst):
    drive_iterate = int(round(drive_time / drive_burst))
    print("evade.evade_fwd_2  > Still Too close!\nevade.evade_fwd_2  > Performing 2nd order evasive manouver\n")
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
        print("evade.evade_fwd_2  > I will proceed forward and right with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_3()
            ##Drive right and forward for drive_burst seconds
            driveme_tank.turn_right_fwd(drive_burst)
    ##If the optimal direction is reverse, continue to reverse
    elif opt_dir == 'reverse':
        print("evade.evade_fwd_2  > Reversing blind, no rear sensor check set up")
        driveme_tank.reverse(drive_time)
    ##If the optimal direction is test_mode (manually configured), drive forward
    elif opt_dir == 'test_mode':
        print("evade.evade_fwd_2  > Test mode: driving forward ")
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_3()
            ##Drive right and forward for drive_burst seconds
            print("Evade 2: Action after checking")
    ##Results should be only 'left', 'right', or 'reverse'. If not, see optimal_direction.py
    else:
        print("evade.evade_fwd_2  > Unexpected result from optimal_direction.py")

def check_fr_2():
    ##Define the variable f_dist as the distance from the front sensor to the nearest object
    f_dist = sensors.front_distance()
    ##Instruct action: if an object is closer than 15 cm away, check for the optimal direction and take evasive action
    if f_dist < 15:
        evade_fwd_2(1, 1)
    else:
        print("evade.check_fr_2   > All clear in front!")

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
        print("evade.evade_fwd_1  > I will proceed forward and right with caution")
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
    ##If the optimal direction is test_mode (manually configured), drive forward
    elif opt_dir == 'test_mode':
        print("evade.evade_fwd_1  > Test mode: driving forward ")
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_2()
            ##Drive right and forward for drive_burst seconds
            print("Evade 1: Action after checking")
    ##Results should be only 'left', 'right', or 'reverse'. If not, see optimal_direction.py
    else:
        print("evade.evade_fwd_1  > Unexpected result from optimal_direction.py")

def check_fr_1():
    ##Define the variable f_dist as the distance from the front sensor to the nearest object
    f_dist = sensors.front_distance()
    ##Instruct action: if an object is closer than 15 cm away, check for the optimal direction and take evasive action
    if f_dist < 15:
        evade_fwd_1(1, 1)
    else:
        print("evade.check_fr_1   > All clear in front!")
