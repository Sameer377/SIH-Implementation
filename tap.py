import subprocess
import time
# Coordinates to tap on the screen
x, y = 54, 1824
x1, y1 = 270, 1824
x2, y2 = 760, 1824
x3, y3 = 960, 1824

# Construct the ADB command
tap_home = f"adb shell input tap {x} {y}"
tap_search = f"adb shell input tap {x1} {y1}"
tap_reel = f"adb shell input tap {x2} {y2}"
tap_profile = f"adb shell input tap {x3} {y3}"

scroll = f"adb shell input touchscreen swipe 500 500 500 -2000 1000"

x4,y4 = 1020,1003
tap_like = f"adb shell input tap {x4} {y4}"
tap_story = f"adb shell input tap 115 1500"
tap_close = f"adb shell input tap 1030 150"


for i in range(1,5):
    # Execute the command
    print(f"Executing command: {tap_home}")
    subprocess.run(tap_home, shell=True)
    time.sleep(0.5)
    print(f"Executing command: {scroll}")
    subprocess.run(scroll, shell=True)
    print(f"Executing command: {tap_search}")
    subprocess.run(tap_search, shell=True)
    time.sleep(0.5)
    print(f"Executing command: {scroll}")
    subprocess.run(scroll, shell=True)
    print(f"Executing command: {tap_reel}")
    subprocess.run(tap_reel, shell=True)
    time.sleep(0.5)
    print(f"Executing command: {scroll}")
    subprocess.run(scroll, shell=True)
    time.sleep(0.5)
    print(f"Executing command: {tap_like}")
    subprocess.run(tap_like, shell=True)
    time.sleep(0.5)
    print(f"Executing command: {tap_profile}")
    subprocess.run(tap_profile, shell=True)
    time.sleep(0.5)
    print(f"Executing command: {tap_story}")
    subprocess.run(tap_story, shell=True)
    time.sleep(1.5)
    print(f"Executing command: {tap_close}")
    subprocess.run(tap_close, shell=True)
    time.sleep(0.5)

