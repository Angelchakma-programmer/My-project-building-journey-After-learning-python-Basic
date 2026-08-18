


#This game i'll build Tomorrow
print("Welcome to the Text-based Adventure Game! The Adventure about Rangamati District in bangaladesh.")

User_input = input("Do you wnat to Explore Rangamti District ? [Yes/NO] :")

if User_input.casefold().strip() == "yes":
    class About_Distric():

        def About_Rangamti_sub_district():

            # print("Rangamati District")
            print(""""
                Welcome to Rangamti Sub District
                  
                1 : "Rangamti Sadar
                2 : "Baghaichhari.
                3 : "Kaptai.
                4 : "Kawkhali.
                5 : "Barkal.
                6 : "Langadu.
                7 : "Naniarchar.
                8 : "Rajastthali.
                9 : "Juraichari.
                10 : "Belaichari.""")
    class Show_Datails():

        def Rangamti_sadar():
            print("Welcome to Rangamati Sadar !")
            User_input = input("Sir Rangamati Sub Discrics has a lots of Favourit Tourist place :\n" \
            "Do want to know about that's Place [Yes/No]")
            if User_input.casefold().strip() == "yes":
                print(""" Okay Sir : Here is a name of Rangamati Toursit Place
                      1. Hanging Brige .
                      2. Polwel Park
                      3. Chakma Rajbari
                      4. Rangamati Govt Collge
                      5. Aronnok .""")
                User_input = int(input("Do you want to Know about That Specifice Place Name: "))
                if User_input == 1:
                    print("Yes . The Rangamati Hanging Brige One of the most Popular Tourst spot\n"
                          "Here is a Wesome leak views. And ect.")
                elif User_input == 2:
                    print("Nice chosing . the polwel park is one of the most Popular place in Rangamati Sadar\n"
                          "Here is has a many type of Garden and Stasus and etc .")
                elif User_input == 3:
                    print("Nice pick, The chakma Rajbari is the History of Chakma Adibashi, and The Chakma indeguneas has a Qune and King\n" \
                    "and etc")
                elif User_input == 4:
                    print("greate Choise, The Aronnok Park is a one the most Popular place in Rangmati, that Controled under Bangaladesh \n"
                          "Army . and here is a has view kaptai leak etc.")
                
                else:
                    print("Sorry , pleass Input Valid serial no: and Try Again")
     
            else:
                print("Ok sir No problem !")

        def Baghaichaari():
            print("Welcome to BaghaiChhari.")
            User_input = input("Do you Want to Explore Baghaichhari Upazila ? Yes/No :")
            if User_input == "yes".casefold().strip():
                print("Great Choice, Here is a has Lots of Favourit place. You can explore anything .")
                print("""Chose the Serial no of Place name:
                      1.Latbon
                      2.Majipara.
                      3.Sajek Velly.
                      4.Bangaltuli.
                      5.Marissa Vilage.""")
                User_input = int(input("What's your Choise Place just write this place Serial no: "))
                if User_input == 1:
                    print("Welcome to latbon , This is a one of the most Popular place is marissa. in summer here is views is very Awesome\n"
                          "Becuse here is a has lots of filde.\n"
                          "And in moonsoon This place look like be a Flote like a mini Cox's Bazar.")
                    User_input = input("Are you want to go Back or Sty here ?" "yes/no")
                    if User_input == "yes".casefold().strip():
                        print("Ok Thanks, Back Again.")
                    elif User_input == "No".casefold().strip():
                        print("Ok sir, staty here and enjoy the Latboon views.")
                    else:
                        print("invaild input .")
                elif User_input == 2:
                    print("Nice chose. Maji para is the most Popular place in marissa right now. cause here's a has many Hill and Jum land .\n"
                          "And here is has manny Bembo garden,Green Jum land. and Helipate .\n"
                          "here is a many favourit Place in mariisa .")
                    User_input = input("Do you want to Stay here ? Yes/No :")
                    if User_input == "yes".casefold().strip():
                        print("Ok sir you can back, but Come again . welcome sir.see you again.")
                    else:
                        print("Ok sir , Stay here and Enjoy The majipara Peacefull Views .")
                elif User_input == 3:
                    print("Nice Choise, Wecome to the sajek veally . \n"
                          "The sajek vally is the most popular Tourist place in Bangladesh.\n"
                          "Ok sir you can enjoy the mountain views and lite could .and Enjoy sir . The sajjek velly")
                    User_input = input("Do you want to Stay here ? Yes/No: ")
                    if User_input == "yes".casefold().strip():
                        print("Ok Enjoy your Life with the beutifull veiws.")
                    else:
                        print("Ok sir, you can go . and Must be back again.")
                elif User_input == 4:
                    print("Nice Choise, The Bangatuli Union has a lots of travling plaece. \n")

                    print("""Here is has like :
                          1.Korengatuli Bazar .
                          2. BT high Scholl.
                          3. kasalong River.
                          4. Lots of place .""")
                    
                    User_input == int(input("If you want Explore ,Enter palac serial name : "))
                    if User_input == 1:
                        print("Nice one, The korengatuli Bazar is a Popular Market, cacuse Here is Many peple come from long way\n"
                              "The Market Open Everyday, but Saterday is Main Opened day. here is a many peple come to the market for \n",
                              "bougt There Requred Ponno.")
                    elif User_input == 2:
                        print("Welcome to The BT high scholl. The Bt high scholl is a Best school for The Bangatuli Union, BT fulls Meaning is :\n"
                              "Bangaltuli Tintila.Ok Enjoy your moment .")
                    elif User_input == 3:
                        print("The kasalong river Going to the Karnafully river beside korengatuli Bazar, Here is has a may bot,Brige , And \n"
                              "Many peple fishing here. And Excetera.")
                    elif User_input == 4:
                        print("I'm not want to say which place have are here. if you want to know ,just you have to Explore The Bangaltuli village and \n"
                              "There Culture.")
                    else:
                        print("As your mine.")

                
                elif User_input == 5:
                   print("Welcome to the marissa. here is a has a lots of Favourit place.")
                   print("Soo. you have to explore another mariisa place, becuse here isn't possible explain to everything. \n"
                         "If you want to know just Expolore bro.")
        def Kaptai():
            print("Welcome to Kapati Sadar.")
            User_input = input("Do you Want to Explore Kapai Sadar ? Yes/No :")
            if User_input== "yes".strip().casefold() :

                print("Welcome to the Kaptai Sadar and Here is a lots of Place to Exlpere .")
                print(""" Name of Place.
                      1.Kaptai Dam
                      2.Kaptai national park.
                      3.Kornopuli River.""")
                User_input = int(input("Do you want explore any Place jsut write Place Serial No :"))
                if User_input == 1:
                    print("The kaptai Dam is Created in 1960. Since 1960 to Right now it's Almost 50 years . it's can created electricity,\n"
                          "And here is passing bambo for Condrogan to chittagram. the bembo using make like pappers books eveything.")
                    User_input = input("Sir Could you stay here ? Yes/No :")
                    if User_input == "yes".casefold().strip():
                        print("Ok Enjoy your moment and Save it your Albume.")
                    else:
                        print("Ok sir. advance , see you again .")
                elif User_input == 2:
                    print("The kaptai national park is a has many animal and birds etc. just explore and Enjoy . ")
                    User_input = input("Are you stay here ? Yes/No :")
                    if User_input == "yes".casefold().strip():
                        print("Ok sir you can stay here. here has a many hotel so you Enjoy your moment . Good luck sir.")
                    else:
                        print("Ok sir. see you again. Bye ")
                elif User_input == 3:
                    print("Welcome to the karnapuli River.")
                    print("here is a has lots of History.")
                    User_input = input("Do you want to Know abuut karnapuli Rivers History and Place ? Yes/No :")
                   
                    if User_input == "yes".strip().casefold():
                        print(""" Sir Which You want to Know ?
                              1.Histroy of Kaptai Rivers .
                              2. Kaptai Rivers Favourit Place .""")
                        User_input = int(input("Which you want just wirte the Serial No :"))

                        if User_input == 1:
                            print("""The
                                  Construction of the reservoir for the hydro-electric plant began in 1956 by the Government of East Pakistan.
                                  54,000 acres (220 km2) of farmland in the Rangamati District was submerged with the creation of the lake.
                                  The project was finished in 1961.[3] 40% of 
                                  the total arable land went underwater as a result of the dam construction and 100,000 people were displaced.
                                  against the lake's maximum capacity of 109 MSL.""")
                            
                        elif User_input == 2:
                            print("Here is a has lots of popular palce. I can't explain Right now.")
                            print("If you want to know Just Explore bro.")
                        
                    else:
                        print("Ok no porblem.")
                else:
                    print("Invaild input . Please try again.")

                pass
            else:
                print("Ok No problem .")
        def kawkali():
            print("Hey , Welcome to The Kawakali Upazila.")
            User_input = input("Do you want to Exlplore Kawkalli Upzalila ? Yes/No :")
            if User_input == "yes".casefold().strip():
                print("Nice chose. i whis have a Best Explore.")
                print("""Here is Popular place name :
                      1.Gagra Barar.
                      2.Pahari Chora.""")
                User_input == int(input("Which plaece Are you want explore just write this serial No."))
                

                if User_input == 1:
                    print("Welcome to the Gagra Bazar . the gagra Bazar One of the most Polular market in Kawkali.\n"
                          "Here is a Avalable many type of jummo foods and Vegitable. like Mokke, Sindire, Mamara, and etc."
                          )
                    
                    # The project is going on. adding gagra bazar.


            else:
                print("Ok no problem .")
    class Select_Sub_Distric(Show_Datails):
      


            pass

    
        


        


       
    a =About_Distric.About_Rangamti_sub_district()
    #show_datalis =Select_Sub_Distric.Baghaichaari()
    show_datalis = Select_Sub_Distric.Kaptai()
            
        

        

else:
    print("The game is Ended")



