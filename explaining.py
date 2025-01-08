
import time
import sys
import datetime

#((((Modules Imported:)))
        #time: Provides functions to manage time, like sleep() which pauses the program.
        #sys: Used here to interact with the system's standard output (your console).
        #datetime: Allows working with dates and times.
        
        
while True:
    now = datetime.datetime.now() 
    #(((What it does: Gets the current date and time, down to the exact second.)))
    print(now.strftime("%H:%M:%S"), end="\r")
    #(((now.strftime("%H:%M:%S"): Formats the current time (now) into a string showing only hours, minutes, and seconds in 24-hour format (e.g., 16:30:10).))) 
    #(((end="\r": Ensures that each new time overwrites the previous one on the same line instead of creating a new line in the console.)))
    sys.stdout.flush() 
    #(((What it does: Forces the program to immediately show the output in the console (overwriting the previous time). Without this, the display might not update smoothly.)))
    time.sleep(.4) 
    #(((What it does: Pauses the program for 0.4 seconds before running the next iteration of the loop. This creates a slight delay between each update of the displayed time.)))






    