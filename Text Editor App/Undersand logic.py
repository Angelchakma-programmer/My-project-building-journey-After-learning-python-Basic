

import tkinter as tk
root = tk.Tk()
root.title("Text Editor")

root.geometry("600x600")
text = tk.Text(root,tk.WORD,font = ("arial",12),fg = "white")
root.mainloop()