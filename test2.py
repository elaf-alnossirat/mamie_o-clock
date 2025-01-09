import time
import sys
import datetime


# Function to display the current time dynamically
def display_current_time():
    print("\nCurrent time:")
    while True:
        now = datetime.datetime.now()
        print(now.strftime("%H:%M:%S"), end="\r")
        time.sleep(1)


# Function to display and update the manually reset time dynamically
def display_reset_time(hour, minute, second):
    print("\nUpdated time after resetting:")
    while True:
        print(f"{hour:02}:{minute:02}:{second:02}", end="\r")
        time.sleep(1)
        # Increment the time
        second += 1
        if second == 60:
            second = 0
            minute += 1
        if minute == 60:
            minute = 0
            hour += 1
        if hour == 24:
            hour = 0


  

# Function to reset the time manually
def reset_time():
    print("\nReset the time manually:")
    try:
        new_hour = int(input("Enter hour (0-23): "))
        new_minute = int(input("Enter minute (0-59): "))
        new_second = int(input("Enter second (0-59): "))
        
        if 0 <= new_hour < 24 and 0 <= new_minute < 60 and 0 <= new_second < 60:
            return new_hour, new_minute, new_second
        else:
            print("Invalid time entered. Please try again.")
            return reset_time()  # Retry on invalid input
    except ValueError:
        print("Please enter valid numeric values.")
        return reset_time()  # Retry on invalid input
      

        


# Function to set and check the alarm
def set_and_check_alarm(alarm_hour, alarm_minute, alarm_second, hour, minute, second):
    print("\nClock is running:")
    while True:
        print(f"{hour:02}:{minute:02}:{second:02}", end="\r")
        time.sleep(1)
        # Increment the time
        second += 1
        if second == 60:
            second = 0
            minute += 1
        if minute == 60:
            minute = 0
            hour += 1
        if hour == 24:
            hour = 0

        # Check if the current time matches the alarm time
        if hour == alarm_hour and minute == alarm_minute and second == alarm_second:
            print("\n⏰ Playing alarm! Time is up! ⏰")
            break
          
          
          
          


# Main program flow
print("Welcome to the Clock Program!")

# Step 1: Show the current system time dynamically
try:
    display_current_time()
except KeyboardInterrupt:
    print("\nDo you want to reset the time? (Press 'Ctrl+C' to continue)\n")

# Step 2: Ask the user to reset the time manually
hour, minute, second = reset_time()

try:
    # Display reset time dynamically
    display_reset_time(hour, minute, second)
except KeyboardInterrupt:
    print("\nNow, let's set the alarm:")

# Step 3: Set the alarm
alarm_hour = int(input("Enter alarm hour (0-23): "))
alarm_minute = int(input("Enter alarm minutes (0-59): "))
alarm_second = int(input("Enter alarm seconds (0-59): "))

# Step 4: Run the clock and check the alarm
try:
    set_and_check_alarm(alarm_hour, alarm_minute, alarm_second, hour, minute, second)
except KeyboardInterrupt:
    print("\nProgram stopped.")
