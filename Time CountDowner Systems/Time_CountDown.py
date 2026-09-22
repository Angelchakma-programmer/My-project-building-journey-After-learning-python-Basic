

#This project Created by Angel Chakma.
import time
from time import strftime

print("Welcome to Time CounDown System!")

# Time_set = input("Enter your Time and Get Set [H:M:S] : ")
user_time_set = int(input("Enter your Time \n"
                          "Must be in Second :"))

#time = user_time_set
times = user_time_set
sleep_time = -1

while user_time_set != sleep_time:
    #print("It's me Angel Chakma.....")
    a = time.sleep(1)
    print(f'\r Countdown : {user_time_set:02d} s',end= '')
    
    user_time_set -= 1
    if sleep_time == user_time_set:
        print(f"\nYour time was :{times}s")
        print("Time is Excuted !")
        break





