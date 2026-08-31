#The game is not created yet. but i'll create in this night.
# a = input("Enter your name : ")
# print(f"Hey good morning {a}, have a nice day !")

#This is my 5th attemp::
#This is main component of this game.
Secreat_word = "Angel Chakma"
Add_Word = []
Finish_game = False

chances = 10
while not Finish_game:#Jokon finish game is True.
    for word in Secreat_word:#jokon word er betore secreat _word ta takbe.
        if word.lower() in Add_Word: #Jodi word e taka later ti add word e take taile.
            print(word, end= " ") #print Korbe je owrd ta r , laste space
        else:
            print("_",end= "") #jodi na take taile " _ " print kore dekabe.
            #At this point it's fine.
    
    user_guess = input(f"Your chances is : {chances} . Enter you guess word :") # ekane user teke input nibo and Chances ta o dekabo.
    Add_Word.append(user_guess.lower()) #ekane user input ke add_word e append kore dibo.
    if user_guess.lower() not in Secreat_word.lower(): #jodi user_ges secreat word e na take.
        chances -= 1 #chances take komiye dao
        if chances == 0: # Jodi chances komte komte  zero hoi tahole loop ta break kore dao.
            break

    Finish_game = True #Finish game ta ke true kore dissi

    for word in Secreat_word: #jokke word to secreat word ot tebo.
        if word.lower() not in Add_Word: #jodi word to add_word tot 9 tai
            Finish_game = False #sekke finish game ore false bane de.
    
if Finish_game:
    print(f"Congratests you won the game.The secrect word is : {Secreat_word}")
else:
    print('You lose the game and try again.')


    

  