import subprocess

def show_notification(title, message):
    # ADB command to create a notification using the 'service' command
    adb_command = f'adb shell service call notification 1 s16 "{title}" s16 "{message}"'
    
    # Execute the ADB command
    result = subprocess.run(adb_command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f'Notification sent: "{title}: {message}"')
    else:
        print("Error sending notification. Make sure ADB is connected and try again.")

show_notification("Connection Status", "Phone is connected successfully!")