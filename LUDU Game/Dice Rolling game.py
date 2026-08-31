
#This is Dice rolling game.

import random
Roll_number = random.randint(1,6)
print("Welcome To our Dice Rolling game.")
print(f"Your Roll number is : {Roll_number}.")

while True:
    
    Roll_number = random.randint(1,6)
    
    
    User_input = input("Do you wnat To Role Again. [y/n]")
    if User_input.lower().upper() == "Y":
        print(f"Your Roll number is : {Roll_number}.")
        continue

    elif User_input.lower().upper() == "N":
        print("The game is ended.")
        break
    else:
        print("Invalid input try again.")




#Finally the game is Completed by Angel Chakma.




    

