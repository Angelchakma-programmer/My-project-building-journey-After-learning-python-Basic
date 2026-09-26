

# #UnderStanding time fucntiion. and Convert

# def convert(seconds):
#     seconds = seconds % (24 * 3600)
#     hour = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60
    
#     return "%d:%02d:%02d" % (hour, minutes, seconds)

# # Driver program
# n = int(input("Enter your Time : \n"
#               "\n must be in Seocnd :"))
# print(convert(n))


# # print(3%3) #This is Bagses

# # print(3/3) #This is Divison.
# # print(3//3) #This is only Divison value without decimal numbers
Seconds = int(input("Enter your time :"))
def Convert_time():
    Time = Seconds % (24 * 3600)
    Hours = Time // 3600
    Time = Time % 3600
    Miniute = Time // 60
    Time = Time % 60
    second = Time
    
    print(f"time CountDown is :  ", end= "\r")

Convert_time()

