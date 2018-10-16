#/bin/bash
kill $(pgrep -f 'drive.py')
python3 gpio_cleanup.py
exit 1
