import subprocess
import os
from appium import webdriver
import time

# Function to get device name
def get_device_name():
    result = subprocess.run(["adb", "devices"], stdout=subprocess.PIPE, text=True)
    devices = result.stdout.splitlines()
    if len(devices) > 1:
        return devices[1].split()[0]  # Return the first device name
    else:
        raise Exception("No devices found. Please connect your Android device.")

# Function to get app package and main activity
def get_app_info(package_name):
    result = subprocess.run(["adb", "shell", "pm", "list", "packages"], stdout=subprocess.PIPE, text=True)
    packages = result.stdout.splitlines()
    if package_name not in packages:
        raise Exception(f"{package_name} is not installed on the device.")

    result = subprocess.run(["adb", "shell", "dumpsys", "package", package_name], stdout=subprocess.PIPE, text=True)
    for line in result.stdout.splitlines():
        if "launchMode" in line:
            activity_line = line
            activity = activity_line.split(" ")[-1]
            return package_name, activity
    raise Exception("Could not find the main activity.")

# Set your desired app package name here
app_package_name = "com.whatsapp"  # WhatsApp package

# Get device name
device_name = get_device_name()
print(f"Device Name: {device_name}")

# Get app package and main activity
app_package, main_activity = get_app_info(app_package_name)
print(f"App Package: {app_package}, Main Activity: {main_activity}")

# Set up Appium Desired Capabilities
desired_caps = {
    "platformName": "Android",
    "deviceName": device_name,
    "appPackage": app_package,
    "appActivity": main_activity,
    "autoGrantPermissions": True
}

# Start Appium session
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# Wait for the app to load
time.sleep(5)

# Function to take a screenshot
def capture_screenshot(counter):
    filename = f"screenshot_{counter}.png"
    screenshot_path = os.path.join(os.getcwd(), filename)
    driver.save_screenshot(screenshot_path)
    print(f"Captured: {screenshot_path}")

# Scroll and take screenshots
counter = 0
try:
    for _ in range(10):  # Adjust the range for more or fewer screenshots
        # Capture screenshot
        capture_screenshot(counter)
        counter += 1
        
        # Scroll down
        driver.swipe(500, 1500, 500, 500, 1000)  # Adjust coordinates based on your screen resolution
        time.sleep(2)  # Wait for a moment before taking the next screenshot
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Quit the driver
    driver.quit()
