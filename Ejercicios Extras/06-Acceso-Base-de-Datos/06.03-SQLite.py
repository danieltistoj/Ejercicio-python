import sqlite3
import sys
from typing import Sized

#Establecemos conexión con la base de datos, indicando la ruta del fichero
#Si el fichero no exite, se crea
connection = sqlite3.connect('.\\Ficheros\\demo.db')

#Creamos un cursor que nos permite ejecutar comandos en la base de datos
cursor = connection.cursor()

#En una base de datos nueva, necesitamos inicialmente crear las tablas
#Estas sentencias se ejecutan una sola vez
command = "SELECT count() FROM sqlite_master WHERE type = 'table' AND name = 'Alumnos'"
cursor.execute(command)
tablas = cursor.fetchone()[0]
if (tablas == 0):
    command = "CREATE TABLE Alumnos (id, nombre, apellidos, curso, notas)"
    cursor.execute(command)

#Consultar datos
command = "SELECT * FROM Alumnos"

cursor.execute(command)
r = cursor.fetchone()
while (r):
    print(r)
    r = cursor.fetchone()

print("")

cursor.execute(command)
data = cursor.fetchall()
for r in data:
    print(r)

print("")

for r in cursor.execute(command):
    print(r)


#Insertar un registro en la base de datos
command = "INSERT INTO Alumnos (id, nombre) VALUES ('A00', 'Borja')"
command = "INSERT INTO Alumnos VALUES ('A00', 'Borja', 'Cabeza', '2B', Null)"
cursor.execute(command)
connection.commit()


#Insertar varios registros en la base de datos
listaAlumnos = [('H32', 'Ana', 'Trujillo', '2B', None), ('5H2', 'Adrian', 'Sánchez', '2C', None), ('A9C', 'José', 'Sanz', '2A', None)]
command = "INSERT INTO Alumnos VALUES (?, ?, ?, ?, ?)"
cursor.executemany(command, listaAlumnos)
connection.commit()

#Actualiza registros
command = "UPDATE Alumnos SET apellidos = 'Sanz' WHERE id = '5H2'"
cursor.execute(command)
connection.commit()

#Eliminar registros
command = "DELETE Alumnos WHERE id = '5H2'"
cursor.execute(command)
connection.commit()

