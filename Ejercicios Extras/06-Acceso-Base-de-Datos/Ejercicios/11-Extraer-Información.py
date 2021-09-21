from pymongo import MongoClient

# Conexión con MongoDB
connect = MongoClient("mongodb://localhost:27017/")
db = connect.Northwind

# Cuantos productos tenemos ????
productos = db.products
numProductos = productos.estimated_document_count()
print("Número de Productos: ", numProductos)

# Buscar y Mostrar todos los productos
listProductos = productos.find()

for n in listProductos:
    print(f"{n['ProductName']}")

print("")

cursor = productos.find()
while(cursor.alive):
    print(cursor.next()['ProductName'])

print("")

# Buscar todos los productos. Con un filter buscamos los productos con UnitsInStock = 0
listProductos = productos.find()
pro = list(filter(lambda p: p['UnitsInStock'] == '0', listProductos))
for p in pro:
    print(f"{p['ProductName']}")

print("")

# Buscar los productos con UnitsInStock = 0
cursor = productos.find({ 'UnitsInStock' : '0'})
while(cursor.alive):
    print(cursor.next()['ProductName'])


# Coste o Valor de nuestro Stock - Producto -> UnitsInStock, UnitPrice
listProductos = productos.find({'UnitsInStock' : { '$ne': '0'}})
#listProductos = productos.find()
valorStock = 0
for n in listProductos:
    valorStock = valorStock + (float(n['UnitPrice']) * int(n['UnitsInStock']))

print(f"\nValor del Stock: {valorStock:1.2f}")

# Coste o Valor de nuestro Stock utilizand map() y sum()
TotalStock = sum(list(map(lambda x: float(x['UnitPrice']) * int(x['UnitsInStock']), productos.find())))
print(f"\nValor del Stock: {TotalStock:1.2f}")
print("")

# Coste o Valor de nuestro Stock utilizando la función aggregate()
query = [
    { '$match': { 'UnitsInStock' : { '$ne': '0' } } },
    { '$addFields': {
        'Price': { '$toDouble': '$UnitPrice' },
        'Stock': { '$toInt': '$UnitsInStock' },
        }
    },
    { '$group': {
        '_id': 'Valor del Stock', 
        'Total': { '$sum': { '$multiply': [ '$Price', '$Stock' ] } },
        'Items': { '$sum' : 1 }
        }
    }
]

listProductos = productos.aggregate(query)
print(listProductos.next())
