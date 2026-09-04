
#Contact book app . i'll build tommowrow

Store_Contact = {}
def View_Contact():
    print("Name \t\t Phone Number")
    for Dict_key in Store_Contact:
        print("{}\t\t{}".format(Dict_key, Store_Contact.get(Dict_key)))

while True:
    User_inut = input(
                      "1. Add Contact\n"
                      "2. View Contact.\n"
                      "3. Search Contact.\n"
                      "4. Update Contact. \n"
                      "5. Delete Contact.\n"
                      "6 . Exit Apps.\n"
                      "\nWhat you wnat to do Just write That Number :")
    if User_inut == "1":
        print("You can add your Contact .")
        Contact_name = input("Enter your name :")
        Contact_Number = input("Enter your Phone Number :")

        Store_Contact[Contact_name] = Contact_Number

    elif User_inut == "2" :
        if not Store_Contact:
            print("The Contact is Empty.")
        else:
            View_Contact()
            
    elif User_inut ==  "3":
        user_contact = input("Enter your Contact name :")
        if user_contact in Store_Contact:
            print(user_contact,"Your Phone number is : ",Store_Contact[user_contact])

        else:
            print("\nContact is not found.")

    elif User_inut == "4" :
        print("Which Contact do you want update ?")
        User_inut = input("Enter your conatct name :")
        if User_inut in Store_Contact:
            Input_phone = input("Enter your phone Number :")
            Store_Contact[User_inut] = Input_phone
            View_Contact()
        else:
            print("Contact is not fouond. ")

    elif User_inut == "5" :
        print("You can delete your Contact .")
        User_inut = input("Do you want to Delete Contact ? [Yes/No] :")
        if User_inut.strip().casefold() == "yes":
            User_inut = input("Enter your Contact name :")
            if User_inut in Store_Contact:
                Store_Contact.pop(User_inut)
                print("This Contact is Deleted.")
                View_Contact()
                pass
            else:
                print("Sorry Contact is not found .")
            
        else:
            print("Fine. it's ok")
        
    elif User_inut == "6" :
        print("This Apps is clossed.")
        break
    else:
        print("Invalid Input. Try Again.")


