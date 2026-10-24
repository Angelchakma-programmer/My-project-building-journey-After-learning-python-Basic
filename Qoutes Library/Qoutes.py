

import Qoutes_DB
import time
#Colors
Blue  = "\033[34m"
Reset = "\033[0m"
red = "\033[31m"
Yellow = "\033[33m"

access = Qoutes_DB.prosse
print(Blue,"Welcome to Qoutes Library !!",Reset)

user_input = input(f"{Yellow}{"Do you Want to Read Qoutes ? [Y/N] :"} {Reset}" )
if user_input.strip().casefold() == "y":
        
    Done = False
    while not Done:
        access.input()
    
        user_input = input(f"{red} {"Quit Library ? [Y/N]"}{Reset}")
        if user_input.strip().casefold() == "y":
            Done = True
            print("Library is Closed !")
            if Done :
                break

        elif user_input.strip().casefold() == "N":
            continue
        else:
            print("Please Enter Vaild input!!")
            
elif user_input.strip().casefold() == "n":
    print("The Library is Clossed !")
else:
    print("Invalid input.. try with Valid input..")

    

