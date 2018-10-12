##Using Python 3.6.5

##Import local library explore
import explore

##Test: check the mode_discovery function works WITHOUT CHECKING FOR Distance
##USE TO VALIDATE DECISION MAKING LOGIC
##Input: explore.mode_discovery(x, y, z, u)
##x is the time that left or right forward drive will run for assuming no obstacles
##y is the time that the vehicle should run for before checking input from the sensor
##z is the bias 'left' or 'right'
##u is the check status 'on' or 'off'

##How to set up tests that are possible without hardware:
##Pre-set the dictionary values for various scenarios... sensors are in development mode_discovery
##Advanced: Build a map to test the edge and corner cases

print("\n\nStarting Test: explore_test1\n\n")

for z in range(1):
    explore.mode_discovery(1, 1, 'left', 'off')

for z in range(1):
    explore.mode_discovery(1, 1, 'right', 'off')
