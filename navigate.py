import subprocess
import time
import uiproperties.navbtn as btn
import system.capture as capture
import os
import scroll 


def open_activity():
    tap_activity = f"adb shell input tap {btn.acivity_button_x} {btn.top_nav_y}"
    subprocess.run(tap_activity, shell=True)
    time.sleep(2)
    print("Activity Opened...")
    

    # Define the directory path
    directory_path = "screenshots/activity"

    # Create the directory if it doesn't exist
    os.makedirs(directory_path, exist_ok=True)
    # Check if the directory was created
    os.path.exists(directory_path)
    print("Directory Created : screenshot/activity")

def scroll_to_bottom():
    scroll.scroll("activity")
   

def parse_activity():
    open_activity()
    scroll_to_bottom()
   
