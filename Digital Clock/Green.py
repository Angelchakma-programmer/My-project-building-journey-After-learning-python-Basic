

#Green colors Digital Clock.
from time import strftime
import tkinter as Structure

root = Structure.Tk()
root.title("Angel Chakma")
def Time_def():
    Labeling.config( text = strftime("%I:%M:%S %p  \n %d/%m/%y"))
    Labeling.after(1000,Time_def)
    pass

Labeling = Structure.Label( root,background= 'black',foreground= "#0AFF22",font=  ("arial",55,"bold"))

Labeling.pack(anchor= "center")
Time_def()

root.mainloop()