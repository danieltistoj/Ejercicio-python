from tkinter import *
def Orden():
    lista=""
    if(queso.get()):
        lista+="Con queso"
    else:
        lista+="sin queso"
    if(lechuga.get()):
        lista+=" Con lechuga"
    else:
        lista+=" Sin lechuga"
    imprimir.config(text=lista)

root = Tk()
#bd = borde
root.config(bd=20,bg="goldenrod3")
root.title("Casa de comidas")

queso = IntVar()
lechuga = IntVar()


imagen = PhotoImage(file="hamburguesa.png")
Label(root,image=imagen).pack(side = LEFT)
#frame organiza los demas elementos
frame = Frame(root)
frame.pack(side=RIGHT)
frame.config(bg="goldenrod3")
Label(frame,text="¿Como quieres tu hamburguesa",bg="goldenrod3",font="Curier 15").pack(anchor="w")

Checkbutton(frame,text="Con queso",variable=queso,onvalue=1,offvalue=0
            ,bg="goldenrod3",font="Curier 15",command=Orden).pack(anchor="w")
Checkbutton(frame,text="Con lechuga",variable=lechuga,onvalue=1,offvalue=0
            ,bg="goldenrod3",font="Curier 15",command=Orden).pack(anchor="w")

imprimir = Label(frame,bg="goldenrod3")
imprimir.config(font="Curier 20")
imprimir.pack()




root.mainloop()
