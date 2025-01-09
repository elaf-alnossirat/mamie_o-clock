
import time
import datetime


# Function to display the current time dynamically
def display_current_time(time_format):
    print("\nCurrent time:")
    while True:
        now = datetime.datetime.now()
        if time_format == 12:
            formatted_time = now.strftime("%I:%M:%S %p")  # 12-hour format
        else:
            formatted_time = now.strftime("%H:%M:%S")  # 24-hour format
        print(formatted_time, end="\r")
        time.sleep(1)


# Function to display and update the manually reset time dynamically
def display_reset_time(hour, minute, second, time_format):
    print("\nUpdated time after resetting:")
    while True:
        if time_format == 12:
            suffix = "AM" if hour < 12 else "PM"
            display_hour = hour % 12 or 12  # Convert to 12-hour format
            print(f"{display_hour:02}:{minute:02}:{second:02} {suffix}", end="\r")
        else:
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
def set_and_check_alarm(hour, minute, second, alarm_hour, alarm_minute, alarm_second, time_format):
    print("\nClock is running:")
    while True:
        if time_format == 12:
            suffix = "AM" if hour < 12 else "PM"
            display_hour = hour % 12 or 12  # Convert to 12-hour format
            print(f"{display_hour:02}:{minute:02}:{second:02} {suffix}", end="\r")
        else:
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


# Function to choose the time display format
def choose_time_format():
    print("\nChoose the time display format:")
    print("1. 24-hour format (default)")
    print("2. 12-hour format (AM/PM)")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "2":
        return 12
    else:
        return 24


# Menu function
def menu():
    print("\nMenu:")
    print("1. Show the current time")
    print("2. Reset the time manually")
    print("3. Set an alarm")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice


# Main program flow
print("Welcome to the Clock Program!")

# Choose the time display format
time_format = choose_time_format()

hour, minute, second = None, None, None  # Initialize reset time variables

while True:
    choice = menu()
    if choice == "1":
        # Show the current system time dynamically
        try:
            display_current_time(time_format)
        except KeyboardInterrupt:
            print("\nExiting current time display...")
    elif choice == "2":
        # Reset the time manually
        hour, minute, second = reset_time()
        try:
            display_reset_time(hour, minute, second, time_format)
        except KeyboardInterrupt:
            print("\nExiting reset time display...")
    elif choice == "3":
        # Set the alarm
        if hour is None or minute is None or second is None:
            # If the time has not been reset, use the current system time
            now = datetime.datetime.now()
            hour, minute, second = now.hour, now.minute, now.second

        print("\nSet the alarm:")
        try:
            alarm_hour = int(input("Enter alarm hour (0-23): "))
            alarm_minute = int(input("Enter alarm minutes (0-59): "))
            alarm_second = int(input("Enter alarm seconds (0-59): "))

            # Run the clock and check the alarm
            set_and_check_alarm(hour, minute, second, alarm_hour, alarm_minute, alarm_second, time_format)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except KeyboardInterrupt:
            print("\nExiting alarm check...")
    elif choice == "4":
        print("\nExiting program. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please try again.")
