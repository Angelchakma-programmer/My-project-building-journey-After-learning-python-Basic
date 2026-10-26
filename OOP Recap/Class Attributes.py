

#This is Calss and object  Attributes:
class Student:
    university_name = "University of Dhaka" #Class Attributes

    def __init__(self,name,department,university_name):
        self.name = name
        self.department = department
        self.university_name = university_name #object Attribur
        #Object Attribues > class Attriubes

st = Student("Angel Chakma","Physics","National University")
print(st.name,st.department,st.university_name)

st2 = Student("Lolin Chakma","CST","Diploma and Enginering")

print(st2.name,st2.department,st.university_name)
st3 = Student("Biggan jyoti","Phyics",None)
print(st3.name,st3.department,st.university_name)