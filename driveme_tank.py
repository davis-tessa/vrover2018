##Using Python 2.7.3

import RPi.GPIO as gpio
import time
import sys

#Goal: Drive vechicle using Remote Control including:
## ---driveme.init() --- Initialise GPIO pins to drive as output
## ---driveme.forward(tf) --- Drive Foward
## ---driveme.reverse --- Drive in Reverse
## ---driveme.turn_left_fwd --- Turn left while moving forward
## ---driveme.turn_right_fwd --- Turn right while moving forward
## ---driveme.turn_left_rev --- Turn left while moving backward
## ---driveme.turn_right_rev --- Turn right while moving backward
## ---driveme.pivot_right --- Pivot clockwise (defined as from a 'birds eye view' with 12o'clock at the front of the vehicle (Pivot right)
## ---driveme.pivot_left --- Pivot counter clockwise (Pivot left)

#Assumption: All right and all left wheels drive together.
#Refer to test image - colour is lead colour. GPIO input defined in variables:
#Blue Lead goes to right front wheel and back right wheel - forward spin (rt_fwd) - green LEDs
#White lead goes to right front wheel and right back wheel - reverse spin (rt_rev) - red LEDs

#Purple Lead goes to left front wheel and left back wheel - forward spin (lft_fwd) - yellow LEDs
#Yellow lead goes to left front wheel and left back wheel - reverse spin (lft_rev) - red LEDs

##Define variables for each wheel to map to the GPIO pin output. Replace variables with the corresponding GPIO pin on your rover.
rt_fwd = 16
rt_rev = 18
lft_fwd = 13
lft_rev = 15

##Set up GPIO pins as output
def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(rt_fwd, gpio.OUT)
    gpio.setup(rt_rev, gpio.OUT)
    gpio.setup(lft_fwd, gpio.OUT)
    gpio.setup(lft_rev, gpio.OUT)

##Define a function that will drive the vechicle forward for an amount of time (tf)
def forward(tf):
    gpio.setmode(gpio.BOARD)
    gpio.output(rt_fwd, True)
    gpio.output(rt_rev, False)
    gpio.output(lft_fwd, True)
    gpio.output(lft_rev, False)

    time.sleep(tf)
    gpio.cleanup()

##Define a function that will drive the vechicle in reverse for an amount of time (tf)
def reverse(tf):
    gpio.output(rt_fwd, False)
    gpio.output(rt_rev, True)
    gpio.output(lft_fwd, False)
    gpio.output(lft_rev, True)

    time.sleep(tf)
    gpio.cleanup()

##Define a function that will drive the vechicle forward and left for an amount of time (tf)
def turn_left_fwd(tf):
    gpio.setmode(gpio.BOARD)
    gpio.output(rt_fwd, True)
    gpio.output(rt_rev, False)
    gpio.output(lft_fwd, False)
    gpio.output(lft_rev, False)

    time.sleep(tf)
    gpio.cleanup()

##Define a function that will drive the vechicle forward and right for an amount of time (tf)
def turn_right_fwd(tf):
    gpio.output(rt_fwd, False)
    gpio.output(rt_rev, False)
    gpio.output(lft_fwd, True)
    gpio.output(lft_rev, False)

    time.sleep(tf)
    gpio.cleanup()

##Define a function that will drive the vechicle in reverse and left for an amount of time (tf)
def turn_left_rev(tf):
    gpio.setmode(gpio.BOARD)
    gpio.output(rt_fwd, False)
    gpio.output(rt_rev, True)
    gpio.output(lft_fwd, False)
    gpio.output(lft_rev, False)


    time.sleep(tf)
    gpio.cleanup()

##Define a function that will drive the vechicle forward and right for an amount of time (tf)
def turn_right_rev(tf):
    gpio.output(rt_fwd, False)
    gpio.output(rt_rev, False)
    gpio.output(lft_fwd, False)
    gpio.output(lft_rev, True)

    time.sleep(tf)
    gpio.cleanup()

##Define a function that will pivot the vechicle clockwise (right) for an amount of time (tf)
def pivot_right(tf):
    gpio.setmode(gpio.BOARD)
    gpio.output(rt_fwd, False)
    gpio.output(rt_rev, True)
    gpio.output(lft_fwd, True)
    gpio.output(lft_rev, False)

    time.sleep(tf)
    gpio.cleanup()

##Define a function that will pivot the vechicle counter-clockwise (left) for an amount of time (tf)
def pivot_left(tf):
    gpio.output(rt_fwd, True)
    gpio.output(rt_rev, False)
    gpio.output(lft_fwd, False)
    gpio.output(lft_rev, True)

    time.sleep(tf)
    gpio.cleanup()

#drive vechicle forward for tf
init()
forward(tf)
#turn vehicle left while moving forward for tf seconds
init()
reverse(tf)
#turn vehicle left while moving forward for tf seconds
init()
turn_left_fwd(tf)
#turn vehicle right while moving forward for tf seconds
init()
turn_right_fwd(tf)
#turn vehicle left while reversing for tf seconds
init()
turn_left_rev(tf)
#turn vehicle right while reversing for tf seconds
init()
turn_right_rev(tf)
#Pivot vehicle clockwise (right) for tf seconds
init()
pivot_right(tf)
#Pivot vehicle counterclockwise (left) while moving forward for tf seconds
init()
pivot_left(tf)
