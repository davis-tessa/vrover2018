##Using Python 3.6.5

##Import public library python-sys
import sys
##Import local library python-sensors: see sensors.py
import evade

## Test: Test mid level check_bk logic - change x to n level check_bk_x used in script
print("\n\nStarting Test: evade_rev_test3\n\n")
evade.check_bk_2(2, 2, 'left')
