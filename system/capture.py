import subprocess,time


def shoot(activity,num):
    # Capture screenshot
    subprocess.run(["adb", "shell", "screencap", "/sdcard/screen.png"])
    # Pull the screenshot to your machine
    subprocess.run(["adb", "pull", "/sdcard/screen.png", f"screenshots/{activity}/{num}.png"])
    time.sleep(1)
