

class car:
    def __init__(self):
        self.acc =  False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("This car is started. ....")

c = car()
c.start()

#let's practics
'''
create account classs with 2 attributes - blance & accont no:
create method for debit ,credit & printing the blance.
'''
class Account:
    def __init__(self,balance,AccountNo):
        self.Balance = balance
        self.Account_Number = AccountNo

    def debit(self,Debit):
        self.Balance -= Debit
        print(Debit,"Tk" , "is Debited")

    def Creadit(self,credit):
        self.Balance += credit
        print(credit,"Tk is Creadited ")
    def Blance(self):
        return self.Balance



a = Account(50000,101)
a.debit(5000)
a.Creadit(4000)
a.Creadit(1000)
print(a.Blance(),"Tk"
)