##Using Python 2.7.3

##Code to Pan the Servo to 10/2/12 on the clock (12 o'clock is forward).
##To be used for: front sensor and camera
##Assumption: "Top" is the side of the servo that the payload is mounted. Reverse left and right is mount is vertically flipped

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.OUT)

pwm=GPIO.PWM(12, 50)

pwm.start(7.5)

#left
time.sleep(1)
pwm.ChangeDutyCycle(10)

#right
time.sleep(1)
pwm.ChangeDutyCycle(5)

#centre
time.sleep(1)
pwm.ChangeDutyCycle(7.5)
time.sleep(0.2)
GPIO.cleanup()
