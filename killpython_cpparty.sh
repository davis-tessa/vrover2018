#/bin/bash
kill $(pgrep -f 'drive.py')
cp ./drive_party.py ./drive.py
exit 1
