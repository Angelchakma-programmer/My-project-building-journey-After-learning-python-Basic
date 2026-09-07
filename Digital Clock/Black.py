

#This is Black colours 

from time import strftime
import tkinter as tk

root = tk.Tk()
root.title("Angel Chakma. Digital Clock.")

def Time():
    format_times = strftime("%I:%M:%S %p \n %d/%b/%y")
    Make_label.config(text = format_times)
    Make_label.after(1000,Time)



Make_label = tk.Label(root,foreground="black",background = "White",font = ("arial",55,"bold"))
Make_label.pack(anchor= "center")
Time()
root.mainloop()