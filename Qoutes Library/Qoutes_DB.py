
import random
from time import sleep


class Qoutes_Database:

    def Life_lesson(self):
       
    
        life_lesson = [
            {
                1 : "Do less but..\n"
                "Do it Better.....😉",
                2 : "Sisuation will tech you \n"
                "The real meaning of life....🌸",
                3 : "Bad Days build better Days...",
                4 : "Be like water,\n"
                "Not Luxurious but Valuable for life...✍️",
                5 : "Dont't Be perfect.🙂\n"
                "Be Real...",
                6 : "Never Stop learning,\n"
                "Because life never stops teching.....",
                7 : "Dear Self..\n"
                "I Wil win, I promise..😉",
                8 : "Life is a book\n"
                "Everyday is a new page,\n"
                "Every month is a new chapter and\n"
                "Every year is a new serics.....😉"


                
            }
            ]
        return life_lesson
    def self_improvment(self):
        Self_Improve_Qoutes = [
            {
                1 : "Change is Scary, but Change is Growth...",
                2 : "Focus on improving yourself, \n"
                "Not proving yourself..🌸",
                3 : "Same Tree Different Season...\n"
                "Remember Everything is Temporary..\n"
                "So just Move on and Enjoy your Life...🫠",

                4 : " The Buddha Once Said \n"
                "Nothing is Forever,\n"
                "Except The Change..✋\n"
                "\t \t Buddha" ,
                5 : " Don't Be Same,\n"
                "Be Different.....",
                6 : "I am Working \n"
                "on myself\n"
                "for myself\n"
                "by myself...",
                7 : " No internet ?\n"
                "try:\n"
                "\t . Throw your phone Way ..\n"
                "\t . Find a spot in nature,\n"
                "\t . Then Enjoy your moment🌸.",
                8 : "Pray with Trust...",
                9 : "Simplicity is my mine..🙂",
                10 : " Do good.\n"
                "it will come back to you in \n "
                "unexpected ways...🌸"

                
    
            }
        ]
        return Self_Improve_Qoutes
    def Self_Respect(self):

        self_respect_qoutes = [
            {
                1 : " I don't respect those \n who don't Respect me\n"
                "you call it ego.\n"
                "I call it Self Respect 😏",
                2 : "Be your own Version \n"
                "to Smile...🐸",
                3 : "Ego is Important but \n"
                "Self Respect is most Important",
                4 : "Never run back to what broke you"
            }
        
        ]
        return self_respect_qoutes
        


Color = "\033[33m"
Reset = "\033[0m"
Purple = "\033[38;5;93m"
Qoutes_object = Qoutes_Database()
#Access all Qoutes len 
len_of_Life_lesson = len(Qoutes_object.Life_lesson()[0])
len_of_self_improvment = len(Qoutes_object.self_improvment()[0])
len_of_self_respect = len(Qoutes_object.Self_Respect()[0])
    
def Run_LIfe_lesson():
    Random_valueLifeLesson = random.randint(1,len_of_Life_lesson)
    Qoutes = Qoutes_object.Life_lesson()[0][Random_valueLifeLesson]
    print(Color + Qoutes + Reset )
    

def Run_Self_improvment():
    Random_value_of_Self_improvment = random.randint(1,len_of_self_respect)
    Qoutes = Qoutes_object.self_improvment()[0][Random_value_of_Self_improvment]
    print(Color + Qoutes + Reset)

def Run_Self_Respect ():
    Random_Value_Self_Respect = random.randint(1,len_of_self_respect)
    Qoutes = Qoutes_object.Self_Respect()[0][Random_Value_Self_Respect]
    print(Color + Qoutes + Reset)

class prosse(Qoutes_Database):
    def input():
         Magenta = "\033[35m"
         global User_Input
         User_Input = input(f"{Magenta}{"1. Life lesson \n"
                        "2. Self Improvment \n"
                        "3. Self Respect \n"
                        
                        "Which type Qoutes you Want Please \n"
                        "Enter Topic Serial :"} {Reset}")
         
         if User_Input == "1":
                while True :
                    Run_LIfe_lesson()
                    User_Input = input("Next Qoutes ? [Y/N]:")
                    if User_Input.strip().casefold() == "y":
                        print(Purple,"Qoutes is Loading....",Reset)
                        sleep(3)
                        continue
                    elif User_Input.strip().casefold() == "n":
                        break

                    else:
                        print("Please Input Valid input")
                        break


         elif User_Input == "2":
                 while True :
                    Run_Self_improvment()
                    User_Input = input("Next Qoutes ? [Y/N]:")
                    if User_Input.strip().casefold() == "y":
                        print(Purple,"Qoutes is Loading....",Reset)
                        sleep(3)
                        continue
                    elif User_Input.strip().casefold() == "n":
                        break

                    else:
                        print("Please Input Valid input")
                        break
         elif User_Input == "3":
                 while True :
                    Run_Self_Respect()
                    User_Input = input("Next Qoutes ? [Y/N]:")
                    if User_Input.strip().casefold() == "y":
                        print(Purple,"Qoutes is Loading....",Reset)
                        sleep(3)
                        continue
                    elif User_Input.strip().casefold() == "n":
                        break

                    else:
                        print("Please Input Valid input")
                        break
         else:
             print("Please !! Enter Valid input.")
    
