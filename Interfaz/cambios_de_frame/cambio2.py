from tkinter import *
try:
    import Tkinter as tk
except:
    import tkinter as tk

#la clase muestaAplicacion hereda de la clase tk.Tk
#esta clse sera una hija de esta la clase tk.Tk
class muestraAplicacion(tk.Tk):
    def __init__(self):
        #En el constructor se debe ded inicializar la clase Tk
        #por eso se realiza la siguiente sentencia
        tk.Tk.__init__(self)
        self.geometry("1000x500")
        menuBar = Menu(self)
        self.config(menu=menuBar)

        inicioMenu = Menu(menuBar, tearoff=0)
        inicioMenu.add_command(label="Pagina inicial",command=lambda: self.cambioDeFrame(frameInicial))
        inicioMenu.add_command(label="Iniciar Sesion")
        inicioMenu.add_command(label="Cerrar Sesion")


        inventarioMenu = Menu(menuBar,tearoff=0)
        inventarioMenu.add_command(label="Material",command=lambda: self.cambioDeFrame(frameMaterial))
        inventarioMenu.add_command(label="Producto",command=lambda: self.cambioDeFrame(frameProducto))

        clienteMenu = Menu(menuBar,tearoff=0)
        clienteMenu.add_command(label="Cliente",command=lambda: self.cambioDeFrame(frameCliente))
        clienteMenu.add_command(label="Historial",command=lambda:self.cambioDeFrame(frameHistorialCliente))

        menuBar.add_cascade(label="Inicio",menu = inicioMenu)
        menuBar.add_cascade(label="Inventario",menu=inventarioMenu)
        menuBar.add_cascade(label="Cliente",menu=clienteMenu)
        #El frame se deja como nulo
        self._frame = None
        #hacemos un cambio de  frame en donde inicialmente sera de tipo principal
        self.cambioDeFrame(frameInicial)

    def cambioDeFrame(self,tipo_de_frame):
        nuevo_frame = tipo_de_frame(self)
        #Si el frame no es nulo se debe de destruir, para poner el nuevo frame
        if self._frame is not None:
            print("entro")
            self._frame.destroy()
        #El frame ahora sera del tipo de frame que enviamos
        self._frame = nuevo_frame
        #Se agrega el frame a la ventana
        self._frame.pack()


class frameInicial(tk.Frame):
    def __init__(self, principal):
        tk.Frame.__init__(self)
        tk.Label(self,text="Pagina Inicial").pack()
        #tk.Button(self,text="Pagina Uno",command=lambda: principal.cambioDeFrame(framePaginaUno)).pack()
        #tk.Button(self,text="Pagina Dos",command=lambda: principal.cambioDeFrame(framePaginaDos)).pack()


class frameMaterial(tk.Frame):
    def __init__(self,principal):
        tk.Frame.__init__(self,bg="red")
        tk.Label(self,text="Material").pack()
        #tk.Button(self,text="Regresar a principal",command=lambda: principal.cambioDeFrame(frameInicial)).pack()

class frameProducto(tk.Frame):
    def __init__(self,principal):
        tk.Frame.__init__(self)
        tk.Label(self,text="Producto").pack()
        #tk.Button(self,text="Regresar a principal",command=lambda: principal.cambioDeFrame(frameInicial)).pack()

class frameCliente(tk.Frame):
    def __init__(self,principal):
        tk.Frame.__init__(self)
        tk.Label(self,text="Cliente").pack()

class frameHistorialCliente(tk.Frame):
    def __init__(self,principal):
        tk.Frame.__init__(self)
        tk.Label(self,text="Historial cliente").pack()

class frameProveedor(tk.Frame):
    def __init__(self,principal):
        tk.Frame.__init__(self)
        tk.Label(self,text="Proveedor")

if __name__ == "__main__":
    aplicacion = muestraAplicacion()
    aplicacion.mainloop()

