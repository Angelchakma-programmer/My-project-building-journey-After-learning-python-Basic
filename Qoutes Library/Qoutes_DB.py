
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
                "Every year is a new serics.....😉",
                9 : "Sometimes it's better to be alone.",
                10 : " Real Connection starts with honest Conections...",
                11 : "Being gentle with yourself\n"
                "is part of growing...",
                12 : "God, i am tired, but i trust you..",
                13 : "Not everyone deserves \n"
                "to see all your sides..",
                14 : " Past is past, Focus on your Future.",
                15 : "Small circle,private life,happy heart\n"
                "clear mind and peaceful life.",
                16 : " Keep going, your time will come..",
                17 : "Life is 10% what happens to you \n"
                "and 90%  how you react to it..",
                18 : "Learn from yesterday, live for today,\n"
                "And hope for Tomorrow..",
                19 : "It's not how many times you fall, \n"
                "but how many times you get up that counts..",
                20 : "Happniness is not about getting what you want,\n"
                "it's about wanting what you have..",
                21 : "If you want to change the world,\n"
                "start by changing yourself..",
                22 : "The biggest risk in life is not taking any risk..",
                23 : "Forgive others,but never forget what you learned from them..",
                24 : "Your life is your story,\n"
                "and the adventure ahead of you is the journey \n"
                "to fulfill your own purpose..",
                25 : "  Tough times never last ,but tough people do..",
                26 : "Don't compare your life to others.\n"
                "The sun and moon don't compare,\n"
                "They shine when it's their time...",
                27 : "You can by a clock, but not time...",
                28 : "Life is mad of samall moments.Learn to cheirsh them..",
                29 : " If you can't fly then run, if you can't run then walk,\n"
                "if you can't walk then crow!\n "
                "but whatever you do you have to keep moving forward..",
                30 : "Peace comes from within. \n"
                "Do not seek it withour...",
                31 : "Life is like a mirror,\n"
                "it will smile at yu if you smile at it.."




                
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
                "unexpected ways...🌸",
                11 : "Wake up 1 hour earilier than usual.\n"
                "No phone for first 30 mins...",
                12 : " No social media for 24 hours. Notice how much time you save..",
                13 : "Write down 3 clear goals.\n"
                "1 for this month\n"
                "1 for 6 months,\n"
                "1 for year...",
                14 : " Watch a 30-min tutorial or read about a skill you want to learn",
                15 : "Do 30-mins Exercise,walk or workout. \n"
                "No excuses..",
                16 : "Write 5 Things you are grateful for .\n"
                "It changes your Mindset instantly...",
                17 : "Clear your room,desk, and phone.\n"
                "Clean space = clear mind.....",
                18 : "For 24 hours, don't complain about anything.\n"
                "just find solutions...",
                19 : " Read 20 page of a self-help or knowledge book....",
                20 : "Start a conversation with a stranger or someone you admire.\n"
                "Build Confidence....",
                21 : "Track every taka you spend today.\n"
                "Learn where your money goes.....",
                22 : " Say no to al least 1 thing \n"
                "That wastes your time or energy...",
                23 : "Forgive one person who hurt you.\n"
                "Not for them,for your peace..",
                24 : "Write a letter to yourself 1 year from now.\n"
                "What do you want to become ?",
                25 : "Do 1% better every day. Don't try to be perfect...",
                26 : 'Progress begins\n'
                'when excuses end.',
                27 : 'Build habits\n'
                'that make your future easier.',
                28 : 'Small steps repeated every day\n'
                'create lasting results.',
                29 : 'Discipline helps you act\n'
                'even when motivation is low.',
                30 : 'Invest in skills\n'
                'that will benefit you tomorrow.',
                31 : 'Your future improves\n'
                'with every useful choice you make today.',
                32 : 'Learn from mistakes,\n'
                'then give yourself room to improve.',
                33 : 'Consistency turns intention\n'
                'into real progress.',
                34 : 'Focus on becoming better,\n'
                'not on appearing perfect.',
                35 : 'Read, practice, and reflect.\n'
                'Growth needs all three.',
                36 : 'Use your time with purpose,\n'
                'because it cannot be replaced.',
                37 : 'Replace worry with preparation\n'
                'and uncertainty with action.',
                38 : 'Success grows from patience,\n'
                'practice, and persistence.',
                39 : 'Improve your environment\n'
                'so good habits become easier.',
                40 : 'Do the difficult task first,\n'
                'then let the rest feel lighter.',
                41 : 'Your energy is valuable.\n'
                'Spend it on meaningful progress.',
                42 : 'Rest when needed,\n'
                'but do not let rest become giving up.',
                43 : 'Review your progress regularly\n'
                'and adjust your direction.',
                44 : 'Become a little wiser each day\n'
                'by staying curious and open.',
                45 : 'Keep moving forward.\n'
                'A steady effort creates real change.'

                
    
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
                4 : "Never run back to what broke you",
                5 : 'Choosing yourself\n'
                'is not selfish.',
                6 : 'You teach people how to treat you\n'
                'by what you accept.',
                7 : 'Walk away from places\n'
                'where your worth is questioned.',
                8 : 'Self respect means setting boundaries\n'
                'without feeling guilty.',
                9 : 'Do not shrink yourself\n'
                'to make others comfortable.',
                10 : 'Your peace is more important\n'
                'than other people approval.',
                11 : 'Respect yourself enough\n'
                'to stop begging for attention.',
                12 : 'You do not need permission\n'
                'to protect your dignity.',
                13 : 'Never stay where\n'
                'your presence is taken for granted.',
                14 : 'Self respect starts\n'
                'when you stop accepting disrespect.',
                15 : 'You can be kind\n'
                'and still have strong boundaries.',
                16 : 'Choose people\n'
                'who value your time and character.',
                17 : 'Losing yourself\n'
                'to keep someone else is not love.',
                18 : 'Know when to speak,\n'
                'and know when to walk away.',
                19 : 'Your standards determine\n'
                'the life you allow yourself to live.',
                20 : 'Protecting your self worth\n'
                'is an act of courage.',
                21 : 'Respecting yourself\n'
                'is the beginning of lasting change.',
                22 : 'Never apologize\n'
                'for protecting your peace.',
                23 : 'Your boundaries\n'
                'are not a request for permission.',
                24 : 'Leave quietly\n'
                'when your presence is not valued.',
                25 : 'You deserve respect\n'
                'without having to prove your worth.',
                26 : 'Stand up for yourself,\n'
                'even when your voice shakes.',
                27 : 'A strong sense of self\n'
                'is stronger than others opinions.',
                28 : 'Do not trade your dignity\n'
                'for temporary approval.',
                29 : 'Choose growth\n'
                'over situations that diminish you.',
                30 : 'Your self respect should never\n'
                'depend on someone else.',
                31 : 'Stop explaining yourself\n'
                'to people committed to misunderstanding you.',
                32 : 'Being alone is better\n'
                'than accepting less than you deserve.',
                33 : 'You owe no one access\n'
                'to your heart or your time.',
                34 : 'Respect is something you give\n'
                'and something you require.',
                35 : 'The right people will never ask you\n'
                'to abandon your standards.',
                36 : 'Protect your energy\n'
                'as carefully as your dreams.',
                37 : 'Silence can be\n'
                'a powerful form of self respect.',
                38 : 'Know your worth,\n'
                'and let your actions show that you do.',
                39 : 'A peaceful heart begins\n'
                'with refusing what damages it.',
                40 : 'You become stronger every time\n'
                'you choose yourself with dignity.'
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
    Random_value_of_Self_improvment = random.randint(1,len_of_self_improvment)
    Qoutes = Qoutes_object.self_improvment()[0][Random_value_of_Self_improvment]
    print(Color + Qoutes + Reset)

def Run_Self_Respect ():
    Random_Value_Self_Respect = random.randint(1,len_of_self_respect)
    Qoutes = Qoutes_object.Self_Respect()[0][Random_Value_Self_Respect]
    print(Color + Qoutes + Reset)

class prosse(Qoutes_Database):
    def input():
         Magenta = "\033[35m"
         Bright_Blue = "\033[94m"

         global User_Input
         User_Input = input(f"{Bright_Blue}{"1. Life lesson \n"
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
    
