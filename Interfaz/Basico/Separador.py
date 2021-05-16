import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.resizable(False,False)
root.title('Separador')
ttk.Label(root,text='Mi primer label').pack()
separador = ttk.Separator(root,orient='horizontal')
separador.pack(fill="x")
ttk.Label(root,text="Mi segunda Label").pack()




root.mainloop()