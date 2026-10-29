

class Student:
    name = "Angel Chakma"
    __pass = "676767776"
    def __init__(self,Deapartment, University):
        self.Department = Deapartment
        self.University  = University

    def __Hey(self):
        print(f"Hello {self.University}")
    def hello(self):
        self.__Hey()
    
st = Student("Physics","National uniersity")
st.hello()
print(st.Department)
print(st.University)
print(st.name)