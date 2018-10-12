##Using Python 3.6.5

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
##Import local library evade: see evade.py
import evade

##Define optimal_direction as a global variable
##optimal_direction = optimal_direction.optimal_direction()

##RUn on startup: Look up "System D" Unit file... Google and see Digital Ocean. - when it starts, run this check with Andrew if stuck.
##Have mode be a switch of some kind. Hardawre: button on Pi
##Software - start in normal mode, switch in and out of Party mode

#Goal:
##1. Drive vechicle autonomously in "explore" mode.
##2. Constantly check the distance on the front sensor, print the result and take an additional remediation action
# ---sensors.distance() --- Return the distance from the sensor to the nearest object
## ---driveme_tank.init() --- Initialise GPIO pins to drive as output
## ---driveme_tank.forward(tf) --- Drive Foward
## ---driveme_tank.reverse(tf) --- Drive in Reverse
## ---driveme_tank.turn_left_fwd(tf) --- Turn left while moving forward
## ---driveme_tank.turn_right_fwd(tf) --- Turn right while moving forward
## ---driveme_tank.turn_left_rev(tf) --- Turn left while moving backward
## ---driveme_tank.turn_right_rev(tf) --- Turn right while moving backward
## ---driveme_tank.pivot_right(tf) --- Pivot clockwise (defined as from a 'birds eye view' with 12o'clock at the front of the vehicle (Pivot right)
## ---driveme_tank.pivot_left(tf) --- Pivot counter clockwise (Pivot left)

#Assumptions: see driveme_tank.py

def main():
    print("explore            > Help! I'm a function without definition: define me!")
##Once development is complete, move main() definition to the end of the script
##Python Main if __name__ == "__main__" E.g. Set a function called "Start" at the start of the file - see guru99.com
##def main():
##    do stuff
##Then put this in the end of the script. If python runs this file and you haven't specified anything it will run this..
##if __name__ == "__main__":
##    main()
##The main funciton will probably be some version of mode_discovery with a forever while loop

##Define a function to exit the program and print the reason "why" - to be specified in each function
def abort_drive(why):
    print(why)
    exit(0)
## OR
## switch to mode_RCD? Automatically? Or send a distress message?

##Define a function to run as the primary vehicle autonomous drive mode: mode_discovery

##Input: explore.mode_discovery(x, y, z, u)
##x is the time that left or right forward drive will run for assuming no obstacles
##y is the time that the vehicle should run for before checking input from the sensor
##z is the bias 'left' or 'right'
##u is the check status 'on' or 'off'
def mode_discovery(drive_time, drive_burst, mode, check):
    print("\n\nexplore            > Exploring with a", mode, "hand bias\n\n")
##When drive forward is chosen, continue for twice as long as the time spent driving to the left or right.
    drive_iterate = int(round(drive_time / drive_burst))
    drive_iterate_f = 2 * drive_iterate
    ##Desired result is to drive forward drive_burst seconds before checking (e.g. 0.03)
    ##Drive for drive_drive seconds
    ##Drive_iterations = drive_time

    ##1 represents forward, 2 represents forward and left, 3 represents forward and right
    LHB_options = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3]
    RHB_options = [1, 1, 1, 1, 1, 1, 2, 3, 3, 3]
    ##Set the bias right or left based on input chosen when calling mode_discovery(tf, mode)
    if mode == 'left':
        bias = LHB_options
    elif mode == 'right':
        bias = RHB_options
    else:
        print("explore            > 'mode' defined in function mode_discovery(drive_time, drive_burst, mode, check) must be 'left' or 'right'. Please try again.")
        ##Check if obstacle cheking should be on or off

    def collision_avoidance(drive_time, drive_burst):
        if check == 'on':
            evade.check_fr_1(drive_time, drive_burst)
        elif check == 'off':
            print("explore            > Driving blind!!\n")
        else:
            print("explore            > 'check' defined in function mode_discovery(drive_time, drive_burst, mode, check) must be 'on' or 'off'. Please try again.")

    ##Choose a random direction to travel in:
    x = random.choice(bias)
    ##If 1 is chosen at random from either LHB_options or RHB_options... (depending on bias 'left' or 'right')
    if x == 1:
        print("explore            > I will explore forward with caution")
        ##Repeat the steps below drive_iterate_f times
        for y in range(drive_iterate_f):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            collision_avoidance(drive_time, drive_burst)
            ##Drive forward for drive_burst seconds
            driveme_tank.forward(drive_burst, mode)

    ##If 2 is chosen at random from either LHB_options or RHB_options... (depending on bias 'left' or 'right')
    elif x == 2:
        print("explore            > I will explore forward and left with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            collision_avoidance(drive_time, drive_burst)
            ##Drive left and forward for drive_burst seconds
            driveme_tank.turn_left_fwd(drive_burst, mode)
    ##If 3 is chosen at random from either LHB_options or RHB_options... (depending on bias 'left' or 'right')
    elif x == 3:
        print("explore            > I will explore forward and right with caution")
        ##Repeat the steps below drive_iterate times
        for y in range(drive_iterate):
            ##Run the function collision_avoidance() to check the distance from the front sensor to the closest object
            collision_avoidance(drive_time, drive_burst)
            ##Drive right and forward for drive_burst seconds
            driveme_tank.turn_right_fwd(drive_burst, mode)
    else:
        abort_drive("explore            > Critical error in mode_discovery. Aborting...")

##for z in range(10):
##    mode_discovery(2, 'left')
