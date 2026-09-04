
#This is Dictionary itmes add logic
# Dictionary_Add = {}
# User_age = input("Enter your Age:")
# user_name = input ("Enter your name :")



# Dictionary_Add[user_name] = User_age

# print(Dictionary_Add)
# # a = Dictionary_Add.copy()

# # print(a)

# print(Dictionary_Add[user_name])

#Display Contact Function.
user_input = input("Enter your name :")
user_phone = input("Enter your phone :")

naem = {}
naem[user_input] = user_phone
print(naem)

for i in naem:
    print("Name \t \t Phone")
    print("{}\t{}".format(i,naem.get(i)))

# def View_Contact():
#     print(naem.items())
#     print("Name \t\t Phone ")
#     for A in naem:
#         print("{}\t{}".format(A,naem.get(A)))

# View_Contact()

# def display_contact():
#     print(Contact.items())
#     print("Name\t\tContact Number")
#     for key in Contact:
#         print("{}\t\t{}".format(key,Contact.get(key)))

# print("{}\t {}")