##Using Python 3.6.5

##Import public library python-sys
import sys
##Import local library python-sensors: see sensors.py
import evade

## Test: Test base level check_fr logic - change x to lowest level check_fr_x used in script
print("\n\nStarting Test: evade_fwd_test7\n\n")
evade.check_fr_1(2, 2, 'left')
