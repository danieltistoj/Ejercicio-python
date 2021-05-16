from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x300")

w = Spinbox(root,values=("Python","HTML5","Java","JavaScript"))
w.pack()

e = Spinbox(root,values=("carne","verdura","pasta"))
e.pack()
root.mainloop()