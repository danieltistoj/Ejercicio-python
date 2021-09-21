from pymongo import MongoClient, collation
from pprint import pprint
from bson.objectid import ObjectId
import sys, json

## Establecer conexión con MongoDB (motor de base datos)
client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

## Mostar el estado del servidor (motor de base de datos)
# Asignamos a la variable db el objeto que representa la base de datos admin
db = client.admin

# Ejecutamos comandos en la base de datos utilizando la función command
# El comando serverStatus nos retorna el estado del servidor en JSON
status = db.command("serverStatus")
pprint(status)

## Trabajando con Datos
# Seleccionar la base de datos con la que vamos a trabajo
#northwindDB = client['Northwind']
northwindDB = client.Northwind

# Listar las colecciones de la base de datos
print(northwindDB.list_collection_names())

# Seleccionar una colección de la base de datos
collection = client.Northwind.customers
collection = client['Northwind']['customers']
collection = northwindDB['customers']
collection = northwindDB.customers

# Utilizamos estimated_document_count() para saber el número de documentos en la colección
result = collection.estimated_document_count()

# Buscar documentos dentro de una colección y retornamos el primer documento encontrado
result = collection.find_one({'Country': 'USA'})
pprint(result)

# Buscar documentos por ObjectId
id = ObjectId('609277299664cd3234ddc8e3')
result = collection.find_one({ '_id' : id })
pprint(result)

result = collection.find_one({ '_id' : ObjectId('609277299664cd3234ddc8e3') })
pprint(result)

# Buscar documentos dentro de una colección
cursor = collection.find({'Country': 'USA'})
cursor = collection.find({'Country': 'USA'}).limit(3)
cursor = collection.find({'Country': 'USA'}).skip(5)
cursor = collection.find({'Country': 'USA'}).sort('City')
cursor = collection.find({'Country': 'USA'}).sort('City').limit(10).skip(5)
cursor = collection.find({'Country': 'USA'}).sort('City', 1)       #Ascendente     A a W
cursor = collection.find({'Country': 'USA'}).sort('City', -1)      #Descendente    W a A
cursor = collection.find({'Country': 'USA', 'City': 'Portland'}).sort('City')
cursor = collection.find({'Country': 'USA', 'City': 'Portland'}).sort('City')
cursor = collection.find({'Country': { '$in' : ['USA', 'Mexico']}})
cursor = collection.find({'Country': { '$in' : ['USA', 'Mexico']}}).sort('City')

print("Número de documentos: ", cursor.count())
print("Número de documentos: ", collection.count_documents({'Country': 'USA'}))

print("Datos por leer: ", cursor.alive)

while (cursor.alive):
    pprint(cursor.next())

print("Datos por leer: ", result.alive)

#Buscamos datos utilizando la función aggregate()
#Ejemplo: recuperamos datos de ANATR y todo sus pedidos
cursor = client.Northwind.customers.aggregate([
    { '$match': { 'CustomerID' : 'ANATR' } },
    { '$sort': { 'City' : 1 } },
    { '$lookup' : {
        'from' : 'orders',
        'localField' : 'CustomerID',
        'foreignField' : 'CustomerID',
        'as' : 'Orders'
        } 
    }
])

customer = cursor.next()
print('ID: ', customer['CustomerID'])
print('Empresa: ', customer['CompanyName'])
print('País: ', customer['Country'])
for order in customer['Orders']:
    print('ID Pedido: ', order['OrderID'])
    print('ID Empledo: ', order['EmployeeID'])


# Insertar un documento en la colección utilizando un objeto JSON
customer = {
    "CustomerID": "DEMO2",
    "CompanyName": "Uno Comidad y Bebidas, SL",
    "ContactName": "Borja Cabeza",
    "ContactTitle": "Propietario",
    "Address": "Calle Gran Vía, 41",
    "City": "Madrid",
    "Region": "Madrid",
    "PostalCode": "28044",
    "Country": "Spain",
    "Phone": "(91) 200 20 20",
    "Fax": "(91) 200 20 21"
}

idNewDocument = collection.insert_one(customer).inserted_id
print('ID Nuevo Documento: ', idNewDocument)

# Insertamos un documentos utilizando un objeto de Python
class Customer:
    CustomerID = None
    CompanyName = None
    ContactName = None
    ContactTitle = None
    Address = None
    City = None
    Region = None
    PostalCode = None
    Country = None
    Phone = None
    Fax = None

cliente = Customer()
cliente.CustomerID = "DEMO4"
cliente.CompanyName = "Un Dos Tresm, SL"
cliente.ContactName = "Borja Cabeza"
cliente.ContactTitle = "Generente"
cliente.Address = "Calle Gran Vía, 16"
cliente.Region = "Madrid"
cliente.City = "Madrid"
cliente.Country = "Spain"
cliente.PostalCode = "28024"
cliente.Phone = "(91) 200 20 20"
cliente.Fax = "(91) 300 30 30"

pprint(cliente.__dict__)

idNewDocument = client.Northwind.customers.insert_many(cliente.__dict__).inserted_id
print('ID Nuevo Documento: ', idNewDocument)


# Actuliazamos documentos en una colección
# Consulta, determina los documentos que se tienen que modificar
query = {'CustomerID': 'DEMO2'}

# Determina las claves y valores que son modificados en los documento encontrados por la consulta
newValues = { 
    "$set" : { 
        "CompanyName": "Restaurantes Dos, SL", 
        "Address": "Calle Serrano, 81", 
        "Phone": "(91) 400 80 80"
        } 
    }

# Las funciones que realizan la búsqueda y modificación de los documentos
result = collection.update_many(query, newValues)
result = collection.update_one(query, newValues)
print(result.matched_count, ' elementos encontrados.')
print(result.modified_count, ' elementos modificados.')
pprint(result)
pprint(collection.find_one(query))