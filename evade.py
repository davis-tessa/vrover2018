##Using Python 2.7.3

##Import public library python-RPi.GPIO
import RPi.GPIO as gpio
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
    print(why, "\n\nevade.abort_drive  > EXITING... \nevade.abort_drive  > I suggest you work out RC Override!\n")
    sys.exit()

def stuck_help(why):
    print("evade.stuck_help   > Help! I'm Stuck!! rescue me!!\n")
    abort_drive(why)

def check_bk_3(drive_time, drive_burst):
    print("evade.check_bk_3   > Now check the front sensor again - is it safe?\n")
    ##Define the variable r_dist as the distance from the rear sensor to the nearest object
    f_dist = sensors.front_distance()
    ##Instruct action: if an object is closer than 15 cm away, check for the optimal direction and take evasive action
    if f_dist < 15:
        stuck_help("evade.check_bk_3  > Ooops!\nevade.check_bk_2  > I don\'t know how to solve this problem")
    else:
        print("evade.check_bk_3   > All clear in front!")

def evade_rev_2(drive_time, drive_burst):
    drive_iterate = int(round(drive_time / drive_burst))
    print("evade.evade_rev_2  > Too close!\nevade.evade_rev_2  > Performing 2st order evasive manouver\n")
    ##Bring the return of the function optimal_direction in from optimal_direction.py
    opt_dir = optimal_direction.optimal_direction()

    if opt_dir == 'left':
        print("evade.evade_rev_2  > I will proceed forward and left with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_bk_3(drive_time, drive_burst)
            ##Drive left and forward for drive_burst seconds
            driveme_tank.turn_left_fwd(drive_burst)
    ##If the optimal direction is right, drive forward and right
    elif opt_dir == 'right':
        print("evade.evade_rev2  > I will proceed forward and right with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_bk_3(drive_time, drive_burst)
            ##Drive right and forward for drive_burst seconds
            driveme_tank.turn_right_fwd(drive_burst)
    else:
        stuck_help("evade.evade_rev_2  > Ooops!\nevade.evade_rev_2  > I don\'t know how to solve this problem")

def check_bk_2(drive_time, drive_burst):
    print("evade.check_bk_2   > I must find a way forward - checking the front:\n")
    ##Define the variable r_dist as the distance from the rear sensor to the nearest object
    f_dist = sensors.front_distance()
    ##Instruct action: if an object is closer than 15 cm away, check for the optimal direction and take evasive action
    if f_dist < 15:
        evade_rev_2(drive_time, drive_burst)
    else:
        print("evade.check_bk_2   > All clear in front!")

def evade_rev_1(drive_time, drive_burst):
    print("evade.evade_rev_1  > Too close!\nevade.evade_rev_1  > Performing 1st order evasive manouver\n")
    drive_iterate = int(round(drive_time / drive_burst))
    ##Bring the return of the function optimal_direction in from optimal_direction.py
    opt_dir = optimal_direction.optimal_direction()
    ##Check the front distance
    front_dist = sensors.front_distance()
    if front_dist > 15 and opt_dir == 'left':
        print("evade.evade_rev_1  > I will proceed forward and left with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Collision collision_avoidance
            check_bk_2(drive_time, drive_burst)
            ##Drive left and forward for drive_burst seconds
            driveme_tank.turn_left_fwd(drive_burst)

    elif front_dist > 15 and opt_dir == 'right':
        print("evade.evade_rev_1  > I will proceed forward and right with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Collision collision_avoidance
            check_bk_2(drive_time, drive_burst)
            ##Drive left and forward for drive_burst seconds
            driveme_tank.turn_right_fwd(drive_burst)

    else:
        stuck_help("evade.evade_rev_1  > Boxed in on 3-sides\nevade.evade_rev_1  > I don\'t know how to solve this problem")

def check_bk_1(drive_time, drive_burst):
    print("evade.check_bk_1   > First check of the rear sensor:\n")
    ##Define the variable r_dist as the distance from the rear sensor to the nearest object
    r_dist = sensors.rear_distance()
    ##Instruct action: if an object is closer than 15 cm away, check for the optimal direction and take evasive action
    if r_dist < 15:
        evade_rev_1(drive_time, drive_burst)
    else:
        print("evade.check_bk_1   > All clear behind!")

def check_fr_4(drive_time, drive_burst):
    print("evade.check_fr_4   > Fourth and final check of the front sensor:\n")
    ##Define the variable f_dist as the distance from the front sensor to the nearest object
    f_dist = sensors.front_distance()
    ##Instruct action: if an object is closer than 15 cm away, check for the optimal direction and take evasive action
    if f_dist < 15:
        stuck_help('evade.check_fr_4   > Still too close at front on 4th check')
    else:
        print("evade.check_fr_4   > All clear in front!")

def evade_fwd_3(drive_time, drive_burst):
    drive_iterate = int(round(drive_time / drive_burst))
    print("evade.evade_fwd_3  > Still Too close!\nevade.evade_fwd_3  > Performing 3rd order evasive manouver\n")
    ##Bring the return of the function optimal_direction in from optimal_direction.py
    opt_dir = optimal_direction.optimal_direction()
    ##First, reverse
    ##Repeat the steps below drive_iterate times
    for y in range(drive_iterate):
        ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
        check_bk_1(drive_time, drive_burst)
        ##Drive left and forward for drive_burst seconds
        driveme_tank.reverse(drive_burst)
    ##If the optimal direction is left, drive forward and left
    if opt_dir == 'left':
        print("evade.evade_fwd_3  > I will proceed forward and left with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_4(drive_time, drive_burst)
            ##Drive left and forward for drive_burst seconds
            driveme_tank.turn_left_fwd(drive_burst)
    ##If the optimal direction is right, drive forward and right
    elif opt_dir == 'right':
        print("evade.evade_fwd_3  > I will proceed forward and right with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_4(drive_time, drive_burst)
            ##Drive right and forward for drive_burst seconds
            driveme_tank.turn_right_fwd(drive_burst)
    ##If the optimal direction is reverse, continue to reverse
    elif opt_dir == 'reverse':
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_bk_1(drive_time, drive_burst)
            ##Drive left and forward for drive_burst seconds
            driveme_tank.reverse(drive_burst)
    ##If the optimal direction is test_mode (manually configured), drive forward
    elif opt_dir == 'test_mode':
        print("evade.evade_fwd_3  > Test mode: driving forward ")
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_4(drive_time, drive_burst)
            ##Drive right and forward for drive_burst seconds
            print("Evade 3: Action after checking")
    ##Results should be only 'left', 'right', or 'reverse'. If not, see optimal_direction.py
    else:
        print("evade.evade_fwd_3  > Unexpected result from optimal_direction.py")

def check_fr_3(drive_time, drive_burst):
    print("evade.check_fr_3   > Third check of the front sensor:\n")
    ##Define the variable f_dist as the distance from the front sensor to the nearest object
    f_dist = sensors.front_distance(drive_time, drive_burst)
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
    ##Repeat the steps below drive_iterate times
    for y in range(drive_iterate):
        ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
        check_bk_1(drive_time, drive_burst)
        ##Drive left and forward for drive_burst seconds
        driveme_tank.reverse(drive_burst)
    ##If the optimal direction is left, drive forward and left
    if opt_dir == 'left':
        print("evade.evade_fwd_2  > I will proceed forward and left with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_3(drive_time, drive_burst)
            ##Drive left and forward for drive_burst seconds
            driveme_tank.turn_left_fwd(drive_burst)
    ##If the optimal direction is right, drive forward and right
    elif opt_dir == 'right':
        print("evade.evade_fwd_2  > I will proceed forward and right with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_3(drive_time, drive_burst)
            ##Drive right and forward for drive_burst seconds
            driveme_tank.turn_right_fwd(drive_burst)
    ##If the optimal direction is reverse, continue to reverse
    elif opt_dir == 'reverse':
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_bk_1(drive_time, drive_burst)
            ##Drive left and forward for drive_burst seconds
            driveme_tank.reverse(drive_burst)
    ##If the optimal direction is test_mode (manually configured), drive forward
    elif opt_dir == 'test_mode':
        print("evade.evade_fwd_2  > Test mode: driving forward ")
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_3(drive_time, drive_burst)
            ##Drive right and forward for drive_burst seconds
            print("Evade 2: Action after checking")
    ##Results should be only 'left', 'right', or 'reverse'. If not, see optimal_direction.py
    else:
        print("evade.evade_fwd_2  > Unexpected result from optimal_direction.py")

def check_fr_2(drive_time, drive_burst):
    print("evade.check_fr_2   >Second check of the front sensor:\n")
    f_dist = sensors.front_distance()
    ##Instruct action: if an object is closer than 15 cm away, check for the optimal direction and take evasive action
    if f_dist < 15:
        evade_fwd_2(drive_time, drive_burst)
    else:
        print("evade.check_fr_2   > All clear in front!")

#Define the first order action to take when evading a forward obstacl
def evade_fwd_1(drive_time, drive_burst):
    drive_iterate = int(round(drive_time / drive_burst))
    print("evade.evade_fwd_1  > Too close!\nevade.evade_fwd_1  > Performing 1st order evasive manouver\n")
    ##Bring the return of the function optimal_direction in from optimal_direction.py
    opt_dir = optimal_direction.optimal_direction()
    ##First, reverse
    print("evade.evade_fwd_1  > I will reverse with caution.")

    ##Repeat the steps below drive_iterate times
    for y in range(drive_iterate):
        ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
        check_bk_1(drive_time, drive_burst)
        ##Drive left and forward for drive_burst seconds
        driveme_tank.reverse(drive_burst)
    ##If the optimal direction is left, drive forward and left
    if opt_dir == 'left':
        print("evade.evade_fwd_1  > I will proceed forward and left with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_2(drive_time, drive_burst)
            ##Drive left and forward for drive_burst seconds
            driveme_tank.turn_left_fwd(drive_burst)
    ##If the optimal direction is right, drive forward and right
    elif opt_dir == 'right':
        print("evade.evade_fwd_1  > I will proceed forward and right with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_2(drive_time, drive_burst)
            ##Drive right and forward for drive_burst seconds
            driveme_tank.turn_right_fwd(drive_burst)
    ##If the optimal direction is reverse, continue to reverse
    elif opt_dir == 'reverse':
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_bk_1(drive_time, drive_burst)
            ##Drive left and forward for drive_burst seconds
            driveme_tank.reverse(drive_burst)
    ##If the optimal direction is test_mode (manually configured), drive forward
    elif opt_dir == 'test_mode':
        print("evade.evade_fwd_1  > Test mode: driving forward ")
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            check_fr_2(drive_time, drive_burst)
            ##Drive right and forward for drive_burst seconds
            print("Evade 1: Action after checking")
    ##Results should be only 'left', 'right', or 'reverse'. If not, see optimal_direction.py
    else:
        print("evade.evade_fwd_1  > Unexpected result from optimal_direction.py")

def check_fr_1(drive_time, drive_burst):
    print("evade.check_fr_1   > First check of the front sensor:\n")
    ##Define the variable f_dist as the distance from the front sensor to the nearest object
    f_dist = sensors.front_distance()
    ##Instruct action: if an object is closer than 15 cm away, check for the optimal direction and take evasive action
    if f_dist < 15:
        evade_fwd_1(drive_time, drive_burst)
    else:
        print("evade.check_fr_1   > All clear in front!")
