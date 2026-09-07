

#This Digital Clock Created by Angel Chakma. 
#And this clock clours is White.
import tkinter as tk
from time import strftime

Access_tkinter = tk.Tk()
Access_tkinter.title("Angel Chakma ")
def time():
    format_time = strftime("%I:%M:%S %p \n %d/%m/%y")
    make_label.config( text=format_time)
    make_label.after(1000,time)


    


make_label = tk.Label(Access_tkinter,background= "black",font= ("arial",55,"bold"),foreground= "white")
make_label.pack(anchor= "center")
time()

Access_tkinter.mainloop()