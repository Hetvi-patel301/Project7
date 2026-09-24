from datetime import datetime
import time
def current_datetime():
    current = datetime.now()
    print("Current Date and Time:",current)
def datetime_difference():
    date1 = input("Enter First Date(YYYY-MM-DD):")
    date2 = input("Enter Second Date(YYYY-MM-DD):")
    dt1 = datetime.strptime(date1,"%Y-%m-%d")
    dt2 = datetime.strptime(date2,"%Y-%m-%d")
    diff = abs (dt2 - dt1)
    print("Difference:",diff.days,"days")
def custom_date():
    date = input("Enter date (YYYY-MM-DD):")
    d = datetime.strptime(date, "%Y-%m-%d")
    print("Custom Format:", d.strftime("%d-%m-%Y"))
def stopwatch():
     input("Press Enter to start stopwatch")
     start =  time.time()
     input("Press Enter to stop stopwatch")
     end = time.time()
     elapsed = end - start
     print("Elapsed Time:",round(elapsed,2),"seconds")
def countdown():
    s = int(input("Enter Countdown time in seconds:"))
    while s>0:
        print("Time remaining:",s,"seconds")
        time.sleep(1)
        s -=1
    print("Time's up!") 
