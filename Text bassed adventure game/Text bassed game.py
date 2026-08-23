


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
                10 : "Belaichari.
                11 : Exit Game.""")
    class Show_Datails:

        def Rangamti_sadar(self):
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
                User_input = input("Do you want to Know about That Specifice Place Name: ")
                if User_input == "1":
                    print("Yes . The Rangamati Hanging Brige One of the most Popular Tourst spot\n"
                          "Here is a Wesome leak views. And ect.")
                elif User_input == "2":
                    print("Nice chosing . the polwel park is one of the most Popular place in Rangamati Sadar\n"
                          "Here is has a many type of Garden and Stasus and etc .")
                elif User_input == "3":
                    print("Nice pick, The chakma Rajbari is the History of Chakma Adibashi, and The Chakma indeguneas has a Qune and King\n" \
                    "and etc")

                elif User_input == "4":
                    print("Welcome To Rangamti Govt college. ")
                    User_input = input("Do you Want to Know about Rangamti Govt college ? Yes /No :")
                    if User_input == "yes".strip().casefold():
                        print("Here is has lot of Deaprtment. here is has HSC Cariculam and Honours And Degree.")
                        print(""" Nice choise.
                                Here is has lot of Department.
                                1. Department of physics.
                                2. Department of Mathmethcis.
                                          
                                           """)
                        User_input = input("Do you Want to know about That Department . Selcet just serial No:")
                        if User_input == "1":
                            print("This The most High Demand Department of Rangamati Govt college. here is Sheet Only 50 . So that's why \n"
                                  "It's one of the most Demanding Subject in the College.")
                            print("Here is A has one Students and she is learning programming .")
                            User_input = input("Do you want to know who is him ? " "yes/ No: ")
                            if User_input == "yes".strip().casefold():
                                print("Nice . He is  a Angel Chakma.\n"
                                      "her Roll no is : 17\n"
                                      "he's learning python programming langauage.")
                            print()
                        elif User_input == "2":
                            print("The mathmathics Department is one of the most popular Department of Rangamati Govt college.\n"
                                  "I have no idea about the department.")
                        else:
                            print("invalid Input.")

                           
                        #Adding Department info of Rangmati Govt college.
                    else:
                        print("It's ok bro.")
                elif User_input == "5":
                    print("greate Choise, The Aronnok Park is a one the most Popular place in Rangmati, that Controled under Bangaladesh \n"
                          "Army . and here is a has view kaptai leak etc.")
                
                else:
                    print("Sorry , pleass Input Valid serial no: and Try Again")
     
            else:
                print("Ok sir No problem !")

        def Baghaichaari(self):
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
                User_input = input("What's your Choise Place just write this place Serial no: ")
                if User_input == "1":
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
                elif User_input == "2":
                    print("Nice chose. Maji para is the most Popular place in marissa right now. cause here's a has many Hill and Jum land .\n"
                          "And here is has manny Bembo garden,Green Jum land. and Helipate .\n"
                          "here is a many favourit Place in mariisa .")
                    User_input = input("Do you want to Stay here ? Yes/No :")
                    if User_input == "yes".casefold().strip():
                        print("Ok sir you can back, but Come again . welcome sir.see you again.")
                    else:
                        print("Ok sir , Stay here and Enjoy The majipara Peacefull Views .")
                elif User_input == "3":
                    print("Nice Choise, Wecome to the sajek veally . \n"
                          "The sajek vally is the most popular Tourist place in Bangladesh.\n"
                          "Ok sir you can enjoy the mountain views and lite could .and Enjoy sir . The sajjek velly")
                    User_input = input("Do you want to Stay here ? Yes/No: ")
                    if User_input == "yes".casefold().strip():
                        print("Ok Enjoy your Life with the beutifull veiws.")
                    else:
                        print("Ok sir, you can go . and Must be back again.")
                elif User_input == "4":
                    print("Nice Choise, The Bangatuli Union has a lots of travling plaece. \n")

                    print("""Here is has like :
                          1.Korengatuli Bazar .
                          2. BT high Scholl.
                          3. kasalong River.
                          4. Lots of place .""")
                    
                    User_input = int(input("If you want Explore ,Enter palac serial name : "))
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

                
                elif User_input == "5":
                   print("Welcome to the marissa. here is a has a lots of Favourit place.")
                   print("Soo. you have to explore another mariisa place, becuse here isn't possible explain to everything. \n"
                         "If you want to know just Expolore bro.")
                else:
                    print("Invalid Input. Try Again.")

            else:
                print("It's ok no problem.")
        def Kaptai(self):
            print("Welcome to Kapati Sadar.")
            User_input = input("Do you Want to Explore Kapai Sadar ? Yes/No :")
            if User_input== "yes".strip().casefold() :

                print("Welcome to the Kaptai Sadar and Here is a lots of Place to Exlpere .")
                print(""" Name of Place.
                      1.Kaptai Dam
                      2.Kaptai national park.
                      3.Kornopuli River.""")
                User_input = input("Do you want explore any Place jsut write Place Serial No :")
                if User_input == "1":
                    print("The kaptai Dam is Created in 1960. Since 1960 to Right now it's Almost 50 years . it's can created electricity,\n"
                          "And here is passing bambo for Condrogan to chittagram. the bembo using make like pappers books eveything.")
                    User_input = input("Sir Could you stay here ? Yes/No :")
                    if User_input == "yes".casefold().strip():
                        print("Ok Enjoy your moment and Save it your Albume.")
                    else:
                        print("Ok sir. advance , see you again .")
                elif User_input == "2":
                    print("The kaptai national park is a has many animal and birds etc. just explore and Enjoy . ")
                    User_input = input("Are you stay here ? Yes/No :")
                    if User_input == "yes".casefold().strip():
                        print("Ok sir you can stay here. here has a many hotel so you Enjoy your moment . Good luck sir.")
                    else:
                        print("Ok sir. see you again. Bye ")
                elif User_input == "3":
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
        def kawkali(self):
            print("Hey , Welcome to The Kawakali Upazila.")
            User_input = input("Do you want to Exlplore Kawkalli Upzalila ? Yes/No :")
            if User_input == "yes".casefold().strip():
                print("Nice chose. i whis have a Best Explore.")
                print("""Here is Popular place name :
                      1.Gagra Barar.
                      2.Pahari Chora.""")
                User_input = input("Which plaece Are you want explore just write this serial No :")

                if User_input == "1":
                    print("Welcome to the Gagra Bazar . the gagra Bazar One of the most Polular market in Kawkali.\n"
                          "Here is a Avalable many type of jummo foods and Vegitable. like Mokke, Sindire, Mamara, and etc."
                          )
                    
                    # The project is going on. adding gagra bazar.
                    User_input = input("Do You want to Explore Gagra Bazar ? Yes/No :")
                    if User_input == "Yes".strip().casefold():
                        print("""Here is a has Many  Type Producnts Like .
                                1. Jummo Paper,
                                2. Termeric Pouder No Formalin.
                                3.Handcraft Product .
                                4.Dry fish and Sidol.
                        
                               """)
                        User_input = input("Are you Want to Explore This type products ? Yes/No :")
                        if User_input == "yes".strip().casefold():
                            print("Nice Choise .")
                            
                            User_input == int(input("Seclect The products serial NO. what is you want to explore ."))
                            if User_input == 1:
                                print("The jummo Paper is Call localy Jummo moris. it's very spices. and it't market value \n"
                                      "Per Kilogram 400 Tk. if you want to by just Ask them.")
                            elif User_input == 2:
                                print("The Termeric and termeric pauder it's we use for dally cooking.\n"
                                      "Every Matton and Every type of foods requred This.\n"
                                      "Otherwise that's foods isn't Testy . it's making prosses has a lots of history\n"
                                      "That's isn't poosible to Expalin here . if you want to know you have to explore There Culture.\n"
                                      "Go for Explore , Best wishes to You Bro.")
                            elif User_input == 3:
                                print(""""The handcraft product 
                                      like .
                                      there local name :
                                      1. Tranditiona Pinone hadi.
                                      2. Traditional Tami.
                                      3. Lei, Senge, toloi and Hulo etc.
                                      4.Dup.
                                      """)
                                print("If you Wnat to Know  just  Explore bro.")

                            elif User_input == 4:
                                print("The dry Fish And Sidol is most popular product here. because of The Sidol is Spices in Chakma indegenus. and \n"
                                      "And The Dry fish it's called localy Sutiki in Bangala. and Suguni in Chakma.\n" 
                                      "If you Wnat to Testsing that you have to go There Village and Explore there Culuture.")
                                
                            else:
                                print("Invalid Input . try again .")

                        else:
                            print("It's ok no problme .")


                    else:
                        print("Ok . You can explore another places.")

                elif User_input == "2":

                    print("""The pahari chora it's Place located in kawkali in Rangamti.\n"
                        "Here is a has lots of Mind Relaxing place Like :
                        1. Fresh and cool Water
                        2. Tracking in Mountain.
                        3. Gagra Kolabagan Waterfall.
                        """)
                    User_input = input("Do you Want to Explore This Place ? Yes/No :")
                    if User_input == "yes".strip().casefold():
                        print("Nich Chose ! ")
                        User_input = int(input("Which Place are you want explore just write This place serial No :"))

                        if User_input == 1:
                            print("Here is a has lots of favourite place and fresh, cool water.\n"
                                "The Fresh and cool water requred in our life. because of when we be a overloded . then we need to be fresh\n"
                                "That's why you should explore kawkali Fresh and coll water Place and leak.")
                            User_input = input("One question are you Depress or Overlode ? Yes/ No :")
                            if User_input == "yes".casefold().strip():
                                print("No worries, bro just Enjoy The view and cool water and i wish your mind is be a calm and happy .\n"
                                    "Then if you be a relax you have to Say Thnaks me.")
                            else:
                                print("ok no problem . you're problem only solve  you. just enjoy The views bro.")

                        elif User_input == 2:
                            print("You're Brave bro ! Cause many peple don't chose Tracking mountain becuse there're Weak. That's why you are Brave.\n"
                                "Here is a has lots of Mountain and those is Popular for tracking.\n"
                                "Just Enjoy bro your life.\n"
                                "Life is one so just Enjoy This.")
                            User_input = input("One Question Whay you chose for tracking Mountain ?")

                            print(f"{User_input}, That's Aesome.")
                        elif User_input ==3 :
                            print("Nich choise. The Gagra kolabagan WalterFall is One of the most Peacefull place in Gagra.\n"
                                "Here is a has lots of mini walter falls. if you want to go here it's take time might 20 -25 minute.")
                            
                            User_input = input("Do you Enjoying the Exploring Gagra waterfalls ? yes/no :")
                            if User_input == "yes".strip().casefold():
                                print("Nich bro you're brave man. Enjoy your moment .")
                            elif User_input == "No".strip().casefold():
                                print("Ok, i guees Don't know about this place. best wishes to you. just enjoy the Journey. ")

                else:
                    print("Invlild Input. try again.")
                    

                        
                # else:
                #     print("It's ok no Problem.")
               


            else:
                print("Ok no problem .")

        def Naniarchar(self):
            print("Welcome to Naniarchar Sadar  .")
            User_input = input("Do you want to Explore Naniarchar Sub District ? Yes/No:")
            if User_input == "Yes".strip().casefold():
                print(""""Nich Choise, Here is a has Lots of place :
                      1. Pineapple Garden.
                      2. Birstesto Munsi abdur Memorial.
                      3. Naniarchar Brige.""")
                
                User_input = input("Which Place do you want to Explore write serial no :")
                if User_input == "1":
                    print("Welcome to Naniarchar Pineapple Graden. Here is has lots of Gareden . You can explore Anything\n"
                          "In naniarchar Every mountain is Fineapple garden so just explore.")
                    User_input = input("Do you Enjoying Exploring Fineapple Garden? Yes/No :")
                    if User_input == "yes".strip().casefold():
                        print("Nich Bro. enjoy your moment .")
                    else:
                        print("It's ok ")

                elif User_input == "2":
                    print("Welcome to Brisresto munis adbdhur Roup Memorial. \n"
                          "You Can explore that memorial.")
                    User_input = input("Do you want to know about The memorial History ? Yes/No :")
                    if User_input == "yes".strip().casefold():
                        print("The memorical Created for 1971 eng for birsresto munsi abodur roup she was Mukti jodda.\n"
                              "That's why The memorial Created.")
                        print("Munshi Abdur Rouf was born on 8 May 1943 at Salamatpur village.\n" 
                              "(renamed Rouf Nagar)[4] under Boalmari thana (currently Madhukhali thana) in Faridpur District.[")
                        
                        pass
                    else:
                        print("Ok, as your wish .")
                elif User_input == "3":
                    print("Welcome to the Naniarchar Brige. The Naniarchar Brige is one of the most Popular place in Naniarchar.\n"
                          "Here is a has lots of view and leak view.")
                    User_input = input("Do you want to know about the brige History ? Yes/No :")
                    if User_input == "yes".strip().casefold():
                        print("The Naniarchar Brige is Created in 1980. Since 1980 to Right now it's Almost 50 years . it's can created electricity,\n"
                              "And here is passing bambo for Condrogan to chittagram. the bembo using make like pappers books eveything.")
                    
                else:
                    print("Invalid Input . Please try again .")

            else:
                print("It's ok no problem")
        def barkal(self):
            print("Welcome to the Barkal Upazila.")
            User_input = input("Do you want to Explore Barkal Upazila ? Yes/No :")
            if User_input == "yes".strip().casefold():
                print("Great Choice, Here is a has lots of place to Explore .")
                print("""Here is a has lots of place :
                      1. Barkal Bazar.
                      2. Barkal Brige.
                      3. Barkal Park.
                      4. Subolong Waterfall.""")
                User_input = input("Which Place do you want to Explore just write serial no :")
                if User_input == "1":
                    print("Welcome to the Barkal Bazar. The Barkal Bazar is one of the most Popular place in Barkal.\n"
                          "Here is a has lots of view and leak view.")
                    User_input = input("Do you want to know about the bazar History ? Yes/No :")
                    if User_input == "yes".strip().casefold():
                        print("The barkal bazar is one of the most popular bazar in Barkal Upazila.\n"
                              " Here is a has lots of shops and market. The barkal bazar is one of the most popular place in Barkal.\n")
                        User_input = input("Do you want to know about The barkal bazar products ? Yes/No :")
                        if User_input == "yes".strip().casefold():
                            print("The barkal bazar is one of the most popular bazar in Barkal Upazila.\n"
                                  " Here is a has lots of shops and market. The barkal bazar is one of the most popular place in Barkal.\n"
                                  "Here is a has lots of products like :\n"
                                  "1. Jummo Paper.\n"
                                  "2. Termeric Pouder No Formalin.\n"
                                  "3. Handcraft Product .\n"
                                  "4. Sidol.\n"
                                  "5. Ginger. \n"
                                  "6. kaptai leak fish.")
                            User_input = int(input("If you want to know Sepecifiec items just write Products No :"))
                            if User_input == 1 :
                                print("The jummo papper is one of the most Popular spices in Barkal Bazar.\n"
                                      "It's per kilogram 200 Tk .")
                            elif User_input == 2:
                                print("The Termeric powder is One of the most Requred Spices in Everyday. it's helps us building masal.\n"
                                      "The termeric making prosses has a lots of hsitory if you want to explore just Dive in thear village.")
                                #Adding Barkal upazila.
                            elif  User_input == 3:
                                print("The handcraft product is one the most usefull here. because the handcarft product made using Bembo,Tree \n"
                                      "So this is very natureal not Fast type.\n"
                                      "The handcarft products We use dally life so that's why we can use handcarft products .")
                                
                            elif User_input == 4:
                                print("The Sidol it's local name . it't original name is Nappi. The sidol They use everyday for made food.\n"
                                      "That's why There requred it.")
                            elif User_input == 5:
                                print("The Ginger It's localy called Ada. The Ginger plantation we use jumm land and some land.\n"
                                      "It's making has many prosse .")
                                User_input = input("Do you want to know That's prosses ? Yes/No :")
                                if User_input == "yes".strip().casefold():
                                    print("Nice one . The ginger makeing lots of prosse. so we expalin first to last .\n"
                                          "1. Before going to plantaion we have to Sowing .\n "
                                          "2. Then we have to make land for wowing. \n"
                                          "3. Then we have to planting.\n"
                                          "4. After planting we have to wait 3 - 4 month soo this time we have to wait for claim. \n"
                                          "5. After waiting for we have to sift for Selling. then we have to sell a gain maoney \n"
                                          "That's is all prosses for only basic . here isn't possible to explain here. so if you want to know just explore bro.")
                                    
                                else:
                                    print("It's ok bro.")

                            elif User_input == 6 :
                                print("The kaptai leak fish . The local peple fishing here . here has  lots place for fishing Specialy Kattoli leak. and someting.\n "
                                      "if you want to know all the prosses just you have to explore bro.\n"
                                      "Soo best wishes to you. enjoy your moment.")
                
                        
                                
                            

                        else:
                            print("Ok, as your wish .")

                    else:
                        print("Invalid Input . Please try again .")
                elif User_input == "2":
                    print("Welcome to barkal brige. The barkal brige I don't have to soo much idea. i can say just explore bro. \n"
                          "Best wishes to you bro.")
                elif User_input == "3" :
                    print("Welcome to Barkal Park bro. here is has lots of views for Exploring and Feeligs deeply.\n"
                          "If you want to know about more you have to just explore bro.\n"
                          "Best wihses to you bro. Just explore and ejnoy your moment.")

                elif User_input == "4":
                    print("Hey bro welcome to Subolong walterfall. You can explore bro .")
                    User_input = input("Do you want to Explore Subolong walterfalls ? yes/no :")
                    if User_input == "yes".strip().casefold():
                        print("Nice one bro.")
                        print("""Welcome to Subolong park and waterfall
                              you can Explore this . 
                              1. Waterfalls .
                              2. Subolong park.
                              3. ejnoy Kaptai leak views in subolong. """)
                        User_input = int(input("Whis you want to explore write just That's palce serial No :"))
                        if User_input == 1:
                            print("Nice one bro. And Welcome to Subolong Walterfalls. The walterfalls is one of highest Walterfalls in Rangamati District.\n"
                                  "")
                            print("The walterfalls is one of the most Popular place in Barkal Upazila. here is a has lots of views and leak views.\n"
                                  "If you want to know about the walterfalls just explore bro. best wishes to you bro.")
                            User_input = input("Do you want to stay here ? Yes/No :")
                            if User_input == "yes".strip().casefold():
                                print("Ok bro, Enjoy your moment and stay here. and best wishes to you bro. Just enjoy your moment.")
                            else:
                                print("Ok bro, you can go. and best wishes to you bro. Just enjoy your moment.")

                        elif User_input == 2:
                            print("Welcome to the Subolong Park. The subolong park is one of the most Popular place in Barkal Upazila.\n"
                                  "Here is a has lots of views and leak views.\n"
                                  "If you want to know about the subolong park just explore bro. best wishes to you bro.")
                            User_input = input("Do you want to explore the subolong park ? Yes/No :")
                            if User_input == "yes".strip().casefold():
                                print("Ok bro, Enjoy your moment and stay here. and best wishes to you bro. Just enjoy your moment.")
                            else:
                                print("Ok bro, you can go. and best wishes to you bro. Just enjoy your moment.")
                        elif User_input == 3:
                            print("Welcome to the Kaptai leak views in subolong. The Kaptai leak is one of the most Popular place in Barkal Upazila.\n"
                                  "Here is a has lots of views and leak views.\n"
                                  "If you want to know about the Kaptai leak just explore bro. best wishes to you bro.")
                            User_input = input("Do you Wnat to explore Kaptai leak in subolong ? Yes/No :")
                            if User_input == "yes".strip().casefold():
                                print("Nich one. The kaptai leak here is localy call Katoli bill. In the kattoli bill you can go direct marissa Baghaichhari.\n"
                                      "Yes bro Enjoy Explore and enjoy your moment. ")
                                
                            else:
                                print("It's ok")
                            
        
                        
                            #how it's going.

                        else:
                            print(" It's ok . as your wish.")
                    else:
                        print("It's ok no problem") 
                else:
                    print("Invaild Input. Try Again.")

            else:
                print("It's ok As your Wish.")

        def Bilaichari(self):
            print("Welcome to Bilaicharri Upazila")
            User_input = input("Do you Want to Explore Bilaichari Upazila ? Yes/No :")
            if User_input == "yes".strip().casefold():
                print("Nich chosie. let't dive in Bilaichari Favourite and Popular place !")
                print("""Here is has lots of place for Exploring . 
                      Which place do you want to Explore Just write serial NO :
                      1. Dhuppani WalterFall.
                      2. Gaskata Chora Walterfall.
                      3. Niladri Resort.
                      4. Digolchari Brige .
                      5. Local foods.""")
                User_input = input("Enter Serial no:")
                if User_input == "1":
                    print("Nice choise. The Dhuppani Walterfall is one of the most popular in Bilaichari. it's Highet 150 miters.\n"
                          "While Water Up to down then show White Boll. That's Why it's Call Dhuppani jorna.")
                    User_input = input("Do you Want to explore more about Dhupani jorana ? yes / No : ")
                    if User_input == "yes".strip().casefold():
                        print("""Here is has lots of way to Explore Dhuppani jorna.
                              1.Explore by bot .
                              2. Explore by Hill Road.
                              3. JUngle Rolad + Tracking.""")
                        User_input = int(input("Which way to want to Explore enter the seriral No:"))
                        if User_input == 1:
                            print("Nich choise bro. Right now i don't say anything . Just Explore and Enjoy your moment.\n"
                                  "And Remember it;s is Adventure way so Be carefull.")
                        elif User_input == 2:
                            print("Nice one. i guess you're Brave. So explore bor. Enjoy the hill and mountain views \n"
                                  "Relaxing your mind. Be Carefull Cauase it's jungle . so ok bro enjoy your momment.")
                        elif User_input == 3:
                            print("O bro nice choise. in This Way you have to trecking hill jungle and Excectra. soo Let's dive in. And i don't want to say \n"
                                  "anything So just explore and Enjoy your life.")
                        else:
                            print("Invalid input. try agin man.")

                

                        pass
                    else:
                        print("It's ok Bro.")

                elif User_input == "2":
                        print("Welcome to Gagrachora Walter Fall.")
                        User_input = input("Do you want to Explore Gagrachora Walter Fall ? Yes/No :")
                        if User_input == "yes".strip().casefold():
                            print("Nich choise bro. Right now i don't say anything . Just Explore and Enjoy your moment.\n"
                                  "And Remember it;s is Adventure way so Be carefull.")
                        else:
                            print("It's ok bro. as your wish.")
                elif User_input == "3":
                    print("Welcome to Niladri Resort. The Niladri Resort is one of the most Popular place in Bilaichari Upazila.\n"
                          "Here is a has lots of views and leak views.\n"
                          "If you want to know about the Niladri Resort just explore bro. best wishes to you bro.")
                    User_input = input("Do you want to explore the Niladri Resort ? Yes/No :")
                    if User_input == "yes".strip().casefold():
                        print("Ok bro, Enjoy your moment and stay here. and best wishes to you bro. Just enjoy your moment.")
                        print("""In the Niladri Resort here is has lots of services like :
                              1. Hotel.
                              2. Restaurant.
                              3. Swimming Pool.
                              4. Kaptai leak view.""")
                        User_input = int(input("Which service do you want to explore just write serial No :"))
                        if User_input == 1:
                            print("Welcome to the Niladri Resort Hotel. The Niladri Resort Hotel is one of the most Popular place in Bilaichari Upazila.\n"
                                  "Here is a has lots of views and leak views.\n"
                                  "If you want to know about the Niladri Resort Hotel just explore bro. best wishes to you bro.")
                        elif User_input == 2:
                            print("Welcome to the Niladri Resort Restaurant. The Niladri Resort Restaurant is one of the most Popular place in Bilaichari Upazila.\n"
                                  "Here is a has lots of views and leak views.\n"
                                  "If you want to know about the Niladri Resort Restaurant just explore bro. best wishes to you bro.")
                        elif User_input == 3:
                            print("Welcome to the Niladri Resort Swimming Pool. The Niladri Resort Swimming Pool is one of the most Popular place in Bilaichari Upazila.\n"
                                  "Here is a has lots of views and leak views.\n"
                                  "If you want to know about the Niladri Resort Swimming Pool just explore bro. best wishes to you bro.")
                        elif User_input == 4:
                            print("Welcome to the Niladri Resort Kaptai leak view. The Niladri Resort Kaptai leak view is one of the most Popular place in Bilaichari Upazila.\n"
                                  "Here is a has lots of views and leak views.\n"
                                  "If you want to know about the Niladri Resort Kaptai leak view just explore bro. best wishes to you bro.")
                        else:
                            print("Invalid input. try again bro.")
                    else:
                        print("Ok bro, you can go. and best wishes to you bro. Just enjoy")

                elif User_input == "4":
                    print("Welcome to Digolchari Brige. The Digolchari Brige is one of the most Popular place in Bilaichari Upazila.\n"
                        "Here is a has lots of views and leak views.\n"
                        "If you want to know about the Digolchari Brige just explore bro. best wishes to you bro.")
                    User_input = input("Do you want to explore the Digolchari Brige ? Yes/No :")
                    if User_input == "yes".strip().casefold():
                        print("Ok bro, Enjoy your moment and stay here. and best wishes to you bro. Just enjoy your moment.")
                    else:
                        print("Ok bro, you can go. and best wishes to you bro. Just enjoy")
                            
                elif User_input == "5":
                    print("Welcome to Local foods. The Local foods is one of the most Popular place in Bilaichari Upazila.\n"
                        "Here is a has lots of views and leak views.\n"
                        "If you want to know about the Local foods just explore bro. best wishes to you bro.")
                    User_input = input("Do you want to explore the Local foods ? Yes/No :")
                    if User_input == "yes".strip().casefold():
                        print("Ok bro, Enjoy your moment and stay here. and best wishes to you bro. Just enjoy your moment.")
                        user_input = input("Do you want to know about the Local foods ? Yes/No :")
                        if user_input == "yes".strip().casefold():
                            print("yep here is a has lots of Local foods . if you wnat to testing just explore bro. best wishes to you bro.")

                        else:
                         print("Ok bro, you can go. and best wishes to you bro. Just enjoy")

                else:

                    print("Invalid Input. try again.")
            

            else:
                print("It's ok As your Wish.")
        def Langadu(self):
            print("Welcome to Langadu Upazila")
            User_input = input("Do you Want to Explore Langadu Upazila ? Yes/No : ")
            
            if User_input.strip().casefold() == "yes":
                print("Nice choice! Let's dive into Langadu's Favourite and Popular places!")
                print("""Here is has lots of place for Exploring . 
                    
                    1. Kattoli Beel (Wetland & Bird Sanctuary).
                    2. Tin Kona Pahar (Triangular Hill Peak).
                    3. Mainimukh Ghat & Bazar.
                    4. Kalapakujja Lake Viewpoint.
                    5. Duluchhari Waterfall.""")
                
                User_input = input("Which place do you want to Explore Just write serial NO ").strip()


                if User_input == "1":
                    print("Nice choice. Kattoli Beel is the largest wetland in Northern Kaptai Lake.\n"
                        "During winter (November to February), thousands of guest migratory birds arrive here from Siberia.")
                    User_input = input("Do you Want to explore more about Kattoli Beel ? yes / No : ")
                    if User_input.strip().casefold() == "yes":
                        print("""Here is has lots of way to Explore Kattoli Beel:
                            1. Bird Watching by Engine Boat.
                            2. Early Morning Sunrise & Water Lily Tour.
                            3. Visiting Local Fishing Villages.""")
                        User_input = input("Which way do you want to Explore? Enter the serial No: ").strip()
                        if User_input == "1":
                            print("Nice choice bro. You will see thousands of Lesser Whistling Ducks, Pintails, and Cotton Pygmy Geese.\n"
                                "Remember to bring your binoculars and camera. Enjoy your birdwatching moment!")
                        elif User_input == "2":
                            print("Awesome choice! Morning mist on the lake with red water lilies looks magical.\n"
                                "Relax your mind and take plenty of sunrise photos. Enjoy bro!")
                        elif User_input == "3":
                            print("Great choice bro! You will see traditional fishermen casting nets in the vast lake.\n"
                                "Enjoy the peaceful village lifestyle and have fun!")
                        else:
                            print("Invalid input. Try again man.")
                    else:
                        print("It's ok Bro.")
                        #kattoli beel is ok. no problem has

                elif User_input == "2":
                    print("Welcome to Tin Kona Pahar (Triangular Hill)!\n"
                        "It is an iconic pyramid-shaped mountain rising straight from Kaptai Lake waters.")
                    User_input = input("Do you want to Explore Tin Kona Pahar ? Yes/No : ")
                    if User_input.strip().casefold() == "yes":
                        print("""Here is has lots of services and activities:
                            1. 15-20 Minutes Hiking to Summit.
                            2. 360-Degree Lake & Distant Hill View.
                            3. Speedboat Cruise around the Hill Island.""")
                        User_input = input("Which activity do you want to explore? Enter serial No: ").strip()
                        if User_input == "1":
                            print("Nice one! I guess you're brave. Hike up the rocky trail carefully.\n"
                                "Remember to wear good shoes. Enjoy your hiking adventure bro!")
                        elif User_input == "2":
                            print("Awesome! The 360-degree panorama of blue lake water and green hills will blow your mind.\n"
                                "Feel the fresh mountain breeze and relax your mind.")
                        elif User_input == "3":
                            print("Nice choice! Cruising around the triangular peak by boat is exciting.\n"
                                "Enjoy the cool splash of Kaptai Lake water bro!")
                        else:
                            print("Invalid input. Try again bro.")
                    else:
                        print("It's ok bro, as your wish.")
                        #its right

                elif User_input == "3":
                    print("Welcome to Mainimukh Ghat & Bazar. It is the central commercial hub of Langadu Upazila,\n"
                        "located right at the confluence of Maini River and Kaptai Lake.")
                    User_input = input("Do you want to explore Mainimukh Ghat & Bazar ? Yes/No : ")
                    if User_input.strip().casefold() == "yes":
                        print("""In Mainimukh Ghat & Bazar here is has lots of experiences like :
                            1. Weekly Traditional Tribal Haat (Market).
                            2. Fresh Kaptai Lake Fish Market (Chapila, Rui, Boal).
                            3. Local Food & Fresh Fish Fry Tasting.
                            4. Passenger Launch Ghat to Rangamati Sadar.""")
                        User_input = input("Which one do you want to explore? Write serial No: ").strip()
                        if User_input == "1":
                            print("Welcome to the Weekly Haat! Local hill farmers bring fresh jhum crops, bamboo shoots, and wild bananas.\n"
                                "Experience authentic local trade culture bro!")
                        elif User_input == "2":
                            print("Welcome to the Fresh Fish Market! Fishermen bring fresh catch straight from the lake boats.\n"
                                "Famous for big lake Rui, Boal, and sweet Chapila fish.")
                        elif User_input == "3":
                            print("Nice choice! Taste hot fried lake fish with local hill chili and red rice.\n"
                                "Enjoy the delicious authentic local food bro!")
                        elif User_input == "4":
                            print("Welcome to Mainimukh Launch Ghat! Big passenger launches connect Langadu to Rangamati Sadar.\n"
                                "Enjoy the scenic 4-hour boat voyage across Kaptai Lake!")
                        else:
                            print("Invalid input. Try again bro.")
                    elif User_input == "no".strip().casefold():
                        print("Ok bro, you can go. Best wishes to you!")
                        #its ok
                    else:
                        print("Invalid Input.Try again.")

                elif User_input == "4":
                    print("Welcome to Kalapakujja Lake Viewpoint. It is one of the most peaceful lakeside viewpoints in Langadu.\n"
                        "It offers wide-open lake horizons and stunning sunset views.")
                    User_input = input("Do you want to explore Kalapakujja Lake Viewpoint ? Yes/No : ")
                    if User_input.strip().casefold() == "yes":
                        print("""In Kalapakujja Viewpoint here is has lots of things to enjoy:
                            1. Mesmerizing Golden Sunset View.
                            2. Lakeside Breeze & Peaceful Relaxing.
                            3. Local Village Life & Dugout Boats.""")
                        User_input = input("Which one do you want to explore? Write serial No: ").strip()
                        if User_input == "1":
                            print("Awesome choice! Watch the golden sun setting over the blue water horizon around 5:30 PM.\n"
                                "A perfect place for photography and meditation.")
                        elif User_input == "2":
                            print("Sit by the bank of Kaptai Lake, feel the cool evening breeze, and relax your mind.\n"
                                "Enjoy your peaceful moment bro!")
                        elif User_input == "3":
                            print("Observe the simple rural lifestyle of local villagers and traditional wooden fishing boats.\n"
                                "Best wishes for your journey!")
                        else:
                            print("Invalid input. Try again bro.")
                    elif User_input == "NO".strip().casefold():

                        print("Ok bro, you can go. Just enjoy!")
                    else:
                        print("Invalid input. try agian.")

                elif User_input == "5":
                    
                    print("Welcome to Duluchhari Waterfall! A hidden natural cascade nestled deep inside lush green forest.\n"
                        "Cold, crystal-clear mountain spring water flows over ancient rock formations.")
                    User_input = input("Do you want to explore Duluchhari Waterfall ? Yes/No : ")
                    if User_input.strip().casefold() == "yes":
                        print("""Here is has lots of adventure activities:
                            1. Rocky Stream & Jungle Trekking (30-45 mins).
                            2. Bathing in Natural Freshwater Rock Pool.
                            3. Bamboo Forest Camping & Sightseeing.""")
                        User_input = input("Which adventure do you want to explore? Enter serial No: ").strip()
                        if User_input == "1":
                            print("Nice choice bro! Trekking through the rocky stream with a local guide is full of adventure.\n"
                                "Be careful with slippery stones and enjoy the trek!")
                        elif User_input == "2":
                            print("Super refreshing! The pure mountain spring water is chilled and rejuvenating.\n"
                                "Take a dive and wash away your tiredness bro!")
                        elif User_input == "3":
                            print("Surrounded by green bamboo groves and wild birds singing.\n"
                                "Take in the raw beauty of nature and enjoy your moment!")
                        else:
                            print("Invalid input. Try again bro.")

                    elif User_input == "no".strip().casefold():
                        print("Ok bro, you can go. Best wishes to you!")

                    else:
                        print("invalid input and try again.")
                        

                else:
                    print("Invalid input . try agian.")

            else:
                print("It's ok As your Wish.")
                
        def Rajasthali(self):
            print("Welcome to Rajasthali Upazila")
            User_input = input("Do you Want to Explore Rajasthali Upazila ? Yes/No : ")
            
            if User_input.strip().casefold() == "yes":
                print("Nice choice! Let's dive into Rajasthali's Favourite and Popular places!")
                print("""Here is has lots of place for Exploring . 
                    
                    1. Ghagrachhari Waterfall & Rocky Stream.
                    2. Bangalhalia & Poitupara Hill Ridge Viewpoint.
                    3. Rajasthali Central Buddhist Vihara & Golden Pagoda.
                    4. Khiyang & Tripura Indigenous Tribal Village.
                    5. Local Hill Fruits Orchards & Tribal Cuisine.""")
                
                User_input = input("Which place do you want to Explore Just write serial NO : ").strip()

                if User_input == "1":
                    print("Nice choice. Ghagrachhari Waterfall is a natural hidden cascade in Rajasthali,\n"
                        "surrounded by ancient rock boulders and deep mahogany-teak forests.")
                    User_input = input("Do you Want to explore more about Ghagrachhari Waterfall ? yes / No : ")
                    if User_input.strip().casefold() == "yes":
                        print("""Here is has lots of way to Explore Ghagrachhari Waterfall:
                            1. Hiking along the Stony Creek Trail.
                            2. Swimming in the Natural Rock Water Pool.
                            3. Photography and Forest Bird Watching.
                            4. Picnic beside the Mountain Stream.""")
                        User_input = input("Which way do you want to Explore? Enter the serial No: ").strip()
                        if User_input == "1":
                            print("Nice choice bro! Trekking through the rocky stream with cold water splashing your feet is awesome.\n"
                                "Watch your step on wet rocks and enjoy the adventurous trek!")
                        elif User_input == "2":
                            print("Awesome! The fresh mountain spring pool is ice-cold and crystal clear.\n"
                                "Take a refreshing bath and wash away all city stress bro!")
                        elif User_input == "3":
                            print("Great choice! You can spot hill hornbills, wild kingfishers, and mountain butterflies.\n"
                                "Keep your camera ready and capture nature's beauty!")
                        elif User_input == "4":
                            print("Wonderful! Sit on the giant flat stones with friends, listen to cascading water sounds, and enjoy food.\n"
                                "Remember not to litter the nature. Enjoy bro!")
                        else:
                            print("Invalid input. Try again man.")
                    else:
                        print("It's ok Bro.")

                elif User_input == "2":
                    print("Welcome to Bangalhalia & Poitupara Hill Ridge! Located on the high mountain road\n"
                        "connecting Rangamati and Bandarban, offering breathtaking views of lush green valleys.")
                    User_input = input("Do you want to Explore Poitupara Viewpoint ? Yes/No : ")
                    if User_input.strip().casefold() == "yes":
                        print("""Here is has lots of services and activities:
                            1. 360-Degree Mountain Valley View.
                            2. Cloud & Mist Floating Over Green Hills (Morning View).
                            3. Scenic Mountain Bike / Bike Ride on the Winding Road.
                            4. Sunset Viewing over the Bandarban-Rangamati Border Hills.""")
                        User_input = input("Which activity do you want to explore? Enter serial No: ").strip()
                        if User_input == "1":
                            print("Nice one! Looking down from the ridge shows endless waves of green mountain slopes.\n"
                                "Take a deep breath of pure hill oxygen and enjoy bro!")
                        elif User_input == "2":
                            print("Awesome! Early morning clouds drift through the valleys beneath your feet like a white blanket.\n"
                                "Best time is 6:00 AM. Enjoy the magical view!")
                        elif User_input == "3":
                            print("Thrilling choice! The roller-coaster mountain road has sharp curves and scenic tree lines.\n"
                                "Drive carefully and feel the cool mountain breeze!")
                        elif User_input == "4":
                            print("Stunning! Watch the golden orange sun sink behind the deep ridge lines.\n"
                                "Relax your soul and take golden hour photos bro!")
                        else:
                            print("Invalid input. Try again bro.")
                    else:
                        print("It's ok bro, as your wish.")

            
                elif User_input == "3":
                    print("Welcome to Rajasthali Central Buddhist Vihara. A sacred and peaceful monastery\n"
                        "featuring an ornate golden pagoda and ancient Buddhist teachings.")
                    User_input = input("Do you want to explore the Vihara ? Yes/No : ")
                    if User_input.strip().casefold() == "yes":
                        print("""In the Buddhist Vihara here is has lots of experiences like :
                            1. Visiting the Golden Buddha Statues & Pagoda.
                            2. Forest Meditation Zone (Quiet Zone).
                            3. Learning Buddhist Cultural History from Monks.
                            4. Architecture & Traditional Wood Carvings.""")
                        User_input = input("Which one do you want to explore? Write serial No: ").strip()
                        if User_input == "1":
                            print("Welcome! The shimmering golden spire of the pagoda on the hill looks peaceful and majestic.\n"
                                "Remember to maintain respect and quietness in the sacred temple.")
                        elif User_input == "2":
                            print("Peaceful choice! Sit under ancient banyan trees and listen to chirping birds.\n"
                                "A perfect place to calm your thoughts and meditate.")
                        elif User_input == "3":
                            print("Great choice! The elder venerable monks share stories of peace, compassion, and hill history.\n"
                                "An enlightening cultural experience bro!")
                        elif User_input == "4":
                            print("Awesome! The monastery pillars feature handmade carvings of lotus and traditional motifs.\n"
                                "Admire the unique indigenous craftsmanship!")
                        else:
                            print("Invalid input. Try again bro.")
                    else:
                        print("Ok bro, you can go. Best wishes to you!")

                elif User_input == "4":
                    print("Welcome to Khiyang & Tripura Village. Rajasthali is the primary homeland of the rare\n"
                        "Khiyang indigenous community, known for their unique language, bamboo stilt houses, and traditions.")
                    User_input = input("Do you want to explore the Tribal Village ? Yes/No : ")
                    if User_input.strip().casefold() == "yes":
                        print("""In the Indigenous Village here is has lots of cultural activities:
                            1. Traditional Bamboo Stilt House (Machang) Architecture.
                            2. Handmade Back-Strap Loom Weaving Experience.
                            3. Traditional Hill Music & Bamboo Flute Melody.
                            4. Interacting with Friendly Village Elders.""")
                        User_input = input("Which one do you want to explore? Write serial No: ").strip()
                        if User_input == "1":
                            print("Fascinating! The houses are raised on sturdy bamboo and wooden poles above the ground for safety.\n"
                                "Built with natural bamboo splits and thatched leaf roofs.")
                        elif User_input == "2":
                            print("Awesome! Village women weave intricate geometric shawls and wraps on wooden back-strap looms.\n"
                                "You can purchase authentic handmade scarves directly from the artisans!")
                        elif User_input == "3":
                            print("Melodious choice! Listen to ancient hill folk tunes played on handcrafted bamboo flutes.\n"
                                "Enjoy the soothing cultural rhythm bro!")
                        elif User_input == "4":
                            print("Heartwarming! The villagers greet visitors with warm smiles and sweet mountain tea.\n"
                                "Learn their heritage and show your respect bro!")
                        else:
                            print("Invalid input. Try again bro.")
                    else:
                        print("Ok bro, you can go. Just enjoy!")

            
                elif User_input == "5":
                    print("Welcome to Rajasthali's Fruit Orchards & Cuisine! Famous for sweet mountain pineapples,\n"
                        "papayas, hill bananas, and authentic tribal delicacy Hebang.")
                    User_input = input("Do you want to explore the Fruits & Food ? Yes/No : ")
                    if User_input.strip().casefold() == "yes":
                        print("""Here is has lots of food and orchard tours:
                            1. Fresh Pineapple & Mountain Fruit Orchard Walk.
                            2. Tasting Traditional Hebang (Leaf-Wrapped Steamed Fish).
                            3. Bamboo Shoot (Bash Korol) Curry with Sticky Red Rice.
                            4. Fresh Hill Honey & Mountain Spiced Tea.""")
                        User_input = input("Which food experience do you want to explore? Enter serial No: ").strip()
                        if User_input == "1":
                            print("Delicious! Walk through hillside pineapple gardens and taste freshly sliced juicy pineapples.\n"
                                "Naturally organic and sweet bro!")
                        elif User_input == "2":
                            print("Super authentic! Fresh creek fish marinated with wild herbs, wrapped in banana leaf, and slow-baked.\n"
                                "A heavenly traditional tribal delicacy!")
                        elif User_input == "3":
                            print("Awesome! Tender bamboo shoots stir-fried with green chilies and served with hot mountain sticky rice.\n"
                                "Enjoy the authentic spicy flavors bro!")
                        elif User_input == "4":
                            print("Soothing! Warm black tea brewed with wild ginger, hill lemon, and drops of pure forest honey.\n"
                                "Recharges your energy instantly!")
                        else:
                            print("Invalid input. Try again bro.")
                    else:
                        print("Ok bro, you can go. Best wishes to you!")

                else:
                    print("Invalid Input. Please try again.")

            else:
                print("It's ok As your Wish.")

        def Jurachhari(self):
            print("Welcome to Jurachhari Upazila")
            User_input = input("Do you Want to Explore Jurachhari Upazila ? Yes/No : ")
            
            if User_input.strip().casefold() == "yes":
                print("Nice choice! Let's dive into Jurachhari's Favourite and Popular places!")
                print("""Here is has lots of place for Exploring . 
                    
                    1. Jurachhari Ghat & Kaptai Lake Gorge Cruise.
                    2. Lulamura Mountain Peak (Mizoram Border View).
                    3. Jurachhari Forest Vihara & Meditation Caves.
                    4. Chalchali & Yakshichhari Crystal Waterfall.
                    5. Traditional Chakma Jhum Culture & Pinon-Hadi Weaving.""")
                
                User_input = input(" Which place do you want to Explore Just write serial NO : ").strip()

                
                if User_input == "1":
                    print("Nice choice. Jurachhari has no direct road connection from Sadar; the only way\n"
                        "is a mesmerizing 3-hour engine boat voyage through narrow lake gorges between high mountains.")
                    User_input = input("Do you Want to explore more about Lake Cruise & Ghat ? yes / No : ")
                    if User_input.strip().casefold() == "yes":
                        print("""Here is has lots of cruise experiences:
                            1. 3-Hour Long Engine Boat Cruise from Rangamati Sadar.
                            2. Narrow Rocky Water Channels & Mountain Reflections.
                            3. Jurachhari Waterfront Bazar & Fresh Fish Landings.
                            4. Sunset over the Calm Lake Waterways.""")
                        User_input = input("Which cruise option do you want to Explore? Enter serial No: ").strip()
                        if User_input == "1":
                            print("Nice choice bro! Sitting on the roof of the wooden engine boat with cool lake wind in your face\n"
                                "is one of the most serene journeys in Bangladesh. Enjoy the cruise!")
                        elif User_input == "2":
                            print("Breathtaking! As the boat navigates through deep mountain gorges, towering green hills rise on both sides.\n"
                                "Keep your camera rolling bro!")
                        elif User_input == "3":
                            print("Welcome to the Ghat! Local boatmen and villagers bring fresh lake fish and forest vegetables.\n"
                                "Experience authentic riverside hill life!")
                        elif User_input == "4":
                            print("Magical! The entire lake water turns into a mirror of purple and gold during sunset.\n"
                                "Relax your mind and cherish the moment!")
                        else:
                            print("Invalid input. Try again man.")
                    else:
                        print("It's ok Bro.")

                elif User_input == "2":
                    print("Welcome to Lulamura Peak! The highest mountain summit in Jurachhari Upazila,\n"
                        "offering an unhindered panorama of the Lushai Hills of Mizoram (India) across the border.")
                    User_input = input("Do you want to Explore Lulamura Peak ? Yes/No : ")
                    if User_input.strip().casefold() == "yes":
                        print("""Here is has lots of peak trekking activities:
                            1. High Mountain Ridge Trekking (1-Hour Hike).
                            2. International Border Mountain Panorama (Mizoram Hills).
                            3. Cloud Floating & Sunrise Watch over Distant Peaks.
                            4. Camping on the Hilltop under Starlit Sky.""")
                        User_input = input("Which activity do you want to explore? Enter serial No: ").strip()
                        if User_input == "1":
                            print("Nice one! Trekking up the narrow mountain path surrounded by wild ferns and bamboo.\n"
                                "Take a local guide and stay hydrated on the hike bro!")
                        elif User_input == "2":
                            print("Spectacular! From the summit, you can gaze across miles of rolling blue ridges inside India's Mizoram.\n"
                                "A true explorer's view!")
                        elif User_input == "3":
                            print("Awesome! The sunrise paints the high peaks in golden light while misty clouds roll in valleys.\n"
                                "Enjoy the heavenly morning atmosphere!")
                        elif User_input == "4":
                            print("Unforgettable! Camping on the mountain summit with a bonfire, cool breeze, and million stars.\n"
                                "Be safe and make great memories bro!")
                        else:
                            print("Invalid input. Try again bro.")
                    else:
                        print("It's ok bro, as your wish.")

                elif User_input == "3":
                    print("Welcome to Jurachhari Sadhanananda Forest Vihara. A sacred Buddhist pilgrimage\n"
                        "place deep in nature where monks meditate in forest caves and quiet huts.")
                    User_input = input("Do you want to explore the Forest Vihara ? Yes/No : ")
                    if User_input.strip().casefold() == "yes":
                        print("""In the Forest Vihara here is has lots of spiritual experiences :
                            1. Visiting the Main Buddha Sanctuary & Sacred Bodhi Tree.
                            2. Natural Rock Meditation Caves (Kuti).
                            3. Spiritual Peace & Sound of Nature (Silence Zone).
                            4. Listening to Dhamma Teachings from Monk Elders.""")
                        User_input = input("Which one do you want to explore? Write serial No: ").strip()
                        if User_input == "1":
                            print("Welcome! Walk barefoot on the clean temple grounds and offer flowers at the Buddha statue.\n"
                                "Feel instant inner calmness and peace bro.")
                        elif User_input == "2":
                            print("Fascinating! Natural stone caves where Buddhist monks practice deep insight meditation (Vipassana).\n"
                                "A center of high spiritual devotion!")
                        elif User_input == "3":
                            print("Soothing! The absolute silence broken only by rustling leaves and forest wind.\n"
                                "Relax your mind from all city hustle!")
                        elif User_input == "4":
                            print("Great choice! Learn lessons on universal compassion (Metta), non-violence, and mindfulness.\n"
                                "Best wishes for your spiritual journey bro!")
                        else:
                            print("Invalid input. Try again bro.")

                    elif User_input == "No".strip().casefold():
                        print("I's ok bro. i wish you came next time!")
                    else:
                        print("Invaild input. try again.")

                elif User_input == "4":
                    print("Welcome to Chalchali & Yakshichhari Waterfall! An untamed natural cascade hidden in\n"
                        "deep virgin rain forests, flowing with chilled turquoise spring water.")
                    User_input = input("Do you want to explore the Waterfall ? Yes/No : ")
                    if User_input.strip().casefold() == "yes":
                        print("""Here is has lots of wild waterfall adventures:
                            1. Forest Trail & Creek Walk (45-Minute Trek).
                            2. Showering under the Roaring Spring Water.
                            3. Exploring Ancient Rock Formations & Green Moss Gorges.
                            4. Wildlife & Butterfly Spotting along the Stream.""")
                        User_input = input("Which adventure do you want to explore? Enter serial No: ").strip()
                        if User_input == "1":
                            print("Adventurous choice! Follow the clear stony water stream through deep canopy trees.\n"
                                "Wear good grip sandals and enjoy the wild trek bro!")
                        elif User_input == "2":
                            print("Incredible! Stand under the cold cascading mountain water for an exhilarating natural shower.\n"
                                "Pure, refreshing, and energizing!")
                        elif User_input == "3":
                            print("Awesome! The stone walls are covered with emerald green moss and wild climbing orchids.\n"
                                "Capture stunning nature shots with your camera!")
                        elif User_input == "4":
                            print("Nature lover's dream! Giant colorful forest butterflies flutter around the clear stream pools.\n"
                                "Enjoy the pristine wilderness bro!")
                        else:
                            print("Invalid input. Try again bro.")
                    elif User_input == "no".strip().casefold():
                        print("Ok bro, you can go. Just enjoy")
                    else:
                        print("It's ok no problem !")

                elif User_input == "5":
                    print("Welcome to Chakma Cultural Heritage in Jurachhari! Famous for authentic back-strap loom\n"
                        "Pinon-Hadi weaving, traditional Jhum hill farming, and indigenous delicacies.")
                    User_input = input("Do you want to explore Chakma Culture & Cuisine ? Yes/No : ")
                    if User_input.strip().casefold() == "yes":
                        print("""Here is has lots of cultural activities:
                            1. Watching Traditional Pinon-Hadi Handloom Weaving.
                            2. Organic Jhum Hill Farming (Jhum Rice, Corn & Melons).
                            3. Tasting Traditional Pajon & Creek Fish in Bamboo Stalk.
                            4. Pure Wild Forest Honey Tasting.""")
                        User_input = input("Which cultural experience do you want to explore? Enter serial No: ").strip()
                        if User_input == "1":
                            print("Artistic! Local Chakma artisans weave traditional red and black geometric patterns (Chabuk) on wooden looms.\n"
                                "You can collect authentic handmade Pinon-Hadi souvenirs!")
                        elif User_input == "2":
                            print("Fascinating! Walk along hillside Jhum farms where aromatic binni rice, pumpkin, and hill chillies grow naturally.\n"
                                "100% pesticide-free and organic!")
                        elif User_input == "3":
                            print("Mouthwatering! Savor authentic Pajon (mixed 30-herb vegetable stew) and fresh stream fish cooked inside bamboo.\n"
                                "Enjoy the rich tribal flavors bro!")
                        elif User_input == "4":
                            print("Sweet! Taste freshly harvested wild forest honey collected from deep jungle trees.\n"
                                "Pure, natural, and energetic bro!")
                        else:
                            print("Invalid input. Try again bro.")
                    elif User_input == "no".strip().casefold():
                        print("Ok bro, you can go. Best wishes to you!")
                    else:
                        print("Invalid input. Try again.")

            
                else:
                    print("Invalid Input. Please try again.")

            else:
                print("It's ok As your Wish.")

    class Select_Sub_District(Show_Datails):
            def Exit_game(self):
                       
                            User_input = input("Do you want to Exit game ? Yes/No :")
                            if User_input == "Yes".strip().casefold():
                                print("The game is Ended.")
                                exit()
                            else:
                                print("It's ok lets play again.")
            
            def select_sub_sistrict(self):
               
                    

                while True:
                    

                    About_Distric.About_Rangamti_sub_district()

                    User_input = input("Which Sub District Do you want to Explore Select just Serial No :").strip()
                    if User_input == "1":
                        self.Rangamti_sadar()
                        self.Exit_game()
                        
                    elif User_input == "2":
                        
                        self.Baghaichaari()
                        self.Exit_game()
                    elif User_input == "3":
                        self.Kaptai()
                        self.Exit_game()
                    elif User_input == "4":
                        self.kawkali()
                        self.Exit_game()
                    elif User_input == "5":
                        self.barkal()
                        self.Exit_game()
                    elif User_input == "6":
                        self.Langadu()
                        self.Exit_game()
                    elif User_input == "7":
                        self.Naniarchar()
                        self.Exit_game()
                    elif User_input == "8":
                        self.Rajasthali()
                        self.Exit_game()
                    elif User_input == "9":
                        self.Jurachhari()
                        self.Exit_game()
                    elif User_input == "10":
                        self.Bilaichari()
                        self.Exit_game()
                    else:
                        print("Invalid input try Again.")
                    
                        
                    
                    if User_input == "11":
                        print("The game is Ented.")
                        break
                    # else:
                    #     print("invalid input.")

                
                    pass
       
    
       
    # a =About_Distric.About_Rangamti_sub_district()
    # About_Distric.About_Rangamti_sub_district()
    b = Select_Sub_District()
    
    b.select_sub_sistrict()

    # Show_Datails.Rangamti_sadar()
    # show_datalis =Select_Sub_District.Baghaichaari()
    # show_datalis = Select_Sub_District.Kaptai()
    # show_datalis = Select_Sub_District.kawkali()
    # show_datalis = Select_Sub_District.Naniarchar()
    # show_datalis = Select_Sub_District.barkal()
    # show_datalis = Select_Sub_District.Bilaichari()
    # Show_Datails = Select_Sub_District.Langadu()
    # Show_Datails = Select_Sub_District.Rajasthali()
    # Show_Datails = Select_Sub_District.Jurachhari()
             
        

        

else:
    print("The game is Ended")





