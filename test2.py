# import time
# import datetime

# def display_custom_time(hour, minute, second):
#     while True:
#         # Format and display the current time
#         print(f"{hour:02}:{minute:02}:{second:02}", end="\r")
#         time.sleep(1)  # Wait for 1 second
        
#         # Increment the time
#         second += 1
#         if second == 60:
#             second = 0
#             minute += 1
#         if minute == 60:
#             minute = 0
#             hour += 1
#         if hour == 24:
#             hour = 0  # Reset to 0 after 23:59:59
            
# # Set your initial time here
# initial_hour = 15
# initial_minute = 30
# initial_second = 0

# try:
#     display_custom_time(initial_hour, initial_minute, initial_second)
# except KeyboardInterrupt:
#     print("\nProgram stopped.")
            




  
  #((((merge two codes of alarm.py and teste2.py))))


import time
import sys
import datetime

# Function to display the custom time
def display_custom_time(hour, minute, second, alarm_hour, alarm_minute, alarm_second):
    while True:
        # Format and display the current custom time
        print(f"{hour:02}:{minute:02}:{second:02}", end="\r")
        sys.stdout.flush()
        time.sleep(1)  # Wait for 1 second
        
        # Increment the time
        second += 1
        if second == 60:
            second = 0
            minute += 1
        if minute == 60:
            minute = 0
            hour += 1
        if hour == 24:
            hour = 0  # Reset to 0 after 23:59:59
        
        # Check if the current time matches the alarm time
        if hour == alarm_hour and minute == alarm_minute and second == alarm_second:
            print("\n⏰ Playing alarm! Time is up! ⏰")
            break  # Stop the program when alarm goes off

# Show the current time before setting the alarm
now = datetime.datetime.now()
print("\nCurrent system time:", now.strftime("%H:%M:%S"))

# Prompt the user to set the alarm
print("Set your alarm:")
alarm_hour = int(input("Enter hour (0-23): "))
alarm_min = int(input("Enter minutes (0-59): "))
alarm_sec = int(input("Enter seconds (0-59): "))

# Set your initial custom time here
initial_hour = 15
initial_minute = 30
initial_second = 0

# Run the custom time display and alarm check
try:
    display_custom_time(initial_hour, initial_minute, initial_second, alarm_hour, alarm_min, alarm_sec)
except KeyboardInterrupt:
    print("\nProgram stopped.")






