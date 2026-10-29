

class students:
    def __init__(self,student,department,teachers):
        self.student = student
        self.department = department
        self.teachers = teachers
        roll = 10

    @staticmethod
    def roll ():
        print("my roll is 17")
    
class Department_of_phyics(students):
    name = "Angel Chakma"
    def __init__(self,numberOfStudnets,subject,student,department,teachers):
        super().__init__(student,department,teachers)
        self.numberOfStudent = numberOfStudnets
        self.subject = subject
        super().roll()
        


physics = Department_of_phyics("50+","Mechanics","Angel Chakma", "Physics","Gita mem")
physics.name
print(physics.name)
