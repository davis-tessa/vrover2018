##Using Python 3.6.5

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
## modified by KD - added enable code

rt_fwd = 18
rt_rev = 22
rt_ena = 16
lft_fwd = 15
lft_rev = 13
lft_ena = 11
mode_right = 38
mode_left = 36

def init():
    print("driveme_tank       > Initialising GPIO Pins")
    gpio.setmode(gpio.BOARD)
    gpio.setup(mode_right, gpio.OUT)
    gpio.setup(mode_left, gpio.OUT)
    gpio.setup(rt_fwd, gpio.OUT)
    gpio.setup(rt_rev, gpio.OUT)
    gpio.setup(rt_ena, gpio.OUT)
    gpio.setup(lft_fwd, gpio.OUT)
    gpio.setup(lft_rev, gpio.OUT)
    gpio.setup(lft_ena, gpio.OUT)

##    rt_ena_pwm = gpio.PWM(rt_ena, 1000)
##    lft_ena_pwm = gpio.PWM(lft_ena, 1000)
##    rt_ena_pwm.start(25)
##    lft_ena_pwm.start(25)

##Define a function that will drive the vechicle forward for an amount of time (tf)
def cleanup():
    init()
    print("Cleaning up pins")
    gpio.output(rt_ena, False)
    gpio.output(rt_fwd, False)
    gpio.output(rt_rev, False)
    gpio.output(lft_ena, False)
    gpio.output(lft_fwd, False)
    gpio.output(lft_rev, False)
    gpio.output(mode_right, False)
    gpio.output(mode_left, False)

    print("Flashing LEDs")
    for z in range(50):
        gpio.output(mode_right, True)
        gpio.output(mode_left, True)
        time.sleep(0.1)
        gpio.output(mode_right, False)
        gpio.output(mode_left, False)
        time.sleep(0.01)

    time.sleep(0.1)
    gpio.cleanup()

cleanup()
print("Configuration Updated!")
