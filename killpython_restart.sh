#/bin/bash
kill $(pgrep -f 'drive.py')
python3 gpio_cleanup.py
python3 drive.py
exit 1
