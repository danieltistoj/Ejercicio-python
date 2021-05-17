from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def agregarContacto():
    #print(entrada1.get())
    if len(entrada1.get())>0 and len(entrada3.get())>0:
        tabla.insert('','end',text='',value=(entrada1.get(),entrada2.get(),entrada3.get(),entrada4.get()))
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        entrada3.delete(0,END)
        entrada4.delete(0,END)

        #print(contador)

    else:
        messagebox.showwarning("Atencion", message="Debe de tener un nombre y un numero de telefono")



root = Tk()
root.title("Agenda")
root.geometry("700x500")
colorFondo = "#006"
colorLetra = "#FFF"
root.configure(bg=colorFondo)

contador = 0

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

entrada4 = Entry(root,textvariable=correo)
entrada4.place(x=150,y=170)

eliminarEtiqueta = Label(root, text="Eliminar",fg=colorLetra,bg=colorFondo)
eliminarEtiqueta.place(x=370,y=50)

spinTelefono = Spinbox(root,text=eliminar)
spinTelefono.place(x=450,y=50)

botonGuardar  = Button(root,text="Guardar",fg=colorLetra,bg=colorFondo,command = agregarContacto)
botonGuardar.place(x=180,y=200)

botonEliminar  = Button(root,text="Eliminar",fg=colorLetra,bg=colorFondo)
botonEliminar.place(x=490,y=80)

columns = ('#1','#2','#3','#4')
tabla = ttk.Treeview(root,column=columns,show='headings')
tabla.place(x=0,y=250)

tabla.heading(columns[0],text="Nombre",anchor=CENTER)
tabla.heading(columns[1],text="Apellido",anchor=CENTER)
tabla.heading(columns[2],text="Telefono",anchor=CENTER)
tabla.heading(columns[3],text="Correo",anchor=CENTER)

tabla.column(columns[0],width=175,anchor=CENTER)
tabla.column(columns[1],width=175,anchor=CENTER)
tabla.column(columns[2],width=175,anchor=CENTER)
tabla.column(columns[3],width=175,anchor=CENTER)

root.mainloop()