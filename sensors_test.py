##Using Python 2.7.3

##Import the GPIO library
import RPi.GPIO as gpio
##Import the time library
import time
##Import the local sensors library
import sensors

##Test 1: check that the front sensor is correctly wired and functional
##Expected result: prints:
##<Front Distance Measurement in Progress
## xx.xx cm>
#print sensors.front_distance(), "cm"

##Test 2: check that the rear sensor is correctly wired and functional
##Expected result: prints:
##<Rear Distance Measurement in Progress
## xx.xx cm>
#print sensors.rear_distance(), "cm"

##Test 3: check that the servo motor is correctly wired and functional
##Expected result: Servo motor moves to center, left ~30 degrees, right ~30 degrees, back to center
#sensors.front_pan()

##Test 4: check that distance measurements take place between servo rotations
##Expected result: Servo motor moves to center, prints:
##<Watch me position center, take distance.
##Distance at front:
##Front Sensor Distance Measurement in Progress
#xx.xx cm>
##Servo motor moves to left, prints:
##<Watch me position left, take distance.
##Distance to left:
##Front Sensor Distance Measurement in Progress
#xx.xx cm>
##Servo motor moves to right, prints:
##<Watch me position right, take distance.
##Distance at right:
##Front Sensor Distance Measurement in Progress
#xx.xx cm>
##Servo motor moves to center, prints:
##<Watch me position center, take distance.
##Distance at front:
##Front Sensor Distance Measurement in Progress
#xx.xx cm>
sensors.pan_check_distance_1()

##Define a function to check the optimal direction for travel

##Capture distance at left pivot

##Troubleshooting:

## Test 1:

## Error 1:
## <Traceback (most recent call last):
## File "sensors_test.py", line 22, in <module>
## print sensors.front_distance(), "cm"
## File "/home/pi/vforum2018/sensors.py", line 53, in front_distance
## pulse_duration = pulse_end - pulse_start>
## Cause: Theory: The sensor fails to trigger OR Theory: The sensor triggers before the RPi has a chance to capture the pre-trigger state
## Testing: The error appears randomly only on the front sensor (not on the rear sensor) with a frequency of approximately 1 in 3 attempts. Likely to be a faulty sensor or faulty connection
## Resolution: Replace front sensor for production. OR see comment in sensors.py "Give the sensor time to come online" - increase tf in time.sleep(tf)




'''def pan_left():
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
##Cleanup
    time.sleep(0.2)
    gpio.cleanup()
'''
'''
##Define the distance function (to be imported into drive script)
def left_distance():

##Define the GPIO pin number connected to trig
    front_sensor_trig = 7
##Define the GPIO pin number connected to echo
    front_sensor_echo = 11

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
    time.sleep(0.001)

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

##Instruct the function to return 'distance'
    return left_distance

print left_distance(), "cm"
'''
'''
def front_pan():
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
'''
'''
    if left_distance() < 20 and right_distance() < 20:
        optimal_direction = 'reverse'
    else:
        dist_diff = left_distance() - right_distance()
        if dist_diff >= 0:
            optimal_direction = 'left'
        if dist_diff <= 0:
            optimal_direction = 'right'

    return optimal_direction

print optimal_direction()
'''

