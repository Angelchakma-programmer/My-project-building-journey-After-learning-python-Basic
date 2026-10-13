


#This is the latest re building time CountDowner Systems.
#It's me Angel Chakma..........
import time
try:
        
    Time_Input = int(input("Enter your time \n"
                        "Must be in Seconds :"))
    if Time_Input <= 0:
        print("Please input the time less then 0.")
    else:

        Time  = Time_Input
        def Time_Convert(): 
            All_Seconds = Time %(24 * 3600)
            global Hours
            Hours = All_Seconds // 3600
            All_Seconds = All_Seconds % 3600
            global Minute
            Minute = All_Seconds // 60
            global Seconds
            Seconds = All_Seconds % 60

            #This is convert Seconds to Hours, Miniute,Seconds.
        while True:
            Time_Convert()
            print(f" \rCountdown is : {Hours:02d}H : {Minute:02d}M : {Seconds:02d}S",end= " ")
            time.sleep(1)
            
            Time -= 1
            if Time <= -1:
                print("\nTime is Excuted !")
                
                break
        
except ValueError:
    print("Please Input Valid input....")
