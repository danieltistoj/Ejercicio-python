import mariadb
import sys
class DataBase:
    def __init__(self):
        try:
            self.conn = mariadb.connect(
                user="root",
                password="xela2020",
                host="localhost",
                port=3305,
                database="cafeteria_bd"
            )
        except mariadb.Error as e:
            print(f"Error de conexion con la base de datos: {e}")
            sys.exit(1)

        self.cursor = self.conn.cursor()


database = DataBase()
database.cursor.execute(
    "SELECT * FROM cliente"
)

for (idCliente,nombre,apellido,nit,telefono,correo) in database.cursor:
    print(idCliente, nombre, apellido, nit, telefono, correo)