
import tkinter as tk

root = tk.Tk( )
label = tk.Label(root,text = "Angel Chakma",background = ('black'),foreground= ("red"),font= (" ",30,"bold"))
name = tk.Label(root, text = ("Rangamati Govt College"),background = ("pink"),foreground = ("black"),font = (" ",30,"bold"))
label.pack(anchor= "center")
name.pack(anchor= "center")
root.mainloop()