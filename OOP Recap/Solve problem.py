

'''
Question 1:
Define a circle class to create a circle with radius r using constructor.
define an area method of the class which calculate The area of circle.
define a perimeter method of the class which allows to you calculate the perimeter of the circle.

'''

class Circle:
    def __init__(self,Radius):
        self.Radius = Radius
    def Area(self):
        are = (22/7) * (self.Radius**2)
        print("This circle area is : ",are)
    def perimeter (self):
        perimeter = 2 * (22/7) * self.Radius
        print("The circle perimeter is :",perimeter)

cir = Circle(21)
cir.Area()
cir.perimeter()

'''
Question 2 : Define a employe class with attributes role, department & salary.  this class has a also 
show_Details method
'''

class Employe:
    def __init__(self,role,department,salary):
        self.role = role 
        self.department = department
        self.salary = salary
    
    def Show_details(self):
        print("This employe role is :",self.role)
        print("This Employe department is :",self.department)
        print("This emplyes salary earn is :",self.salary,"Tk")
class Engineer(Employe):
    def __init__(self,name,age,role,department,salary):
        
        self.name = name
        self.age = age
        super().__init__(role,department,salary)

    def Show_Engineer(self):
        print("The Engineer name is :",self.name)
        print("This Devloper age is : ",self.age)
        print("This Engineer role is :",self.role)
        print("This Engineer Department is : ",self.department)
        print("This Engineer salay is :",self.salary)




emp = Employe("Software Engineer","CSE",100000)
emp.Show_details()

eng = Engineer("Angel Chakma","18+","Software Enginear","Physics",80000)
eng.Show_Engineer()