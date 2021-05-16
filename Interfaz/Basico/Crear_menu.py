from tkinter import *
from tkinter import messagebox
def cerrar():
    messagebox.askquestion("Cerrar",message="¿Esta segura de cerrar?")
def licencia():
    messagebox.showinfo("version",message="Version 1.0")
def error():
    messagebox.showerror("Error",message="Se encontro un error")
def antencion():
    messagebox.showwarning("Atencion",message="Se borrara el actual")


root = Tk()
menuBar = Menu(root)
root.config(menu=menuBar)

archivoMenu = Menu(menuBar,tearoff=0)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir",command=antencion)
archivoMenu.add_command(label="Guardar",command=error)
archivoMenu.add_command(label="Cerrar",command=cerrar)
archivoMenu.add_separator()
#root.quit es para cerrar la ventana
archivoMenu.add_command(label="Salir",command=root.quit)

editMenu = Menu(menuBar,tearoff=0)

editMenu.add_command(label="Cortar")
editMenu.add_command(label="Copiar")
editMenu.add_command(label="Pegar")
#tearoff es para quitar un separador que aparece al inicio de cada opcion del menu
#que es un linea punteada
ayuadaMenu = Menu(menuBar,tearoff=0)
ayuadaMenu.add_command(label="Ayuda",command=licencia)
ayuadaMenu.add_separator()

menuBar.add_cascade(label="Archivo",menu=archivoMenu)
menuBar.add_cascade(label="Editar",menu=editMenu)
menuBar.add_cascade(label="Ayuda",menu=ayuadaMenu)





root.mainloop()