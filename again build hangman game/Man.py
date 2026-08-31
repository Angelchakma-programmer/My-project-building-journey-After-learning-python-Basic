

Chances = 10
Secreat_Number = "a"
Store_Number = []
Finish_gmae = False

while not Finish_gmae:
    for Numbers in Secreat_Number:
        if Numbers in Store_Number:
            print(Numbers, end= " ")
        else:
            print("_ ", end= "")
        
    Input_number = input(f"Your Chances is : {Chances}. Enter your guess number :")
    Store_Number.append(Input_number.lower())
    if Secreat_Number  not in Store_Number:
        Chances -= 1
        if Chances == 0 :
            print("Your Chances is out.")
            break
    Finish_gmae = True
    for Numbers in Secreat_Number:
        if Numbers not in Store_Number:
            Finish_gmae = False

if Finish_gmae:
    print(f"congrats you won the game. the Secreat numbers is : {Secreat_Number}")
else:
    print("You lose the game. Please try again.")

