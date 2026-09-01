

#This is my last time build Hangman Game.

The_Secreat_word = "Phyics"
Chances = 10
Finish_Game = False
Store_Secreat_word = []

while not Finish_Game:
    for Guess_word in The_Secreat_word:
        if Guess_word.lower() in Store_Secreat_word:
            print(Guess_word, end= " ")
            
        else:
            print("_",end= "")
 
    User_Guess = input(f"Your Chances is : {Chances}. Enter your Guess word : " )

    Store_Secreat_word.append(User_Guess)
    if User_Guess.lower() not in The_Secreat_word :
        Chances -= 1
        if Chances == 0:
            print(f"Your Chances is Out. try Again !")
            break

    Finish_Game = True
    for Guess_word in The_Secreat_word:
       if Guess_word.lower() not in  Store_Secreat_word:
           Finish_Game = False
if Finish_Game:
    print(f"Congratulations You won the game . ")
    print(f"The Secreat Word is : {The_Secreat_word}")
else:
    print("You losse The Game.")
