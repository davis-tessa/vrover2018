##Using Python 3.6.5

##Import local library explore
import explore
##Import time
import time

##Test: check the mode_discovery function works WITHOUT CHECKING FOR Distance
##USE TO VALIDATE DECISION MAKING LOGIC
##Input: explore.mode_discovery(x, y, z, u)
##x is the time that left or right forward drive will run for assuming no obstacles
##y is the time that the vehicle should run for before checking input from the sensor
##z is the bias 'left' or 'right'
##u is check status 'on' or 'off' meaning if 'off', there will be no sensor checks

## Expected behavior:
##  * Pick a direction  with a bias towards left and forward
##  * Drive for 1 second
##  * Repeat 5 times over
##  * Pick a direction  with a bias towards right and forward
##  * Drive for 1 second
##  * Repeat 5 times over

print("\n\nStarting Test: explore_test1\n\n")

for z in range(5):
    explore.mode_discovery(1, 1, 'left', 'off')

print("\n\nChanging mode\n\n")
time.sleep(2)

for z in range(5):
    explore.mode_discovery(1, 1, 'right', 'off')
