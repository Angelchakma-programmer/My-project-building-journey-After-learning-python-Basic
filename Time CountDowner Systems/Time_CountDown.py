

#Re - building my Time countDown project. and it's me Angel Chakma.
#thaking time input from users.

import time
Time_inputFrom_users = int(input("Enter your time \n"
                      "Time Must be Seconds :"))
Seconds = Time_inputFrom_users
def Convert_time():
    Time = Seconds % (24 * 3600)
    global Hours
    Hours = Time // 3600

    Time = Time % 3600
    global Miniute
    Miniute = Time // 60
    Time = Time % 60
    global second
    second = Time
    
   
while True:
    Convert_time()
    
    print(f" \r time CountDown is :  {Hours}H: {Miniute}M: {second}s  ", end= " \r")
    time.sleep(1)

    Seconds -= 1
    if Time_inputFrom_users == 0:
        print("Time is Cxcuted !")
        break


    



