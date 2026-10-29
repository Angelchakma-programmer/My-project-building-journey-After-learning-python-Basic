



class name:
    name = "Angel Chakma"
    roll = 17

    @classmethod
    def change_name (cls,name,roll):
        cls.roll = roll
        cls.name = name


n = name()




n.change_name("Lolin chakma",44)
print(n.name)
print(name.roll)

#property decoretor..
class student:
    def __init__(self,phy,chim,math):
        self.phy = phy
        self.chim = chim
        self.math = math

    @property

    def Avarge_percenteg(self):
        return str((self.phy + self.math + self.chim )/ 3) + "%"
        
std = student(50,60,70)

print(std.Avarge_percenteg
())

std.phy = 100

print(std.Avarge_percenteg())
std.chim =90

print(std.Avarge_percenteg())








