

# #This is my Second time build digital clock. and it's me Angel Chakma

# import tkinter as tk  #This is Grapical user interface model .
# from time import strftime

# Acces_Tkinter  = tk.Tk()

# Acces_Tkinter.title("Digital Clock !")

# def Date_time():
#     Formating_DateTime = strftime("%I:%M:%S %p \n %d/%b/%y")

#     Logic.config(text = Formating_DateTime)
#     Logic.after(1000,Date_time)

# Logic = tk.Label(Acces_Tkinter,font=("calibri",60,"bold"), background= "black",foreground= "Yellow")
    
# Logic.pack(anchor = "center")
# Date_time()

# Acces_Tkinter.mainloop(

# )
from time import strftime
import tkinter

Root = tkinter.Tk()
Root.title("Digial Clock !")

def time_function():
    formatng_string = strftime("%I:%M:%S %p \n %d/%b/%y")
    label.config(text = formatng_string)
    label.after(1000,time_function)
    
label = tkinter.Label(Root,background= ("black"),foreground= ("red"),font= ("calabri",60,"bold"))

label.pack(anchor="center")

time_function()


Root.mainloop()