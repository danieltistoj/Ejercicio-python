from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ventana1
import ventana2

class Ventana:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Ventana principal")

        Label(self.ventana, text="ventana principal").grid(row=0, column=0)

        self.btnVentana1 = Button(self.ventana, text="ventana uno", command=self.ventanaUno)
        self.btnVentana1.grid(row=1, sticky=W + E)

        self.btnVentana2 = Button(self.ventana, text="ventana dos", command=self.ventanaDos)
        self.btnVentana2.grid(row=2, sticky=W + E)

        self.ventana.mainloop()


    def ventanaUno(self):
        ventana1.Ventana()

    def ventanaDos(self):
        ventana2.Ventana()

        pass





