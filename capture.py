import subprocess

# Capture screenshot
subprocess.run(["adb", "shell", "screencap", "/sdcard/screen.png"])
# Pull the screenshot to your machine
subprocess.run(["adb", "pull", "/sdcard/screen.png", "screen.png"])
