
##Import local library explore: see explore.py
import gpio_cleanup
import explore

gpio_cleanup.cleanup()
print("\n\nStarting Test: drive_right\n\n")

for z in range(20):
    explore.mode_discovery(2, 1.00, 'right', 'on')

print("\n\nFinished drive_right\n\nrun me again!")
