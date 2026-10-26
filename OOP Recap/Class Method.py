

#This is Class method

class Car :
    def __init__(self,price,brand):
        self.price = price
        self.brand = brand

    def Starting(self):
        print("The Car is Started")
        print("This Car brand is :",self.brand)

    def Price(self):
        return self.price

car = Car(10000,"BMW")

car.Starting()

print(car.Price())

#problem 
# Create Student class that takes name & marks of 3 subjects as arguments in constructor. 
# Then create a method to print avarage
class Student:
    def __init__(self,name,ICT,Mechanics,Heat_tempareture_and_termodynamic):
        self.name = name
        self.ICT = ICT
        self.Mechanics = Mechanics
        self.Heat_tempareture_and_termodynamic = Heat_tempareture_and_termodynamic

    def Avarage(self):
        avarage_marks = (self.ICT + self.Mechanics + self.Heat_tempareture_and_termodynamic) /3
        print(f"This student name is :",self.name,f"And his Avarage marks is : {avarage_marks}")
marks = Student("Angel Chakma",50,60,70)
marks.Avarage()

marks.name = "HEHEH"
marks.Avarage()