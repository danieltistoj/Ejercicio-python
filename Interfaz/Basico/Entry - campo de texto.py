from tkinter import *

root = Tk()
root.title("Entrada")
root.geometry("300x300")
root.resizable(0,0)#Para que el usuario no modifique la ventana

nombre = StringVar()
apellido = StringVar()
saludo = StringVar()

nombre.set("Escribe aqui tu nombre")
apellido.set("Escribe aqui tu apellido")

def saludar():
    #print("Hola",nombre.get(),apellido.get())
    saludo.set("Hola "+nombre.get()+" "+apellido.get())

#bd = borde, bg = color, font = fuente

etiqueta1 = Label(root,text="Escribe aqui tu nombre: ",bd = 4,bg="red",font=("Curier 10"))
etiqueta1.place(x=10, y=10)
entrada1 = Entry(root,textvariable=nombre,bd=5)
entrada1.place(x=170,y=10)

etiqueta2 = Label(root,text="Escribe aqui tu apellido: ",bd = 4,bg="red",font=("Curier 10"))
etiqueta2.place(x=10, y=40)
entrada2 = Entry(root,textvariable=apellido,bd=5)
entrada2.place(x=170,y=40)

boton = Button(root,text="Saludar ahora",command=saludar,bd=5,bg="blue")
boton.place(x=10,y=100)
#state = disable -> para que el area de texto no pueda ser modificada
entrada3 = Entry(root,bd=20,font=("Curier 10"),textvariable=saludo,state="disable")
entrada3.place(x=70,y=221)
root.mainloop()