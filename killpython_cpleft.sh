#/bin/bash
kill $(pgrep -f 'drive.py')
cp ./drive_left.py ./drive.py
exit 1
