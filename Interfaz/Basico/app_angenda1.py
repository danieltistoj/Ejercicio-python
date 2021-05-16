from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Agenda")
root.geometry("700x500")
colorFondo = "#006"
colorLetra = "#FFF"
root.configure(bg=colorFondo)


nombre = StringVar()
apellido = StringVar()
correo = StringVar()
telefono = StringVar()
eliminar = StringVar()

tituloEtiqueta = Label(root, text="Mi aplicacion",fg=colorLetra,bg=colorFondo)
tituloEtiqueta.place(x=270,y=10)

nombreEtiqueta = Label(root, text="Nombre",fg=colorLetra,bg=colorFondo)
nombreEtiqueta.place(x=50,y=50)

entrada1 = Entry(root,textvariable=nombre)
entrada1.place(x=150,y=50)

apellidoEtiqueta = Label(root, text="Apellido",fg=colorLetra,bg=colorFondo)
apellidoEtiqueta.place(x=50,y=80)

entrada2 = Entry(root,textvariable=apellido)
entrada2.place(x=150,y=80)

telefonoEtiqueta = Label(root, text="Telefono",fg=colorLetra,bg=colorFondo)
telefonoEtiqueta.place(x=50,y=140)

entrada3 = Entry(root,textvariable=telefono)
entrada3.place(x=150,y=140)

correoEtiqueta = Label(root, text="Correo",fg=colorLetra,bg=colorFondo)
correoEtiqueta.place(x=50,y=170)

entrada3 = Entry(root,textvariable=correo)
entrada3.place(x=150,y=170)

eliminarEtiqueta = Label(root, text="Eliminar",fg=colorLetra,bg=colorFondo)
eliminarEtiqueta.place(x=370,y=50)

spinTelefono = Spinbox(root,text=eliminar)
spinTelefono.place(x=450,y=50)

botonGuardar  = Button(root,text="Guardar",fg=colorLetra,bg=colorFondo)
botonGuardar.place(x=180,y=200)

botonEliminar  = Button(root,text="Eliminar",fg=colorLetra,bg=colorFondo)
botonEliminar.place(x=490,y=80)

root.mainloop()