

# Second = 10
# Miniute = 1
# hours = 3
import time

user_time = int(input("Eneter your time :"))


while True:
    Miniute,Second = divmod(user_time,60)
    times =  " {:02d} M: {:02d}".format(Miniute,Second)
    time.sleep(1)
    print(f"{times} S",end= " \r")
    user_time -= 1
    if user_time == -1:
        print("\nTime is UP")
        break

