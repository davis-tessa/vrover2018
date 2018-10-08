##Using Python 2.7.3

##Import the GPIO library
#import RPi.GPIO as gpio
##Import the time library
import time
import sys
import random

#Goal: Drive vechicle using Remote Control including:
##front_sensor_trig is the GPIO pin number that triggers the sensor (GPIO pin configured as output)
##front_sensor_echo is the GPIO pin number that ingests the echo from the sensor

##front_sensor_trig = 7
##front_sensor_echo = 11
##back_sensor_trig = 31
##back_sensor_echo = 33
##pan_control = 12

##Look at using a dictionary to return front, left and right
####Consider sending the output of front_distance to memory and initialize in the right space.. (might be too cumbersome to write to a file)
##Pass by "threadsafe"
##THis is about re-writing this to be multi-threaded

##Define the distance function (to be imported into drive script)
def front_distance():
    print("sensors            > Front Sensor Distance Measurement in Progress")
    try:

        ##Define the GPIO pin number connected to trig
        front_sensor_trig = 7
    ##Define the GPIO pin number connected to echo
        front_sensor_echo = 29

        ##Set the gpio mode to "board" as opposed to BCM to use the physical pin numbers
        gpio.setmode(gpio.BOARD)
        ##Set up pins for trig (out of RPi, into sensor) and echo (out of sensor, in to RPi)
        gpio.setup(front_sensor_trig, gpio.OUT)
        gpio.setup(front_sensor_echo, gpio.IN)

        ##Making sure that the output pin has no pre-configured value
        gpio.output(front_sensor_trig, False)
        ##Print out notice that the sensor is initiating
        ##    print("Waiting for sensor to settle")
        ##Give the sensor time to come online
        time.sleep(1)

        ##Trigger the sensor (8 ultrasound bursts at 40 kHz)
        gpio.output(front_sensor_trig, True)
        ##Confiture the length of the burst to 10uS
        time.sleep(0.00001)
        ##Stop the burst after 10uS
        gpio.output(front_sensor_trig, False)

        ##Listen on the echo pin and as long as there is no signal, take a time stamp (time.time())
        while gpio.input(front_sensor_echo) == 0:
            pulse_start = time.time()
        ##Take a time stamp of the last recorded moment of a high signal
        while gpio.input(front_sensor_echo) == 1:
            pulse_end = time.time()
        ##Pulse_duration is the time that passed between a signal appearing and disappearing
        pulse_duration = pulse_end - pulse_start
        ##The speed of sound in air at sea level = 343m/s or 34 300cm/s
        ##s = d/t : d = s*t. The sound travels to the object and back so d = (s*t)/2
        front_distance = 17150 * pulse_duration
        ##Return an answer to 2 decimal places
        front_distance = round(front_distance, 2)

        ##Clen up the GPIO pins
        gpio.cleanup()

    except:
        print("sensors            > >>>> Sensors are not set up.\nsensors            > >>>>>>> Generating a random distance:\n")

        ##Options used to test a scenario where the sensors are >15cm away from an object the majority of the time
        options = [2000, 60, 80, 21, 14, 64, 18, 33, 9]
        ##Alternative set of options used to test a scenario where the sensors are >15cm away from an object ALL of the time
#        options = [2000, 60, 80, 21, 16, 64, 18, 33, 1000]
        ##Alternative set of options used to test the scenario where right and left are equal in pan_check_distance
#        options = [2000, 2000, 80, 80, 80, 80, 14, 20, 20]
        ##Alternative set of options used to test the scenario where the vehicle is trapped
#        options = [5, 6, 7, 8, 9, 10, 14, 3, 2]
        front_distance = random.choice(options)

##Instruct the function to return 'distance'
    print("sensors            >", front_distance, "cm\n")
    return front_distance

