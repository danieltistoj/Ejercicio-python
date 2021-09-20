import mysql.connector

class Database:
    def __init__(self):
        self.mysql = mysql.connector.connect(
            host="192.168.191.109",  # hostname
            user="proyecto",  # the user who has privilege to the db
            passwd="0101",  # password for user
            database="alumnos",  # database name
            auth_plugin='mysql_native_password',

        )
        #self.cursor = self.connection.cursor()
        self.curso = self.mysql.cursor()
        self.curso.execute("select * from alumnos")
        r = self.curso.fetchall()
        print(r)
        print("Conexion exitosa")

database = Database()


