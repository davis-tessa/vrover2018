##Using Python 3.6.5

import RPi.GPIO as gpio
import time
import sys

rt_fwd = 18
rt_rev = 22
lft_fwd = 15
lft_rev = 13


##Set up GPIO pins as output
def init():
    try:
        print("driveme_tank       > Initialising GPIO Pins")
        gpio.setmode(gpio.BOARD)
        gpio.setup(rt_fwd, gpio.OUT)
        gpio.setup(rt_rev, gpio.OUT)
        gpio.setup(lft_fwd, gpio.OUT)
        gpio.setup(lft_rev, gpio.OUT)
    except:
        print("driveme_tank       > Your GPIO pins are not set up\n")

##Define a function that will drive the vechicle forward for an amount of time (tf)
def forward(tf, mode):
    try:
        print("driveme_tank       > Driving forward")
        init()

        gpio.output(rt_fwd, True)
        gpio.output(rt_rev, False)
        gpio.output(lft_fwd, True)
        gpio.output(lft_rev, False)
        time.sleep(tf)
        gpio.cleanup()

    except:
        print("driveme_tank       > Forward virtual: couldn't find wheels to drive\n")
        time.sleep(tf)

##Define a function that will drive the vechicle in reverse for an amount of time (tf)
def reverse(tf, mode):
    try:
        print("driveme_tank       > Driving in reverse")
        init()
        gpio.output(rt_fwd, False)
        gpio.output(rt_rev, True)
        gpio.output(lft_fwd, False)
        gpio.output(lft_rev, True)
        time.sleep(tf)
        gpio.cleanup()

    except:
        print("driveme_tank       > Reverse virtual: couldn't find wheels to drive\n")
        time.sleep(tf)
##Define a function that will drive the vechicle forward and left for an amount of time (tf)
def turn_left_fwd(tf, mode):
    try:
        print("driveme_tank       > Driving left and forward")
        init()
        gpio.output(rt_fwd, True)
        gpio.output(rt_rev, False)
        gpio.output(lft_fwd, False)
        gpio.output(lft_rev, False)
        time.sleep(tf)
        gpio.cleanup()
    except:
        print("driveme_tank       > Forward left virtual: couldn't find wheels to drive\n")
        time.sleep(tf)

##Define a function that will drive the vechicle forward and right for an amount of time (tf)
def turn_right_fwd(tf, mode):
    try:
        print("driveme_tank       > Driving right and forward")
        init()
        gpio.output(rt_fwd, False)
        gpio.output(rt_rev, False)
        gpio.output(lft_fwd, True)
        gpio.output(lft_rev, False)
        time.sleep(tf)
        gpio.cleanup()
    except:
        print("driveme_tank       > Forward right virtual: couldn't find wheels to drive\n")
        time.sleep(tf)

##Define a function that will drive the vechicle in reverse and left for an amount of time (tf)
def turn_left_rev(tf, mode):
    try:
        print("driveme_tank       > Driving left in reverse")
        init()
        gpio.output(rt_fwd, False)
        gpio.output(rt_rev, True)
        gpio.output(lft_fwd, False)
        gpio.output(lft_rev, False)
        time.sleep(tf)
        gpio.cleanup()
    except:
        print("driveme_tank       > Reverse left virtual: couldn't find wheels to drive\n")
        time.sleep(tf)

##Define a function that will drive the vechicle forward and right for an amount of time (tf)
def turn_right_rev(tf, mode):
    try:
        print("driveme_tank       > Driving right in reverse")
        init()
        gpio.output(rt_fwd, False)
        gpio.output(rt_rev, False)
        gpio.output(lft_fwd, False)
        gpio.output(lft_rev, True)
        time.sleep(tf)
        gpio.cleanup()
    except:
        print("driveme_tank       > Reverse right virtual: couldn't find wheels to drive\n")
        time.sleep(tf)

##Define a function that will pivot the vechicle clockwise (right) for an amount of time (tf)
def pivot_right(tf, mode):
    try:
        print("driveme_tank       > Pivoting right")
        init()
        gpio.output(rt_fwd, False)
        gpio.output(rt_rev, True)
        gpio.output(lft_fwd, True)
        gpio.output(lft_rev, False)
        time.sleep(tf)
        gpio.cleanup()
    except:
        print("driveme_tank       > Pivot right virtual: couldn't find wheels to drive\n")
        time.sleep(tf)

##Define a function that will pivot the vechicle counter-clockwise (left) for an amount of time (tf)
def pivot_left(tf, mode):
    try:
        print("driveme_tank       > Pivoting left")
        init()
        gpio.output(rt_fwd, True)
        gpio.output(rt_rev, False)
        gpio.output(lft_fwd, False)
        gpio.output(lft_rev, True)
        time.sleep(tf)
        gpio.cleanup()
    except:
        print("driveme_tank       > Reverse left virtual: couldn't find wheels to drive\n")
        time.sleep(tf)
