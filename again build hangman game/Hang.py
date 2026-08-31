


#Again buiding hangman game with Sudo code and plan.
InGame_SecreatWord = "Rangamati"
User_Chances = 10
Game_Finished = False
Word_Box = []

while not Game_Finished:
    for Later in InGame_SecreatWord:
        if Later.lower() in Word_Box:
            print(Later, end= " ")
        else:
            print("_",end= "")
        
    User_input = input(f"Yor chances is : {User_Chances} . Enter your guess later : ")
    Word_Box.append(User_input.lower())
    if User_input not in InGame_SecreatWord:
        User_Chances -= 1
        if User_Chances == 0:
            print("Your chances is over.")
            break
    
    Game_Finished = True
    for Later in InGame_SecreatWord:
        if Later.lower() not in Word_Box:
            Game_Finished = False



   

if Game_Finished:
    print(f"Congratulations you won the game.The Secreat word is : {InGame_SecreatWord}")
else:
    print("You lose the game.")

    