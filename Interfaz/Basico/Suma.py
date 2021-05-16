from tkinter import *

root = Tk()
root.title("Suma")
root.geometry("400x250")

primer_numero = IntVar()
segundo_numero = IntVar()

def sumar():
    suma = primer_numero.get() + segundo_numero.get()
    etiqueta3 = Label(root,text="resultado: ")
    etiqueta3.place(x=50,y=150)

    etiqueta4 = Label(root, text=suma)
    etiqueta4.place(x=120, y=150)

def restar():
    suma = primer_numero.get() - segundo_numero.get()
    etiqueta3 = Label(root,text="resultado: ")
    etiqueta3.place(x=50,y=150)

    etiqueta4 = Label(root, text=suma)
    etiqueta4.place(x=120, y=150)

def multiplicar():
    suma = primer_numero.get() * segundo_numero.get()
    etiqueta3 = Label(root,text="resultado: ")
    etiqueta3.place(x=50,y=150)

    etiqueta4 = Label(root, text=suma)
    etiqueta4.place(x=120, y=150)


etiqueta1 = Label(root,text="Engrese el primer numero:")
etiqueta1.place(x=50,y=0)
entrada1 = Entry(root,textvariable=primer_numero)
entrada1.place(x=200,y=0)

etiqueta2 = Label(root,text="Engrese el segundo numero:")
etiqueta2.place(x=50,y=50)
entrada2 = Entry(root,textvariable=segundo_numero)
entrada2.place(x=210,y=50)

boton1 = Button(root,text="Sumar",command= sumar)
boton1.place(x=50,y=100)

boton2 = Button(root,text="restar",command= restar)
boton2.place(x=150,y=100)

boton3 = Button(root,text="multiplicar",command= multiplicar)
boton3.place(x=250,y=100)

root.mainloop()