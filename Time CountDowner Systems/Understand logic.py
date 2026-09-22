

# import time
# user_input  = int(input("Enter you Sleep time :"))
# while user_input != 0:
#     print("IT's me Angel Chakma.")
#     time.sleep(1 )
#     user_input -=1

import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  # Overwrite the line each second
        time.sleep(1)
        t -= 1

    print("Fire in the hole!!")

t = input("Enter the time in seconds: ")

countdown(int(t))