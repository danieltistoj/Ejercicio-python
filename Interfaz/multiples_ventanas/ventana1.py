from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import main

class Ventana:
    def __init__(self):
        ventana = Tk()
        ventana.title("Ventana 1")

        Label(ventana,text="Ventana Uno").grid(row=0,column=0)

        #self.btnVentanaMain = Button(ventana, text="ventna main", command=self.ventanaMain)
        #self.btnVentanaMain.grid(row=1,sticky=W+E)

        ventana.mainloop()


#ventana = Ventana()