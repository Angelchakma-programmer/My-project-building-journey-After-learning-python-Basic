
import random


class Qoutes_Database:

    def Life_lesson(self):
        global life_lesson
    
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
    def self_improvment():
        Self_Improve_Qoutes = [
            {
                1 : "Change is Scary, but Change is Growth...",
                2 : "Focus on improving yourself, \n"
                "Not proving yourself..🌸",
                3 : "Same Tree Different Season...\n"
                "Remember Everything is Temporary..\n"
                "So just Move on and Enjoy your Life...🫠",

                4 : " The Buddha  Said \n"
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
    def Self_Respect():

        self_respect_qoutes = [
            {
                1 : " I don't respect those \n who don't Respect me\n"
                "you call it ego.\n"
                "I call it Self Respect 😏",
                2 : "Be your own Version \n"
                "to Smile...🐸"
            }
        ]
        pass

class Show_Users(Qoutes_Database):

    
    
    #this method using for checking len of life lesson list..
    def len_list(self):
        global Random_Qoutes
       
        #print(Random_Qoutes)
      

    
    def Show_qoutes(self):
        a = len(self.Life_lesson()[0])
        #print(a)

        Random_Qoutes = random.randint(1,a)
        #user_inut = input("Enter you Mood :")
        
        a = self.Life_lesson()
        print(f"{"\033[33m"}  {life_lesson[0][Random_Qoutes]}  {"\033[0m"}")



# users = Show_Users()
# users.Show_qoutes()
#users.len_list()






# a = Qoutes_DB()
# a.Show_qoutes()