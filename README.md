Guide on using GitHub from James McAfee:
https://github.com/james65535/h2k-Sessions/blob/master/Coding/coding-week2.md

IMPORTANT: Please see the team ONE DRIVE folder for additional documentation:
*PPT Guide to downloading repository
*PinOut guide (Excel)

One Drive: https://onevmw-my.sharepoint.com/personal/asingleton_vmware_com/_layouts/15/onedrive.aspx?e=5%3A5a350a00859e4099af3b4f67c4467240&FolderCTID=0x012000C46ABBAC13D03A4888982128F8B176EC&id=%2Fpersonal%2Fasingleton_vmware_com%2FDocuments%2FANZ%20IoT%20Virtual%20Team%2FAutonomous%20Vehicle%20Code

# House Rules:

1. Define human readable variables so it’s easy for the rest of the team to tell what  you are doing (avoid using x, y, 1, etc.)
 
2. ##Comment, ##comment, ##comment! Every line that needs an explanation (unless it's ridiculous). For ourselves (it helps to verify the logic as we go) and for others – it sounds like we will be potentially passing this on to other teams

3. Most bugs are caused by spelling mistakes or a mis-match in function definition between modules. Before assuming the logic is flawed, check your code:
 
  * Are there brackets in the wrong place or is there a bracket missing?
  * Are there spelling mistakes?
  * Did you forget the colon : when a function definition or if/while statement?
  * Check for upper/lower case errors. Python is case sensitive: E.g. the gpio function PWM
  * Are you using the same variable names as the rest of the team for the same function?
  * Are you using the same version of python as specified at the top of the script?

# vrover2018
# Application Architecture:
 https://drive.google.com/file/d/1XY8V5_Ue94OjASC9O3hmTFC60UACYjcd/view?usp=sharing
 
# driveme.py and driveme_test.py
  #driveme.py contains the functions to drive 4 wheels independently. These functions are referenced by other scripts including explore.py (i.e. use as a library)
  #drieme_test.py can be run to test GPIO pinout, H-bridge configuration and motor function when drive train is set up for 4 wheel drive

# driveme_tank.py and driveme_tank_test.py
  #driveme_tank.py contains the functions to drive two "arrays" of motors/wheels (right wheels drive together, left wheels drive together). These functions map 1:1 in the driveme.py library and explore.py can be changed to tank mode by finding all instances of driveme and replacing with driveme_tank.
  #driveme_tank_test.py can be run to test GPIO pinout, H-bridge configuration and motor function when drive train is set up to drive all right wheels together and all left wheels together

# pan.py
  #Code to pan servo motor
# sensors.py
  #Code to take measurements from front (servo) and back (stationary) ultrasonic sensors
# explore.py
  #Putting it all together: code to run the rover in "explore" mode
