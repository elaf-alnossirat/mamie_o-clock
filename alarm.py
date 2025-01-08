
import time
import sys
import datetime

# Function to 



# Function to display the current time
def display_current_time():
    now = datetime.datetime.now()
    print("\nCurrent time:", now.strftime("%H:%M:%S"))

# Show the current time before setting the alarm
display_current_time()

# Prompt the user to set the alarm
print("Set your alarm:")
alarm_hour = int(input("Enter hour (0-23): "))
alarm_min = int(input("Enter minutes (0-59): "))
alarm_sec = int(input("Enter seconds (0-59): "))

# Main loop: continuously display the time and check for the alarm
try:
    while True:
        # Get the current time
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        
        # Display the current time
        print(current_time, end="\r")
        sys.stdout.flush()
        
        # Check if the current time matches the alarm time
        if now.hour == alarm_hour and now.minute == alarm_min and now.second == alarm_sec:
            print("\n⏰ Playing alarm! Time is up! ⏰")
            break
        
        # Wait for 0.4 seconds before updating the time
        time.sleep(0.4)
except KeyboardInterrupt:
    print("\nProgram stopped.")
