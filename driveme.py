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

#Assumption: 4 Wheel Independence
#Refer to test image - colour is lead colour. GPIO input defined in variables:
#Blue Lead goes to right front wheel- forward spin (rt_fr_fwd) - green LED
#White lead goes to right front wheel- reverse spin (rt_fr_rev) - red LED
#Pink lead goes to right back wheel- forward spin (rt_bk_fwd) - green LED
#Grey lead goes to right back wheel- reverse spin (rt_fr_rev) - red LED
#Purple Lead goes to left front wheel- forward spin (lft_fr_fwd) - yellow LED
#Yellow lead goes to left front wheel- reverse spin (lft_fr_rev) - red LED
#Green lead goes to left back wheel- forward spin (lft_bk_fwd) - yellow LED
#Orange lead goes to left back wheel- reverse spin (lft_fr_rev) - red LED


##Define variables for each wheel to map to the GPIO pin output. Replace variables with the corresponding GPIO pin on your rover.
rt_fr_fwd = 16
rt_fr_rev = 18
rt_bk_fwd = 36
rt_bk_rev = 38
lft_fr_fwd = 13
lft_fr_rev = 15
lft_bk_fwd = 35
lft_bk_rev = 37

##Set up GPIO pins as output
def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(rt_fr_fwd, gpio.OUT)
    gpio.setup(rt_fr_rev, gpio.OUT)
    gpio.setup(lft_fr_fwd, gpio.OUT)
    gpio.setup(lft_fr_rev, gpio.OUT)
    gpio.setup(rt_bk_fwd, gpio.OUT)
    gpio.setup(rt_bk_rev, gpio.OUT)
    gpio.setup(lft_bk_fwd, gpio.OUT)
    gpio.setup(lft_bk_rev, gpio.OUT)

##Define a function that will drive the vechicle forward for an amount of time (tf)
def forward(tf):
    gpio.setmode(gpio.BOARD)
    gpio.output(rt_fr_fwd, True)
    gpio.output(rt_fr_rev, False)
    gpio.output(lft_fr_fwd, True)
    gpio.output(lft_fr_rev, False)
    gpio.output(rt_bk_fwd, True)
    gpio.output(rt_bk_rev, False)
    gpio.output(lft_bk_fwd, True)
    gpio.output(lft_bk_rev, False)

    time.sleep(tf)
    gpio.cleanup()

##Define a function that will drive the vechicle in reverse for an amount of time (tf)
def reverse(tf):
    gpio.output(rt_fr_fwd, False)
    gpio.output(rt_fr_rev, True)
    gpio.output(lft_fr_fwd, False)
    gpio.output(lft_fr_rev, True)
    gpio.output(rt_bk_fwd, False)
    gpio.output(rt_bk_rev, True)
    gpio.output(lft_bk_fwd, False)
    gpio.output(lft_bk_rev, True)
    time.sleep(tf)
    gpio.cleanup()

##Define a function that will drive the vechicle forward and left for an amount of time (tf)
def turn_left_fwd(tf):
    gpio.setmode(gpio.BOARD)
    gpio.output(rt_fr_fwd, True)
    gpio.output(rt_fr_rev, False)
    gpio.output(lft_fr_fwd, False)
    gpio.output(lft_fr_rev, False)
    gpio.output(rt_bk_fwd, True)
    gpio.output(rt_bk_rev, False)
    gpio.output(lft_bk_fwd, False)
    gpio.output(lft_bk_rev, False)

    time.sleep(tf)
    gpio.cleanup()

##Define a function that will drive the vechicle forward and right for an amount of time (tf)
def turn_right_fwd(tf):
    gpio.output(rt_fr_fwd, False)
    gpio.output(rt_fr_rev, False)
    gpio.output(lft_fr_fwd, True)
    gpio.output(lft_fr_rev, False)
    gpio.output(rt_bk_fwd, False)
    gpio.output(rt_bk_rev, False)
    gpio.output(lft_bk_fwd, True)
    gpio.output(lft_bk_rev, False)
    time.sleep(tf)
    gpio.cleanup()

##Define a function that will drive the vechicle in reverse and left for an amount of time (tf)
def turn_left_rev(tf):
    gpio.setmode(gpio.BOARD)
    gpio.output(rt_fr_fwd, False)
    gpio.output(rt_fr_rev, True)
    gpio.output(lft_fr_fwd, False)
    gpio.output(lft_fr_rev, False)
    gpio.output(rt_bk_fwd, False)
    gpio.output(rt_bk_rev, True)
    gpio.output(lft_bk_fwd, False)
    gpio.output(lft_bk_rev, False)

    time.sleep(tf)
    gpio.cleanup()

##Define a function that will drive the vechicle forward and right for an amount of time (tf)
def turn_right_rev(tf):
    gpio.output(rt_fr_fwd, False)
    gpio.output(rt_fr_rev, False)
    gpio.output(lft_fr_fwd, False)
    gpio.output(lft_fr_rev, True)
    gpio.output(rt_bk_fwd, False)
    gpio.output(rt_bk_rev, False)
    gpio.output(lft_bk_fwd, False)
    gpio.output(lft_bk_rev, True)
    time.sleep(tf)
    gpio.cleanup()

##Define a function that will pivot the vechicle clockwise (right) for an amount of time (tf)
def pivot_right(tf):
    gpio.setmode(gpio.BOARD)
    gpio.output(rt_fr_fwd, False)
    gpio.output(rt_fr_rev, True)
    gpio.output(lft_fr_fwd, True)
    gpio.output(lft_fr_rev, False)
    gpio.output(rt_bk_fwd, False)
    gpio.output(rt_bk_rev, True)
    gpio.output(lft_bk_fwd, True)
    gpio.output(lft_bk_rev, False)
    time.sleep(tf)
    gpio.cleanup()

##Define a function that will pivot the vechicle counter-clockwise (left) for an amount of time (tf)
def pivot_left(tf):
    gpio.output(rt_fr_fwd, True)
    gpio.output(rt_fr_rev, False)
    gpio.output(lft_fr_fwd, False)
    gpio.output(lft_fr_rev, True)
    gpio.output(rt_bk_fwd, True)
    gpio.output(rt_bk_rev, False)
    gpio.output(lft_bk_fwd, False)
    gpio.output(lft_bk_rev, True)
    time.sleep(tf)
    gpio.cleanup()


tf = 3
#drive vechicle forward for tf
forward(tf)
#turn vehicle left while moving forward for tf seconds
reverse(tf)
#turn vehicle left while moving forward for tf seconds
turn_left_fwd(tf)
#turn vehicle right while moving forward for tf seconds
turn_right_fwd(tf)
#turn vehicle left while reversing for tf seconds
turn_left_rev(tf)
#turn vehicle right while reversing for tf seconds
turn_right_rev(tf)
#Pivot vehicle clockwise (right) for tf seconds
pivot_right(tf)
#Pivot vehicle counterclockwise (left) while moving forward for tf seconds
pivot_left(tf)
