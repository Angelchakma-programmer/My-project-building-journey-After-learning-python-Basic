


import random
print("Hey men , Welcome to Number Guessing Game !")
Maxn = 10
match_number = random.randint(1,Maxn)
guess_count = 5

print("Guess number must be 1 to %d " % Maxn)
ueser_guess = None

while ueser_guess != match_number:
        
        print(f"Your Chance is : {guess_count}")
        # print("Your turn !")
        ueser_guess = int(input("Enter your Guess Number :"))
        if ueser_guess == match_number:
            print("Yes, bro you are won")
       
        elif ueser_guess > match_number:
            print("Too High, Enter low Number :")
        elif ueser_guess < match_number:
            print("Too low, Enter high Number :")
        guess_count = guess_count - 1
        
        if guess_count ==0 :
            print("Your coundown is completed. so you can try Aggin")
            print("Sorry you're not Found match Number")
            break

    

    



# import random
# print("Hey men , Welcome to Number Guessing Game !")
# Maxn = 10
# match_number = random.randint(1,Maxn)
# guess_count = 5

# print("Guess number must be 1 to %d " % Maxn)
# ueser_guess = None

# while ueser_guess != match_number:
        
#         print(f"Your Chance is : {guess_count}")
#         # print("Your turn !")
#         ueser_guess = int(input("Enter your Guess Number :"))
#         if ueser_guess == match_number:
#             print("Yes, bro you are won")
       
#         elif ueser_guess > match_number:
#             print("Too High, Enter low Number :")
#         elif ueser_guess < match_number:
#             print("Too low, Enter high Number :")
#         guess_count = guess_count - 1
        
#         if guess_count ==0 :
#             print("Your coundown is completed. so you can try Aggin")
#             print("Sorry you're not Found match Number")
#             break

    

    
