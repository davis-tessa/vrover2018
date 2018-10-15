
import RPi.GPIO as gpio
import time
import sys

mode_right = 36
mode_left = 38
tf = 3

print("testarray       > Testing mode array")
gpio.setmode(gpio.BOARD)
gpio.setup(mode_right, gpio.OUT)
gpio.setup(mode_left, gpio.OUT)
time.sleep(tf)
print("Testing left hand mode")
gpio.output(mode_right, False)
gpio.output(mode_left, True)
time.sleep(tf)
print("Testing right hand mode")
gpio.output(mode_right, True)
gpio.output(mode_left, False)
time.sleep(tf)
print("Testing party mode")
gpio.output(mode_right, True)
gpio.output(mode_left, True)
time.sleep(tf)
print("Cleaning up pins")
time.sleep(tf)
gpio.cleanup()
