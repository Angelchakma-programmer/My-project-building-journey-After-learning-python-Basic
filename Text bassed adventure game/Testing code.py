def kawkali():
            print("Hey , Welcome to The Kawakali Upazila.")
            User_input = input("Do you want to Exlplore Kawkalli Upzalila ? Yes/No :")
            if User_input == "yes".casefold().strip():
                print("Nice chose. i whis have a Best Explore.")
                print("""Here is Popular place name :
                      1.Gagra Barar.
                      2.Pahari Chora.""")
                
                User_input = int(input("Which plaece Are you want explore just write this serial No :"))

                if User_input == 1:
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

                elif User_input == 2:

                    print("""The pahari chora it's Place located in kawkali in Rangamti.\n"
                        "Here is a has lots of Mind Relaxing place Like :
                        1. Fresh and cool Water
                        2. Tracking in Mountain.
                        3. Gagra Kolabagan Waterfall.
                        """)
                    User_input = input("Do you Want to Explore This Place ? Yes/No :")
                    if User_input == "yes".strip().casefold():
                        print("Nich Chose ! ")
                        User_input == int(input("Which Place are you want explore just write This place serial No :"))

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


                    

                        
                # else:
                #     print("It's ok no Problem.")
               


            else:
                print("Ok no problem .")

kawkali()
