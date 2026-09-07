


from time import strftime
import tkinter as tk

root = tk.Tk()
root.title("Angel Chakma")

def Time_Function():
    format_time =  strftime("%I:%M:%S %p \n %d/%m/%y")
    L.config(text= format_time)
    L.after(1000,Time_Function)
    

L = tk.Label(root,background="white",foreground= "blue",font= ("arial",55,"bold"))
L.pack(anchor= "center")
Time_Function()
root.mainloop()