##Define the distance function (to be imported into drive script)
def rear_distance():
    try:
        print("sensors            > Rear Distance Measurement in Progress")
    ##Define the GPIO pin number connected to trig
        rear_sensor_trig = 31
    ##Define the GPIO pin number connected to echo
        rear_sensor_echo = 33

    ##Set the gpio mode to "board" as opposed to BCM to use the physical pin numbers
        gpio.setmode(gpio.BOARD)
    ##Set up pins for trig (out of RPi, into sensor) and echo (out of sensor, in to RPi)
        gpio.setup(rear_sensor_trig, gpio.OUT)
        gpio.setup(rear_sensor_echo, gpio.IN)

    ##Making sure that the output pin has no pre-configured value
        gpio.output(rear_sensor_trig, False)
    ##Print out notice that the sensor is initiating
    ##    print("Waiting for sensor to settle")
    ##Give the sensor time to come online
        time.sleep(0.001)

    ##Trigger the sensor (8 ultrasound bursts at 40 kHz)
        gpio.output(rear_sensor_trig, True)
    ##Confiture the length of the burst to 10uS
        time.sleep(0.00001)
    ##Stop the burst after 10uS
        gpio.output(rear_sensor_trig, False)

    ##Listen on the echo pin and as long as there is no signal, take a time stamp (time.time())
        while gpio.input(rear_sensor_echo) == 0:
            pulse_start = time.time()
    ##Take a time stamp of the last recorded moment of a high signal
        while gpio.input(rear_sensor_echo) == 1:
            pulse_end = time.time()
    ##Pulse_duration is the time that passed between a signal appearing and disappearing
        pulse_duration = pulse_end - pulse_start
    ##The speed of sound in air at sea level = 343m/s or 34 300cm/s
    ##s = d/t : d = s*t. The sound travels to the object and back so d = (s*t)/2
        rear_distance = 17150 * pulse_duration
    ##Return an answer to 2 decimal places
        rear_distance = round(rear_distance, 2)

    ##Clen up the GPIO pins
        gpio.cleanup()
    except:
        print("sensors            > Sensors are not configured.\nsensors            > Generating a random rear distance:\n")
        ##Options used to test a scenario where the sensors are >15cm away from an object the majority of the time
        options = [2000, 60, 80, 21, 14, 64, 18, 33, 9]
        ##Alternative set of options used to test a scenario where the sensors are >15cm away from an object ALL of the time
#        options = [2000, 60, 80, 21, 16, 64, 18, 33, 1000]
        ##Alternative set of options used to test the scenario where right and left are equal in pan_check_distance
#        options = [2000, 2000, 80, 80, 80, 80, 14, 20, 20]
        ##Alternative set of options used to test the scenario where the vehicle is trapped
#        options = [5, 6, 7, 8, 9, 10, 14, 3, 2]
        rear_distance = random.choice(options)

##Instruct the function to return 'distance'
    print("sensors            >", rear_distance, "cm\n")
    return rear_distance

##Define function to determine the optimal direction for travel
def pan_check_distance():
    distance_table = {}
    try:
        print("sensors            > Watch me position center, take distance.\n")
    ##Define pin mapping for pan control
        pan_control = 12
    ##Take front distance
    ##Set gpio to board mode
        gpio.setmode(gpio.BOARD)
    ##Set pan control gpio pin as output
        gpio.setup(pan_control, gpio.OUT)
    ##Set frequency for servo to 50 Hz
        pwm=gpio.PWM(pan_control, 50)
    ##Set starting position for servo to center
        pwm.start(7.5)
        ##Cleanup
        time.sleep(0.2)
        gpio.cleanup()
        print ("sensors            > Distance at front:")
        front_dist = front_distance()
        distance_table['front'] = front_dist

    ##Take left distance
        print("sensors            > Watch me position left, take distance.")
    ##Set gpio to board mode
        gpio.setmode(gpio.BOARD)
    ##Set pan control gpio pin as output
        gpio.setup(pan_control, gpio.OUT)
    ##Set frequency for servo to 50 Hz
        pwm=gpio.PWM(pan_control, 50)
    ##Set starting position for servo to center
        pwm.start(10)
        ##Cleanup
        time.sleep(0.2)
        gpio.cleanup()
        print ("sensors            > Distance to left:")
        left_dist = front_distance()
        distance_table['left'] = left_dist

    ##Take right distance
        print("sensors            > Watch me position right, take distance.")
    ##Set gpio to board mode
        gpio.setmode(gpio.BOARD)
    ##Set pan control gpio pin as output
        gpio.setup(pan_control, gpio.OUT)
    ##Set frequency for servo to 50 Hz
        pwm=gpio.PWM(pan_control, 50)
    ##Set starting position for servo to center
        pwm.start(5)
        ##Cleanup
        time.sleep(0.2)
        gpio.cleanup()
        print("sensors            > Watch me position right, take distance.")
        right_dist = front_distance()
        distance_table['right'] = right_dist

        print("sensors            > Watch me return to center and stop.")
    ##Define pin mapping for pan control
    ##Take front distance
    ##Set gpio to board mode
        gpio.setmode(gpio.BOARD)
    ##Set pan control gpio pin as output
        gpio.setup(pan_control, gpio.OUT)
    ##Set frequency for servo to 50 Hz
        pwm=gpio.PWM(pan_control, 50)
    ##Set starting position for servo to center
        pwm.start(7.5)
        ##Cleanup
        time.sleep(0.2)
        gpio.cleanup()

    except:

        print("sensors            > Front - RANDOM:")
        front_dist = front_distance()
        distance_table['front'] = front_dist

    ##Take left distance
        print("sensors            > Left - RANDOM:")
        left_dist = front_distance()
        distance_table['left'] = left_dist

    ##Take right distance
        print("sensors            > Right - RANDOM:")
        right_dist = front_distance()
        distance_table['right'] = right_dist

    return distance_table

