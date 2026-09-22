

#This  is testing String formating in time countdown Systems!
import time
print("Time Must be in Second ....")
User_time_input = int(input("Enter you time :"))

for times in range(User_time_input):
    time.sleep(1)
    print(f" \r Countdown: {User_time_input:02d} s", end= " ")
    User_time_input -=1
    

   
print("Tesing is Completed . are you got it?")