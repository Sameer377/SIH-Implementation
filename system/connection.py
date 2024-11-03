import subprocess,time

def check_adb_device():
    try:
        # Run the adb devices command
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
        
        # Check the output
        if "device" in result.stdout:
            # If a device is listed, print a message
            print(f"ADB device is connected : {result.stdout}")
            launch_instagram()
        else:
            print("No ADB device is connected.")
    except FileNotFoundError:
        print("ADB is not installed or not found in the system PATH.")
    except Exception as e:
        print(f"An error occurred: {e}")


def launch_instagram():
     subprocess.run("adb shell am start -n com.instagram.android/.activity.MainTabActivity", shell=True)
     time.sleep(3)
     pass

