import Qoutes_DB
import time
a = Qoutes_DB.Qoutes_Database()

print("Welcome To our Qoutes Library.....🌸")

while True:
    User_Input = input("Do you Want to Explore Qoutes ? [Y/N] :")
    if User_Input.strip().casefold() == "y":
      a.Show_qoutes()
     
        
        
    elif User_Input.strip().casefold() == "n":
        print("It ok . Next time  you can try to read some Qoutes..")
        break
    else:
        print("Invalid Input !! Please try Valid input..🌸")


