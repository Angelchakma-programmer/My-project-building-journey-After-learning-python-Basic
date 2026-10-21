
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
                "Self Respect is most Important"
            }
        
        ]
        return self_respect_qoutes
        

class Show_Users(Qoutes_Database):

    #this method using for checking len of life lesson list..
    def len_list(self):
        global Random_Qoutes
       
        #print(Random_Qoutes)
    def Dynamic_Qoutes(self):
        #Dynamic variable
        All_variabel =  [self.Life_lesson,self.self_improvment,self.Self_Respect]
        global Random_AllVariable
        Random_AllVariable = random.choice(All_variabel)#Random variable create
      
    def Show_qoutes(self):
        self.Dynamic_Qoutes()

        len_of_LifeLesson = len(self.Life_lesson()[0])
        len_of_self_improvment = len(self.self_improvment()[0])

        len_of_Self_Respect  = len(self.Self_Respect()[0])
       
        len_of_qoutes = len(self.Life_lesson()[0]) #This is len of Life_lesson varable
        Random_number_life_lesson = random.randint(1,len_of_LifeLesson)
        Random_number_Self_Respect = random.randint(1,len_of_Self_Respect)
        random_number_Self_improvment = random.randint(1,len_of_self_improvment)
    
        Ask_User = input("\n"
                         "1. Life Lesson\n"
                         "2. Self Improvment \n"
                         "3 .Self Respect\n"
                         "Enter  The Serial No Which type Qoutes do you Wnat to Read :")
        
        Color = "\033[35m"
        Reset = "\033[0m"

        if Ask_User == "1":
            Text = self.Life_lesson()[0][Random_number_life_lesson]
            Qoutes = Text
            print(Color + Qoutes + Reset)
        elif Ask_User == "2":
            Text = self.self_improvment()[0][random_number_Self_improvment]
            Qoutes = Text

            print(Color + Qoutes + Reset)
        elif Ask_User == "3":
            Text = self.Self_Respect()[0][Random_number_Self_Respect]
            Qoutes = Text

            print(Color + Qoutes + Reset)
        else:
            print("Invalid Input.. input Valid input")


      
# users.Show_qoutes()
#users.len_list()






# a = Qoutes_DB()
# a.Show_qoutes()