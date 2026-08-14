

import random

Guess_number = random.randrange(1,10)
print(Guess_number)
user_input = int(input("Enter your guess number between 1 to 10: "))


if user_input > Guess_number:
    print(Guess_number)
    print("Your guess is too high")
elif user_input < Guess_number:
    print(Guess_number)
    print("Your guess number is too low")
else:
    print(Guess_number)
    print("Congratulations , you're Won, cauese your guess number is correct")