
#This project is BMI Test . and also it's Created by Angel Chakma.

print("Welcome to BMI Test !")
def Eroor_handale():
    print("Keep trying .....")
    try:
        user_name = input("Enter your name :")
        User_Weight = float(input("Enter your Weight in [Kg] :"))
        User_height = float(input("Enter you Height in [Meter] :"))
        if User_height and User_Weight  == float(0) and User_height or User_Weight == float(0):
            print("Please Input valid input! try again .")

        else:


            BMI = User_Weight / (User_height **2)

            print(f"Your name is : {user_name}\n"
                f"Your BMI is : {round(BMI,2)}")


            if BMI < 18.5:
                print(f"Mr:{user_name} You're too Underweight! Try to eat healthy food.")
            elif  (18.5 <= BMI <= 24.9):
                print(f"Mr: {user_name} you're normal !. your helth is good.")

            elif (25.0 <=  BMI <= 29.0):
                print(f"Mr: {user_name} you're too Overweight!. Try to eat normal.")
            else:
                print("Invalid BMI!")

    except:
        print("Hi i'm wating for you. You inputed Invalid Info .")

while True:
    Eroor_handale()
    user_input = input( "Do you want to Exit ?[Y/N]")
    if user_input.strip().casefold() == "y":
        print("This program is Exit .")
        break
    else:
        continue