

from time import strftime
import tkinter as tk

root = tk.Tk()
root.title("Digital Clock!")
def Time_def():
    time =strftime("%I:%M:%S %p \n %d/%m/%y")
    Love.config(text = time)
    Love.after(1000,Time_def)
Love = tk.Label(root,foreground= "yellow",background = "black",font = ("arial",55,"bold"))
Love.pack()
Time_def()
root.mainloop()