import tkinter as tk
from tkinter import ttk
def seleccionar(opcion):
    print(opcion)

root = tk.Tk()

#Se escribe lambda cuando recibimos parametros
ttk.Button(root, text = "Python", command=lambda: seleccionar("Python")).pack()
ttk.Button(root, text = "Java", command=lambda: seleccionar("Java")).pack()
ttk.Button(root, text = "JavaScript", command=lambda: seleccionar("JavaScript")).pack()

root.mainloop()