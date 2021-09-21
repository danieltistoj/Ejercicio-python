import pymssql
import sys

#Establecemos la conexión con SQL Server
connection = pymssql.connect(server='localhost', user='test', password='test100', database='Northwind')


#Creamos un cursor para ejercutar comandos en la base de datos
#Los datos se retornar como Tuplas
cursor = connection.cursor()

#Utilizamos el parámetro as_dict=True para que los datos se retornen como diccionarios
cursor = connection.cursor(as_dict=True)


#Ejemplos de como recuperar datos, comando SELECT
cursor.execute("SELECT * FROM Customers WHERE CustomerID = %d", "ANATR")
cursor.execute("SELECT * FROM Customers WHERE CustomerID = 'ANATR'")
cursor.execute('SELECT * FROM Customers WHERE Country = %d', 'Spain')
cursor.execute('SELECT * FROM Customers ORDER BY Country, City')
cursor.execute('SELECT * FROM Customers')

#Mostramos los datos mediante un WHILE
row = cursor.fetchone()
while (row):
    print(f"     ID: {row['CustomerID']}")
    print(f"Empresa: {row['CompanyName']}")
    print("")
    row = cursor.fetchone()

#Mostramos los datos mediante un FOR
cursor.execute('SELECT * FROM Customers')
for row in cursor.fetchall():
    print(f"     ID: {row['CustomerID']}")
    print(f"Empresa: {row['CompanyName']}")
    print("")


#Insertar datos, comando INSERT INTO
#Insertamos un nuevo registro
cursor.execute("INSERT INTO Customers (CustomerID ,CompanyName, City, Country) VALUES ('DEMO1', 'Empresa Demo Uno, SL', 'Madrid', 'Spain')")

#Utilizamos la función commit() para confirmar inserciones, actulizaciones o borrado de datos
connection.commit()

#Utilizamos la función rollback() para no confirmar inserciones, actulizaciones o borrado de datos
#connection.rollback()

#Insertamos varios registros utilizando un comando con comodines y una lista de registros
command = "INSERT INTO Customers VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
command = "INSERT INTO Customers (CustomerID ,CompanyName, City, Country) VALUES (%d, %d, %d, %d)"

data = []
data.append(('DEMO2', 'Empresa Demo Dos, SL', 'Madrid', 'Spain'))
data.append(('DEMO3', 'Empresa Demo Tres, SL', 'Madrid', 'Spain'))
data.append(('DEMO4', 'Empresa Demo Cuatro, SL', 'Madrid', 'Spain'))

cursor.executemany(command, data)
connection.commit()
print(f"Número de filas modificadas: {cursor.rowcount}")


#Modificamos datos, comando UPDATE / SET
#Ejemplo: Cambiamos el valor de Country para todo los registro con valor Spain en Country
cursor.execute("UPDATE Customers SET Country = 'España' WHERE Country = 'Spain'")
connection.commit()
print(f"Número de filas modificadas: {cursor.rowcount}")


#Eliminados datos, comando DELETE
#Eliminamos uno registro 
cursor.execute("DELETE FROM Customers WHERE CustomerID = 'DEMO5'")
cursor.execute('DELETE FROM Customers WHERE CustomerID = %d', 'DEMO5')
cursor.execute('DELETE FROM Customers WHERE Country = %d', 'EEUU')
connection.commit()
print(f"Número de filas modificadas: {cursor.rowcount}")

#Eliminamos varios registro utilizando un comando con comodin y una lista de datos
cursor.executemany("DELETE FROM Customers WHERE CustomerID = %d", ["DEMO2", "DEMO3", "DEMO4"])
connection.commit()
print(f"Número de filas modificadas: {cursor.rowcount}")