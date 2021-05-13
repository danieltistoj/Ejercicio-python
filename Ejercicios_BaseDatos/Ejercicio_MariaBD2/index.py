from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mariadb

class Cliente:
    def __init__(self,ventana):
        self.vetana = ventana
        self.vetana.title("Cliente")

        marco = LabelFrame(self.vetana,text="Cliente")
        #pady significa que tendra 20 espacios arriba y 20 espacios abajo
        marco.grid(row=0,column=0,columnspan=5,pady=20)

        Label(marco,text="Nombre").grid(row=0,column=0) #label
        self.nombre = Entry(marco) #area de texto
        self.nombre.grid(row=0,column=1)

        Label(marco, text="Apellido").grid(row=1, column=0)
        self.apellido = Entry(marco)
        self.apellido.grid(row=1, column=1)

        Label(marco, text="NIT").grid(row=2, column=0)
        self.nit = Entry(marco)
        self.nit.grid(row=2, column=1)

        Label(marco, text="Telefono").grid(row=3, column=0)
        self.telefono = Entry(marco)
        self.telefono.grid(row=3, column=1)

        Label(marco, text="Correo").grid(row=4, column=0)
        self.correo = Entry(marco)
        self.correo.grid(row=4, column=1)
        #buscar cliente entry
        #Buscar nombre
        Label(self.vetana, text="Buscar nombre").grid(row=4, column=0)
        self.buscarNombre = Entry(self.vetana)
        self.buscarNombre.grid(row=4, column=1)
        # Buscar nombre
        Label(self.vetana, text="Buscar NIT").grid(row=5, column=0)
        self.buscarNIT = Entry(self.vetana)
        self.buscarNIT.grid(row=5, column=1)
        #boton
        #columspan significa que el boton va a abarcar 2 columnas
        #sticky significa que el boton va a ocupar de este a oeste
        self.btnCrear = Button(marco,text="Guardar",command=self.agregarRegistro,bg="green",fg="white")
        self.btnCrear.grid(row=5,columnspan=2,sticky=W+E)

        self.btnEditar = Button(marco,text="Editar",command=self.editarRegistro,bg="blue",fg="white")
        self.btnEditar.grid(row=6, columnspan=2, sticky=W + E)

        self.btnBorrar = Button(marco, text="Borrar", command=self.borrarRegistro,bg="red",fg="white")
        self.btnBorrar.grid(row=7, columnspan=2, sticky=W + E)

        Button(self.vetana,text="Buscar cliente",command=self.buscarRegistro,bg='#0C0EE7',fg="white").grid(row=6,column=1)

        self.btnBorrar["state"] = "disabled"
        self.btnEditar["state"] = "disabled"

        #Mensaje
        self.mensaje = Label(text ='',fg='green')
        self.mensaje.grid(row=3,column=0,columnspan=2,sticky=W+E)
        #Tabla
        #posible error: https://es.stackoverflow.com/questions/345051/error-out-of-range-insertando-una-tabla
        columns = ('#1','#2','#3','#4','#5','#6')
        self.tabla = ttk.Treeview(self.vetana,columns=columns,show='headings')
        self.tabla.bind("<Double-Button-1>",self.doubleClickTable)#que este al pendiente
        self.tabla.grid(row=7,column=0,columnspan=2)
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
                database="cafeteria_bd",
                autocommit = True
            )
        except mariadb.Error as e:
            print("Error al conectarse a la bd",e)
        cur = conn.cursor()
        cur.execute(query)
        #por si no se pueden insertar datos: https://stackoverflow.com/questions/41633008/mariadb-cant-insert-data
        return cur

    def mostrarDatos(self,where=""):
        if len(where)>0:
            consulta = self.consultaCliente("SELECT * FROM cliente "+where)
        else:
            consulta = self.consultaCliente("SELECT * FROM cliente")

        cont = 0
        for (id, nombre, apellido, nit, telefono, correo) in consulta:
            self.tabla.insert('', cont, text='', value=(id, nombre, apellido, nit, telefono, correo))
            cont += 1

    def agregarRegistro(self):
        if len(self.nombre.get())!=0 and len(self.apellido.get())!=0:
            query = "INSERT INTO cliente(Nombre,Apellido,NIT, Telefono,Correo) VALUES('{}','{}','{}','{}','{}');".format(self.nombre.get(),self.apellido.get(),self.nit.get(),self.telefono.get(),self.correo.get())
            print(query)
            self.consultaCliente(query)
            self.mensaje['text'] = "El cliente {} se inserto exitosamente".format(self.nombre.get())

        else:
            self.mensaje['text'] = "El cliente debe de tener un nombre y un apellido"
        #actualizar datos
        self.mostrarDatos()
    def editarRegistro(self):
        if len(self.nombre.get())!=0 and len(self.apellido.get())!=0:
            query = "UPDATE  cliente SET Nombre = '{}', Apellido='{}',NIT='{}', Telefono='{}',Correo='{}' WHERE idCliente = {}".format(self.nombre.get(),self.apellido.get(),self.nit.get(),self.telefono.get(),self.correo.get(),self.claveVieja)
            print(query)
            self.consultaCliente(query)
            self.mensaje['text'] = "El cliente {} se actualizo exitosamente".format(self.nombre.get())

        else:
            self.mensaje['text'] = "El cliente debe de tener un nombre y un apellido"
        #actualizar datos
        self.mostrarDatos()
        self.btnCrear["state"]="normal"
        self.btnEditar["state"] = "disabled"
        self.btnBorrar["state"] = "disabled"

        self.nombre.delete(0, END)
        self.apellido.delete(0, END)
        self.nit.delete(0, END)
        self.telefono.delete(0, END)
        self.correo.delete(0, END)


    def doubleClickTable(self,event):
        self.claveVieja = int(self.tabla.item(self.tabla.selection())["values"][0])
        self.nombre.delete(0,END)
        self.apellido.delete(0,END)
        self.nombre.delete(0,END)
        self.telefono.delete(0,END)
        self.correo.delete(0,END)
        self.btnCrear["state"]="disabled"
        self.btnEditar["state"]="normal"
        self.btnBorrar["state"] = "normal"

        self.nombre.insert(0,self.tabla.item(self.tabla.selection())["values"][1])
        self.apellido.insert(0, self.tabla.item(self.tabla.selection())["values"][2])
        self.nit.insert(0, self.tabla.item(self.tabla.selection())["values"][3])
        self.telefono.insert(0, self.tabla.item(self.tabla.selection())["values"][4])
        self.correo.insert(0, self.tabla.item(self.tabla.selection())["values"][5])
    def borrarRegistro(self):
        if messagebox.askyesno(message="¿Esta seguro de eliminar el registro?",title="Borrar cliente") == True:
            query = "DELETE FROM cliente where idCliente = {}".format(self.claveVieja)
            self.consultaCliente(query)
        self.btnCrear["state"] = "normal"
        self.btnEditar["state"] = "disabled"
        self.btnBorrar["state"] = "disabled"
        self.nombre.delete(0, END)
        self.apellido.delete(0, END)
        self.nit.delete(0, END)
        self.telefono.delete(0, END)
        self.correo.delete(0, END)
        self.mostrarDatos()
    def buscarRegistro(self):
        where = "WHERE 1=1"
        if len(self.buscarNombre.get())>0:
            where = where + " and Nombre = '{}'".format(self.buscarNombre.get())
        if len(self.buscarNIT.get())>0:
            where = where + " and NIT = '{}'".format(self.buscarNIT.get())
        self.mostrarDatos(where)
        self.buscarNombre.delete(0, END)
        self.buscarNIT.delete(0, END)

if __name__=="__main__":
    ventana =  Tk()
    aplicacion = Cliente(ventana)
    aplicacion.mostrarDatos()
    ventana.mainloop()