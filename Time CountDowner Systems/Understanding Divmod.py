

#This is understanding divmod in python language.
Time_Input = int(input("Enter your time \n"
                       "Must be is Seconds :"))

Time  = Time_Input
def Time_Convert(): 
    All_Seconds = Time %(24 * 3600)
    Hours = All_Seconds // 3600
    All_Seconds = All_Seconds % 3600
     
    Minute = All_Seconds // 60

    Seconds = All_Seconds % 60
    print(f"The Time is : {Hours}H :{Minute}M :{Seconds}S")

Time_Convert()