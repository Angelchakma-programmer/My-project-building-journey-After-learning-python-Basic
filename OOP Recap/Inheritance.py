

#This is Inheritance

#single inheritance

class Song:
    @staticmethod
    def playing():
        print("song is Playing.....")
    @staticmethod
    def Stop():
        print("This song is not playing...")

class user1(Song):
    def __init__(self,song_name,Singer):
        self.song_name = song_name
        self.Singer = Singer

    
user = user1("Tum hi ho","Arijit sings")
print(user.song_name)
user.playing()


#This is Multilevel inheritance
class Team():
    @staticmethod
    def Player():
        print("yes , we have players....")
    @staticmethod
    def Joursey():
        print("yep, we have a joursey....")

class Brazil(Team):
    def __init__(self,player_name,Joursey_no):
        self.player_name = player_name
        self.Joursey_no = Joursey_no


brazilTeam = Brazil("Neymer",10)
print(brazilTeam.player_name)
brazilTeam.Player()

#This is muyltiple inheritance

class A:
    @staticmethod

    def name():
        print("yep , my name is Angel Chakma")
class B:
    age = "18+"
    
class All(A,B):
    def __init__(self,department):
        self.deaprtment = department

roll = All("English")
print(roll.age
)
roll.name()        