##Define function to pan the servo motor
def front_pan():
    print("sensors            > Watch me position center, then left, then right, and back to center.")
##Define pin mapping for pan control
    pan_control = 12
##Set gpio to board mode
    gpio.setmode(gpio.BOARD)
##Set pan control gpio pin as output
    gpio.setup(pan_control, gpio.OUT)
##Set frequency for servo to 50 Hz
    pwm=gpio.PWM(pan_control, 50)
##Set starting position for servo to center
    pwm.start(7.5)
##Pivot to the left
    time.sleep(1)
    pwm.ChangeDutyCycle(10)
##Pivot to the right
    time.sleep(1)
    pwm.ChangeDutyCycle(5)
##Return to center
    time.sleep(1)
    pwm.ChangeDutyCycle(7.5)
##Cleanup
    time.sleep(0.2)
    gpio.cleanup()

##Define a function to check the optimal direction for travel

##Define function to pan the servo motor and to check the distance at each turn
def pan_check_distance_1():
    print("sensors            > Watch me position center, take distance.")
##Define pin mapping for pan control
    pan_control = 12
##Take front distance
##Set gpio to board mode
    gpio.setmode(gpio.BOARD)
##Set pan control gpio pin as output
    gpio.setup(pan_control, gpio.OUT)
##Set frequency for servo to 50 Hz
    pwm=gpio.PWM(pan_control, 50)
##Set starting position for servo to center
    pwm.start(7.5)
    ##Cleanup
    time.sleep(0.2)
    gpio.cleanup()
    print ("sensors            > Distance at front:")
    front_dist = front_distance()
    print (front_dist, "cm")

##Take left distance
    print("sensors            > Watch me position left, take distance.")
##Set gpio to board mode
    gpio.setmode(gpio.BOARD)
##Set pan control gpio pin as output
    gpio.setup(pan_control, gpio.OUT)
##Set frequency for servo to 50 Hz
    pwm=gpio.PWM(pan_control, 50)
##Set starting position for servo to center
    pwm.start(10)
    ##Cleanup
    time.sleep(0.2)
    gpio.cleanup()
    print ("sensors            > Distance to left:")
    front_dist = front_distance()
    print (front_dist, "cm")

##Take left distance
    print("sensors            > Watch me position right, take distance.")
##Set gpio to board mode
    gpio.setmode(gpio.BOARD)
##Set pan control gpio pin as output
    gpio.setup(pan_control, gpio.OUT)
##Set frequency for servo to 50 Hz
    pwm=gpio.PWM(pan_control, 50)
##Set starting position for servo to center
    pwm.start(5)
    ##Cleanup
    time.sleep(0.2)
    gpio.cleanup()
    print("sensors            > Distance to right:")
    front_dist = front_distance()
    print (front_dist, "cm")

    print("sensors            > Watch me return to center, take distance.")
##Define pin mapping for pan control
##Take front distance
##Set gpio to board mode
    gpio.setmode(gpio.BOARD)
##Set pan control gpio pin as output
    gpio.setup(pan_control, gpio.OUT)
##Set frequency for servo to 50 Hz
    pwm=gpio.PWM(pan_control, 50)
##Set starting position for servo to center
    pwm.start(7.5)
    ##Cleanup
    time.sleep(0.2)
    gpio.cleanup()
    print("sensors            > Distance at front:")
    front_dist = front_distance()
    print (front_dist, "cm")
