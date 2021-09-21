import pymssql

conexion = pymssql.connect(server='localhost', user='test', password='test100', database='Northwind')
cursor = conexion.cursor(as_dict=True)

idPedido = input("Identificador del Pedido: ")
cursor.execute("SELECT * FROM Orders WHERE OrderID = %d", idPedido)

if(cursor.rowcount == 0):
    print(f"El pedido {idPedido} no existe.")
else:
    pedido = cursor.fetchone()
    print(f"===============================================================")
    print(f" DATOS DEL PEDIDO {idPedido}")
    print(f"===============================================================")
    print(f" Entregar : {pedido['ShipName']}")
    print(f"            {pedido['ShipAddress']}")
    print(f"            {pedido['ShipCity']} ({pedido['ShipCountry']})")
    print("")
    
    print(f"===============================================================")
    print(f"  {'Producto':<31} {'Cant. '} {'Precio':>10} {'Total':>10}")
    print(f"===============================================================")

    # Buscamos el detalle del pedido
    cursor.execute("SELECT Quantity, UnitPrice, ProductID FROM [Order Details] WHERE OrderID = %d", idPedido)
    totalPedido = 0
    lineas = cursor.fetchall()
    for linea in lineas:
        # Buscasmos la descripción del producto, utilizando ProductID
        cursor.execute("SELECT ProductName FROM Products WHERE ProductID = %d", linea['ProductID'])
        producto = cursor.fetchone()

        # Mostramos cada linea de pedido
        # producto  -  cantidad  - precio  -  precio * cantidad
        totalLinea = linea['Quantity'] * linea['UnitPrice']
        totalPedido += totalLinea
        totalFormat = "{:0.2f}".format(totalLinea)
        print(f"  {producto['ProductName']:<31} {linea['Quantity']:>6} {linea['UnitPrice']:>10} {totalFormat:>10}")

    #Mostar el importe total del pedido
    print(f"===============================================================")
    totalPedidoFormat = "{:0.2f}".format(totalPedido)
    print(f"  {'TOTAL':>49} {totalPedidoFormat:>10}")
