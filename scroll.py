import subprocess
import hashlib
import time,os
import uiproperties.navbtn as btn
import system.capture as capture 

def capture_screenshot(filename):
    # Capture a screenshot on the device and pull it to the local machine
    adb_screenshot_command = f"adb shell screencap -p /sdcard/{filename}"
    adb_pull_command = f"adb pull /sdcard/{filename} ./system/screenshot/{filename}"
    
    subprocess.run(adb_screenshot_command, shell=True)
    subprocess.run(adb_pull_command, shell=True)

def calculate_file_hash(filepath):
    # Calculate the hash of the screenshot file
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

ss_count = 0

def scroll(activity,up=True):
    global ss_count
    # Define file paths
    if ss_count ==0:
        directory_path = "system/screenshot"
        # Create the directory if it doesn't exist
        os.makedirs(directory_path, exist_ok=True)

    screenshot_dir = "./system/screenshot/"
    screenshot_before = "screenshot_before.png"
    screenshot_after = "screenshot_after.png"
    
    ss_count = ss_count+1
    # Capture the first screenshot before scrolling
    capture.shoot(activity,ss_count)
    capture_screenshot(screenshot_before)
    time.sleep(1)  # Wait a moment to ensure the screenshot is captured

    if up==True:
        # Perform the scroll
        # print(f"{-(btn.coordinate_y-1000)}")
        scroll_command = f"adb shell input touchscreen swipe 500 500 500 -600 1000"
    else:
        scroll_command = f"adb shell input touchscreen swipe 500 500 500 600 1000"
    subprocess.run(scroll_command, shell=True)
    time.sleep(1)  # Wait a moment for the screen to stabilize after the scroll

    # Capture the second screenshot after scrolling
    capture_screenshot(screenshot_after)

    # Calculate hashes of both screenshots
    hash_before = calculate_file_hash(screenshot_dir + screenshot_before)
    hash_after = calculate_file_hash(screenshot_dir + screenshot_after)

    # Compare hashes
    if hash_before == hash_after:
        ss_count=0
        print("No change in content. No more content to scroll.")
        print("Content captured succesfully...")

    else:
        scroll(activity)


# # Run the main function
# scroll()
