

#Delete keyword in clases and object

class Student:
    def __init__(self,name):
        self.name = name

std = Student("Angel Chakma")
del std
print(std.name)