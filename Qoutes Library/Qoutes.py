import Qoutes_DB
import time
a = Qoutes_DB.Show_Users()

print("Welcome To our Qoutes Library.....🌸")

while True:

    User_Input = input("Do you Want to Explore Qoutes ? [Y/N] :")
    if User_Input.strip().casefold() == "y":
        print("Let's dive in...")
        a.Show_qoutes()
        while True:
            
            User_Input = input("\nNext Qoutes ? [Y/N] :")
            if User_Input.strip().casefold() == "y":
                print("Qoutes is loading......")
                time.sleep(3)
                # a.Dynamic_Qoutes()
                a.Show_qoutes()
                #WE need right now... call different method...
            else:
                break
        
    elif User_Input.strip().casefold() == "n":
        print("It ok . Next time  you can try to read some Qoutes..")
        break
        
    else:  
        print("Invalid Input !! Please try Valid input..🌸")


