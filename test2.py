# import time
# import sys
# import datetime


# # Function to display the current time dynamically
# def display_current_time():
#     print("\nCurrent time:")
#     while True:
#         now = datetime.datetime.now()
#         print(now.strftime("%H:%M:%S"), end="\r")
#         time.sleep(1)


# # Function to display and update the manually reset time dynamically
# def display_reset_time(hour, minute, second):
#     print("\nUpdated time after resetting:")
#     while True:
#         print(f"{hour:02}:{minute:02}:{second:02}", end="\r")
#         time.sleep(1)
#         # Increment the time
#         second += 1
#         if second == 60:
#             second = 0
#             minute += 1
#         if minute == 60:
#             minute = 0
#             hour += 1
#         if hour == 24:
#             hour = 0


  

# # Function to reset the time manually
# def reset_time():
#     print("\nReset the time manually:")
#     try:
#         new_hour = int(input("Enter hour (0-23): "))
#         new_minute = int(input("Enter minute (0-59): "))
#         new_second = int(input("Enter second (0-59): "))
        
#         if 0 <= new_hour < 24 and 0 <= new_minute < 60 and 0 <= new_second < 60:
#             return new_hour, new_minute, new_second
#         else:
#             print("Invalid time entered. Please try again.")
#             return reset_time()  # Retry on invalid input
#     except ValueError:
#         print("Please enter valid numeric values.")
#         return reset_time()  # Retry on invalid input
      

        


# # Function to set and check the alarm
# def set_and_check_alarm(alarm_hour, alarm_minute, alarm_second, hour, minute, second):
#     print("\nClock is running:")
#     while True:
#         print(f"{hour:02}:{minute:02}:{second:02}", end="\r")
#         time.sleep(1)
#         # Increment the time
#         second += 1
#         if second == 60:
#             second = 0
#             minute += 1
#         if minute == 60:
#             minute = 0
#             hour += 1
#         if hour == 24:
#             hour = 0

#         # Check if the current time matches the alarm time
#         if hour == alarm_hour and minute == alarm_minute and second == alarm_second:
#             print("\n⏰ Playing alarm! Time is up! ⏰")
#             break
          
          
          
          


# # Main program flow
# print("Welcome to the Clock Program!")

# # Step 1: Show the current system time dynamically
# try:
#     display_current_time()
# except KeyboardInterrupt:
#     print("\nDo you want to reset the time? (Press 'Ctrl+C' to continue)\n")

# # Step 2: Ask the user to reset the time manually
# hour, minute, second = reset_time()

# try:
#     # Display reset time dynamically
#     display_reset_time(hour, minute, second)
# except KeyboardInterrupt:
#     print("\nNow, let's set the alarm:")

# # Step 3: Set the alarm
# alarm_hour = int(input("Enter alarm hour (0-23): "))
# alarm_minute = int(input("Enter alarm minutes (0-59): "))
# alarm_second = int(input("Enter alarm seconds (0-59): "))

# # Step 4: Run the clock and check the alarm
# try:
#     set_and_check_alarm(alarm_hour, alarm_minute, alarm_second, hour, minute, second)
# except KeyboardInterrupt:
#     print("\nProgram stopped.")



import time
import datetime

# Global variable to control pause state
is_paused = False
paused_time = None  # Variable to store the time when paused

# Function to pause and resume the clock
def pause_clock():
    global is_paused, paused_time
    is_paused = not is_paused
    now = datetime.datetime.now()
    formatted_time = now.strftime("%I:%M:%S %p") if time_format == 12 else now.strftime("%H:%M:%S")
    state = "paused" if is_paused else "resumed"
    if is_paused:
        paused_time = now
        print(f"\nClock has been {state} at {formatted_time}.")
    else:
        print(f"\nClock has been {state} at {formatted_time}.")
        print(f"\nCurrent time: {formatted_time}")

# Function to display the current time dynamically
def display_current_time(time_format):
    print("\nCurrent time:")
    try:
        while True:
            now = datetime.datetime.now()
            formatted_time = now.strftime("%I:%M:%S %p") if time_format == 12 else now.strftime("%H:%M:%S")
            if is_paused:
                paused_display = paused_time.strftime("%I:%M:%S %p") if time_format == 12 else paused_time.strftime("%H:%M:%S")
                print(f"[PAUSED] {paused_display}", end="\r")
            else:
                print(formatted_time, end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nReturning to menu...")

# Function to display and update the manually reset time dynamically
def display_reset_time(hour, minute, second, time_format):
    print("\nUpdated time after resetting:")
    try:
        while True:
            display_hour = hour % 12 or 12 if time_format == 12 else hour
            suffix = "AM" if hour < 12 else "PM"
            formatted_time = f"{display_hour:02}:{minute:02}:{second:02} {suffix}" if time_format == 12 else f"{hour:02}:{minute:02}:{second:02}"
            if is_paused:
                print(f"[PAUSED] {formatted_time}", end="\r")
            else:
                print(formatted_time, end="\r")
                second += 1
                if second == 60:
                    second, minute = 0, minute + 1
                if minute == 60:
                    minute, hour = 0, hour + 1
                if hour == 24:
                    hour = 0
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nReturning to menu...")

# Menu function
def menu():
    print("\nMenu:")
    print("1. Show the current time")
    print("2. Reset the time manually")
    print("3. Set an alarm")
    print("4. Pause/Resume Clock")
    print("5. Exit")
    return input("Enter your choice: ")

# Main program flow
print("Welcome to the Clock Program!")
time_format = 24
hour, minute, second = None, None, None

while True:
    choice = menu()
    if choice == "1":
        display_current_time(time_format)
    elif choice == "2":
        hour, minute, second = 12, 0, 0  # Simplified reset for demo
        display_reset_time(hour, minute, second, time_format)
    elif choice == "3":
        print("Alarm feature placeholder.")
    elif choice == "4":
        pause_clock()
    elif choice == "5":
        print("\nExiting program. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please try again.")