'''##Define a function to trigger the server to pan
def front_pan():

    gpio.setmode(gpio.BOARD)

    gpio.setup(12,gpio.OUT)

    pwm=gpio.PWM(12, 50)

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
    gpio.cleanup()

##front_pan()
'''
'''
##Define the distance function (to be imported into drive script)
def front_distance():

##Define the GPIO pin number connected to trig
    front_sensor_trig = 7
##Define the GPIO pin number connected to echo
    front_sensor_echo = 11

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
    time.sleep(0.001)

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

##Instruct the function to return 'distance'
    return front_distance

print front_distance(), "cm"
'''
'''
##Define the distance function for the back side (to be imported into drive script)
def back_distance():
##Define the GPIO pin number xx connected to trig
    back_sensor_trig = 31
##Define the GPIO pin number yy connected to echo
    back_sensor_echo = 33

##Set the gpio mode to "board" as opposed to BCM to use the physical pin numbers
    gpio.setmode(gpio.BOARD)
##Set up pins for trig (out of RPi, into sensor) and echo (out of sensor, in to RPi)
    gpio.setup(back_sensor_trig, gpio.OUT)
    gpio.setup(back_sensor_echo, gpio.IN)

##Making sure that the output pin has no pre-configured value
    gpio.output(back_sensor_trig, False)
##Print out notice that the sensor is initiating
##    print("Waiting for sensor to settle")
##Give the sensor time to come online
    time.sleep(0.00001)

##Trigger the sensor (8 ultrasound bursts at 40 kHz)
    gpio.output(back_sensor_trig, True)
##Confiture the length of the burst to 10uS
    time.sleep(0.00001)
##Stop the burst after 10uS
    gpio.output(back_sensor_trig, False)

##Listen on the echo pin and as long as there is no signal, take a time stamp (time.time())
    while gpio.input(back_sensor_echo) == 0:
        pulse_start = time.time()
##Take a time stamp of the last recorded moment of a high signal
    while gpio.input(back_sensor_echo) == 1:
        pulse_end = time.time()
##Pulse_duration is the time that passed between a signal appearing and disappearing
    pulse_duration = pulse_end - pulse_start

##The speed of sound in air at sea level = 343m/s or 34 300cm/s
##s = d/t : d = s*t. The sound travels to the object and back so d = (s*t)/2
    back_distance = 17150 * pulse_duration
##Return an answer to 2 decimal places
    back_distance = round(back_distance, 2)

##Clen up the GPIO pins
    gpio.cleanup()

##Instruct the function to return 'distance'
    return back_distance

print back_distance(), "cm"
'''
'''
##Define the distance function for the right side (to be imported into drive script)
def right_distance():

##Define the GPIO pin number xx connected to trig
    right_sensor_trig = 12
##Define the GPIO pin number yy connected to echo
    right_sensor_echo = 22

##Set the gpio mode to "board" as opposed to BCM to use the physical pin numbers
    gpio.setmode(gpio.BOARD)
##Set up pins for trig (out of RPi, into sensor) and echo (out of sensor, in to RPi)
    gpio.setup(right_sensor_trig, gpio.OUT)
    gpio.setup(right_sensor_echo, gpio.IN)

##Making sure that the output pin has no pre-configured value
    gpio.output(right_sensor_trig, False)
##Print out notice that the sensor is initiating
##    print("Waiting for sensor to settle")
##Give the sensor time to come online
    time.sleep(0.00001)

##Trigger the sensor (8 ultrasound bursts at 40 kHz)
    gpio.output(right_sensor_trig, True)
##Confiture the length of the burst to 10uS
    time.sleep(0.00001)
##Stop the burst after 10uS
    gpio.output(right_sensor_trig, False)

##Listen on the echo pin and as long as there is no signal, take a time stamp (time.time())
    while gpio.input(right_sensor_echo) == 0:
        pulse_start = time.time()
##Take a time stamp of the last recorded moment of a high signal
    while gpio.input(right_sensor_echo) == 1:
        pulse_end = time.time()
##Pulse_duration is the time that passed between a signal appearing and disappearing
    pulse_duration = pulse_end - pulse_start

##The speed of sound in air at sea level = 343m/s or 34 300cm/s
##s = d/t : d = s*t. The sound travels to the object and back so d = (s*t)/2
    right_distance = 17150 * pulse_duration
##Return an answer to 2 decimal places
    right_distance = round(right_distance, 2)

##Clen up the GPIO pins
    gpio.cleanup()

##Instruct the function to return 'distance'
    return right_distance

##Define the distance function for the left side (to be imported into drive script)
def left_distance():

##Define the GPIO pin number xx connected to trig
    left_sensor_trig = 29
##Define the GPIO pin number yy connected to echo
    left_sensor_echo = 31

##Set the gpio mode to "board" as opposed to BCM to use the physical pin numbers
    gpio.setmode(gpio.BOARD)
##Set up pins for trig (out of RPi, into sensor) and echo (out of sensor, in to RPi)
    gpio.setup(left_sensor_trig, gpio.OUT)
    gpio.setup(left_sensor_echo, gpio.IN)

##Making sure that the output pin has no pre-configured value
    gpio.output(left_sensor_trig, False)
##Print out notice that the sensor is initiating
##    print("Waiting for sensor to settle")
##Give the sensor time to come online
    time.sleep(0.00001)

##Trigger the sensor (8 ultrasound bursts at 40 kHz)
    gpio.output(left_sensor_trig, True)
##Confiture the length of the burst to 10uS
    time.sleep(0.00001)
##Stop the burst after 10uS
    gpio.output(left_sensor_trig, False)

##Listen on the echo pin and as long as there is no signal, take a time stamp (time.time())
    while gpio.input(left_sensor_echo) == 0:
        pulse_start = time.time()
##Take a time stamp of the last recorded moment of a high signal
    while gpio.input(left_sensor_echo) == 1:
        pulse_end = time.time()
##Pulse_duration is the time that passed between a signal appearing and disappearing
    pulse_duration = pulse_end - pulse_start

##The speed of sound in air at sea level = 343m/s or 34 300cm/s
##s = d/t : d = s*t. The sound travels to the object and back so d = (s*t)/2
    left_distance = 17150 * pulse_duration
##Return an answer to 2 decimal places
    left_distance = round(left_distance, 2)

##Clen up the GPIO pins
    gpio.cleanup()

##Instruct the function to return 'distance'
    return left_distance

def clearest_path():
    if left_distance() < 20 and right_distance() < 20:
        clearest_path = 'reverse'
    else:
        dist_diff = left_distance() - right_distance()
        if dist_diff >= 0:
            clearest_path = 'left'
        if dist_diff <= 0:
            clearest_path = 'right'
'''

##print front_distance(), "cm"
##print right_distance(), "cm"
##print left_distance(), "cm"
