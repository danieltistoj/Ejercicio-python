from itertools import product
from pymongo import MongoClient

#Cliente
client = MongoClient('mongodb://localhost:27017/')

#Base de Datos
db = client.Northwind

#Colecciones
orders = db.orders
details = db.order_details
products = db.products


idPedido = input("Identificador del Pedido: ")

pedido = orders.find_one({ 'OrderID' : idPedido })
if(pedido != None):
    print(f"===============================================================")
    print(f" DATOS DEL PEDIDO {idPedido}")
    print(f"===============================================================")
    print(f" Entregar : {pedido['ShipName']}")
    print(f"            {pedido['ShipAddress']}")
    print(f"            {pedido['ShipCity']} ({pedido['ShipCountry']})")
    print("")
    # Buscamos el detalle del pedido
    detalle = details.find({ 'OrderID' :  idPedido })
    print(f"===============================================================")
    print(f"  {'Producto':<31} {'Cant. '} {'Precio':>10} {'Total':>10}")
    print(f"===============================================================")

    totalPedido = 0

    # Recorremos con While el curso del detalle del pedido
    while(detalle.alive):
        linea = detalle.next()
        # Buscasmos y mostramos la descripción del producto, utilizando ProductID
        producto = products.find_one({ 'ProductID' : linea['ProductID']})
        # Mostramos cada linea de pedido
        # Descripción  -  cantidad  - precio  -  precio * cantidad
        totalLinea = int(linea['Quantity']) * float(linea['UnitPrice'])
        totalPedido += totalLinea

        totalFormat = "{:0.2f}".format(totalLinea)

        print(f"  {producto['ProductName']:<31} {linea['Quantity']:>6} {linea['UnitPrice']:>10} {totalFormat:>10}")

    #Mostar el importe total del pedido
    print(f"===============================================================")
    totalPedidoFormat = "{:0.2f}".format(totalPedido)
    print(f"  {'TOTAL':>49} {totalPedidoFormat:>10}")
else:
    print(f"El pedido {idPedido} no existe.")
