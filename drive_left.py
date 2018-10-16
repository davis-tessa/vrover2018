
##Import local library explore: see explore.py
import gpio_cleanup
import explore


gpio_cleanup.cleanup()

print("\n\ndrive_left         > Starting: drive_left\n\n")

for z in range(20):
    explore.mode_discovery(1, 0.10, 'left', 'off')

print("\n\ndrive_left         > Finished drive_left\n\nrun me again!")
