from tkinter import *
def agregar():
    listaProductos.insert(END,entrada.get())
root =Tk()
root.geometry("400x400")

productos = Label(root,text="Productos")
productos.pack()

listaProductos = Listbox(root,width=50)
listaProductos.insert(0,"Carne")
listaProductos.insert(1,"Pollo")
listaProductos.insert(2,"Verdura")
listaProductos.insert(3,"Jugo")
listaProductos.pack()

#Eliminar productos
listaProductos.delete(0)

entrada = Entry(root,bd=20)
entrada.pack()
boton = Button(root,text="Agragar",bd=10,command=agregar)
boton.pack()


root.mainloop()