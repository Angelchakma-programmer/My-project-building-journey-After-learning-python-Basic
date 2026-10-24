import random
from Qoutes_DB import Qoutes_Database

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

print(len(life_lesson[0]))
print(life_lesson[0][5])
class Show_Users(Qoutes_Database):
    def len_list(self):
        a = len(self.Life_lesson()[0])
        print(f"This is len of life lesson list : {a}")
        

        Random_Qoutes = random.randint(1,a)
        print(Random_Qoutes)

c = Show_Users()
c.len_list()
#it's working as a list.. but what happpend if it's as a fucntion...
name = ["Angel Chakma","Lolin Chakma","hahahha Chakma"]

def Angel_Chakma():
    print(" hey it's me Angel Chakma")
def Lolin_Chakma():
    print("Hey it's me Halakko Chakma..")

def Unknon_Chakma():
    print("It's me Unknon  Chakma..")


All_Function = [Angel_Chakma,Lolin_Chakma,Unknon_Chakma]
random_name = random.choice(All_Function)
random_name()

color = "\033[34m"
text = "Hey i'm Angel...."
reset = "\033[0m"

print(color + text + reset)


def acccess ():
    print(name)
acccess()

#Ansi escape codex

Reset = "\033[0m"
Red = "\033[31m"
Green = "\033[32m"
Yellow = "\033[33m"
Blue = "\033 [34m"
Magenta = "\033[35m"
Bright_Blue = "\033[94m"
Purple = "\033[38;5;93m"

class Color_code:
    def __init__(self,Reset,Color,Text):
        self.Reset = Reset
        self.Color = Color
        self.Text = Text
    def Show_output(self):
        print(f"This is Magic of Ansi Escape Codex in python : {self.Color } {self.Text}  {self.Reset}")
        pass
Red_color = Color_code(Reset,Red,"Hello it's me Angel Chakma")
Green_Color = Color_code(Reset,Green,"Hey i'll be a Programmer!!")
yellow_color = Color_code(Reset,Yellow,"I'm a farmar.....")
Magenta_color = Color_code(Reset,Magenta,"Do you love me ?")
Bright_Blue = Color_code(Reset,Bright_Blue,"Department of Physics")
Purple = Color_code(Reset,Purple,"Mine is Self Respect !!")

Red_color.Show_output()
Green_Color.Show_output()
yellow_color.Show_output()
Magenta_color.Show_output()
Bright_Blue.Show_output()
Purple.Show_output()

user_input = input(f"{Green}{"Enter your name" }{Reset} :")
print(f"{color} Hey {user_input } How it's Going? {reset}")