import time

def display_custom_time(hour, minute, second):
    while True:
        # Format and display the current time
        print(f"{hour:02}:{minute:02}:{second:02}", end="\r")
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

# Set your initial time here
initial_hour = 15
initial_minute = 30
initial_second = 0

try:
    display_custom_time(initial_hour, initial_minute, initial_second)
except KeyboardInterrupt:
    print("\nProgram stopped.")