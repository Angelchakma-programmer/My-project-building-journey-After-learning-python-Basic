



#The project name is Celsius to fahrenheit
#And the project created by Angel Chakma

print("This is Temerature Converter!\n"
      "Celsius to Fahrenheit")



def Celsius_to_Fahrenheit():
    user_Temperature_input = input("Enter your Celsius Temperature: ")
    Celsius_temperature = float(user_Temperature_input)
    fahrenheit_temperature = (Celsius_temperature *(9/5))+ 32
    print(f"The {user_Temperature_input} Celsuis quals to {fahrenheit_temperature} Fahrenheit.")
    print("You're will be a Best scientist .")

    
def Fahrenheit_to_Celsius():
    print("Welcome to Fahrenheit to Celsius Temperature Converter !")
    Fahrenheit_Temperature_input = float(input("Enter your Fahrenheite Temperature : "))
    celsius = (Fahrenheit_Temperature_input - 32) * 5/9
    print(f"The {Fahrenheit_Temperature_input} temperature is {celsius} in Celsius Temperature .")

user_input = input("Which temperature Do you wnat to Covert? [C /F]:" )
if user_input.upper().strip() == "C":
    
    Celsius_to_Fahrenheit()
elif user_input.upper().strip() == "F":
    Fahrenheit_to_Celsius()

else:
    print("Invalid Input !")
    

    
