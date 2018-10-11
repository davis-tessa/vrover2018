#/bin/bash
kill $(pgrep -f 'drive.py')
cp ./drive_right.py ./drive.py
exit 1
