

#This is My Rebuilding Calculate expenses Cost project . with Blueprint and Sudo code.
#i have all system degine so let's get start ........

print("Welcome to Expenses cost Calculator .")
Adding_Input_Cost = []
#Adding prices
Done = False
while  not Done:
        
    try:
        while True:
            
            Input_Cost = int(input("Enter you Expeses Cost :"))
        
            Adding_Input_Cost.append(Input_Cost) #Use list data structure for Adding Expenses Cost.

            #Asking from user. Adding items done or Not Done>
            AskToUser = input("Adding Done ? [Y/N]")
            if AskToUser.strip().casefold() == "y":
                print("Ok Cost Add function Closed !")
                break
            
            elif AskToUser.strip().casefold() == "n":
                print("Keep adding...")
                pass
                
            else:
                print("Sorry invalid input not Expected.....")
                #Loop is Continue
        #Showing Buying itmest numbers list.
        print(f"Your Total Buying itmes Is : {len(Adding_Input_Cost)}")
        #Showing total Expenses cost Monney.
        Total_cost = sum(Adding_Input_Cost)
        print(f"Your Total Expenses Cost is : {Total_cost} Tk")
        print("The end Calculatiions Program.") 
        Done = True
        if Done == True:
            break   
     

      

    except:
        print("Plese input Integer  Number . and try Again.")
    
     

#Finally i completed my project...