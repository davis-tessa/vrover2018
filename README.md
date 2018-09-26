IMPORTANT: Please see the team ONE DRIVE folder for additional documentation:
*PPT Guide to downloading repository
*PinOut guide

One Drive: https://onevmw-my.sharepoint.com/personal/asingleton_vmware_com/_layouts/15/onedrive.aspx?e=5%3A5a350a00859e4099af3b4f67c4467240&FolderCTID=0x012000C46ABBAC13D03A4888982128F8B176EC&id=%2Fpersonal%2Fasingleton_vmware_com%2FDocuments%2FANZ%20IoT%20Virtual%20Team%2FAutonomous%20Vehicle%20Code

# vrover2018
# driveme.py and driveme_test.py
  #driveme.py contains the functions to drive 4 wheels independently. These functions are referenced by other scripts including explore.py (i.e. use as a library)
  #drieme_test.py can be run to test GPIO pinout, H-bridge configuration and motor function when drive train is set up for 4 wheel drive

# driveme_tank.py and driveme_tank_test.py
  #driveme_tank.py contains the functions to drive two "arrays" of motors/wheels (right wheels drive together, left wheels drive together). These functions map 1:1 in the driveme.py library and can be replaced in explore.py by finding driveme and replacing with driveme_tank.
  #driveme_tank_test.py can be run to test GPIO pinout, H-bridge configuration and motor function when drive train is set up to drive all right wheels together and all left wheels together

# pan.py
  #Code to pan servo motor
# sensors.py
  #Code to take measurements from front (servo) and back (stationary) ultrasonic sensors
# explore.py
  #Putting it all together: code to run the rover in "explore" mode
