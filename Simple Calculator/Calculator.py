 

def Calculator():
        First_number = float(input("Enter Your first Number :"))
        Second_number = float(input("Enter your Second Number :"))
        Oparators = ["+","-","*","/"]
        print(Oparators)
        User_select_oparator = input("Enter your Oparators :")
        if User_select_oparator in Oparators:
            if User_select_oparator == "+":
                sum = First_number + Second_number
                print(f"Your Sum Number is : {sum} ")

            elif User_select_oparator == "-" :
                subtraction = First_number - Second_number
                print(f"Your Subtraction Number is : {subtraction}")
            elif User_select_oparator == "*" :
                Multification = First_number * Second_number
                print(f"Your Multifications Number is : {Multification} ")
            elif User_select_oparator == "/" :
                Division = First_number / Second_number
                print(f"Your Division Number is : {Division} ")
            
                

            pass
        else:
            print("Invalid Oparators . Syntex error !")

   
while True:
    Calculator()
   
    user_input = input("Do you want to Exit Calculator ? [Yes/No]")
    if user_input.strip().casefold() == "yes":
        print("ok This Apps Is Closed.")
        break
    else:
        continue