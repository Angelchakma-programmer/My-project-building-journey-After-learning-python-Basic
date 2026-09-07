

import tkinter as tk
from time import strftime




root = tk.Tk()
root.title("Digital Clock")

def Date_time():
    Fortamting_time = strftime("%I:%M:%S %p \n %d/%b/%Y")

    l.config(text = Fortamting_time)
    l.after(1000,Date_time)
l = tk.Label(root,font = ("Calibri",40,"bold"),background = "#081402",foregroun = "#E8144D")
l.pack(anchor = "center")
name = tk.Label(root, background = ("pink"),foreground= "#000006",text = "Angel Chakma \n Department of physics\n Rangamati Govt College")
name.pack(anchor= "center")
Date_time()
root.mainloop()