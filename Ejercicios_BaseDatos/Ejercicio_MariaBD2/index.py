from tkinter import *
from tkinter import ttk
import mariadb

class Cliente:
    def __init__(self,ventana):
        self.vetana = ventana
        self.vetana.title("Cliente")

        marco = LabelFrame(self.vetana,text="Cliente")
        #pady significa que tendra 20 espacios arriba y 20 espacios abajo
        marco.grid(row=0,column=0,columnspan=6,pady=20)

        Label(marco,text="Nombre").grid(row=0,column=0) #label
        Entry(marco).grid(row=0,column=1) #area de texto

        Label(marco, text="Apellido").grid(row=1, column=0)
        Entry(marco).grid(row=1, column=1)

        Label(marco, text="NIT").grid(row=2, column=0)
        Entry(marco).grid(row=2, column=1)

        Label(marco, text="Telefono").grid(row=3, column=0)
        Entry(marco).grid(row=3, column=1)

        Label(marco, text="Correo").grid(row=4, column=0)
        Entry(marco).grid(row=4, column=1)

        #boton
        #columspan significa que el boton va a abarcar 2 columnas
        #sticky significa que el boton va a ocupar de este a oeste
        ttk.Button(marco,text="Guardar",command=self.mostrarDatos).grid(row=4,columnspan=2,sticky=W+E)
        #Tabla
        #posible error: https://es.stackoverflow.com/questions/345051/error-out-of-range-insertando-una-tabla
        columns = ('#1','#2','#3','#4','#5','#6')
        self.tabla = ttk.Treeview(self.vetana,columns=columns,show='headings')

        self.tabla.grid(row=4,column=0,columnspan=2)
        #para los encabezados
        self.tabla.heading("#1",text="ID",anchor=CENTER)
        self.tabla.heading("#2",text="Nombre",anchor=CENTER)
        self.tabla.heading("#3",text="Apellido",anchor=CENTER)
        self.tabla.heading("#4",text="NIT",anchor=CENTER)
        self.tabla.heading("#5",text="Telefono",anchor=CENTER)
        self.tabla.heading("#6", text="Correo",anchor=CENTER)

        #para los datos de cada columna
        self.tabla.column("#1",  anchor=CENTER)
        self.tabla.column("#2",  anchor=CENTER)
        self.tabla.column("#3",  anchor=CENTER)
        self.tabla.column("#4",  anchor=CENTER)
        self.tabla.column("#5", anchor=CENTER)
        self.tabla.column("#6", anchor=CENTER)


    def consultaCliente(self,query):
        registros = self.tabla.get_children()#obtenemos la cantidad de datos en la tabla
        #limpiamos la tabla antes de volver a insertar
        for registro in registros:
            self.tabla.delete(registro)
        try:
            conn = mariadb.connect(
                user="root",
                password="xela2020",
                host="localhost",
                port=3305,
                database="cafeteria_bd"
            )
        except mariadb.Error as e:
            print("Error al conectarse a la bd",e)
        cur = conn.cursor()
        cur.execute(query)
        return cur

    def mostrarDatos(self):
        consulta = self.consultaCliente("SELECT * FROM cliente")
        cont = 0
        for (id,nombre,apellido,nit,telefono,correo) in consulta:
            self.tabla.insert('',cont,text='',value=(id,nombre,apellido,nit,telefono,correo))
            cont+=1


if __name__=="__main__":
    ventana =  Tk()
    aplicacion = Cliente(ventana)
    aplicacion.mostrarDatos()
    ventana.mainloop()