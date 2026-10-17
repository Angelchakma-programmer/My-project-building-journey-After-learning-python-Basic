import random
from Qoutes_DB import Qoutes_Database

# life_lesson = [
#             {
#                 1 : "Do less but..\n"
#                 "Do it Better.....😉",
#                 2 : "Sisuation will tech you \n"
#                 "The real meaning of life....🌸",
#                 3 : "Bad Days build better Days...",
#                 4 : "Be like water,\n"
#                 "Not Luxurious but Valuable for life...✍️",
#                 5 : "Dont't Be perfect.🙂\n"
#                 "Be Real...",
#                 6 : "Never Stop learning,\n"
#                 "Because life never stops teching.....",
#                 7 : "Dear Self..\n"
#                 "I Wil win, I promise..😉",
#                 8 : "Life is a book\n"
#                 "Everyday is a new page,\n"
#                 "Every month is a new chapter and\n"
#                 "Every year is a new serics.....😉"


                
#             }
#             ]

# print(len(life_lesson[0]))
# print(life_lesson[0][5])
class Show_Users(Qoutes_Database):
    def len_list(self):
        a = len(self.Life_lesson()[0])
        print(f"This is len of life lesson list : {a}")
        

        Random_Qoutes = random.randint(1,a)
        print(Random_Qoutes)

c = Show_Users()
c.len_list()