import json

def PrintData(customer):
    print(f"ID        : {customer['CustomerID']}")
    print(f"Empresa   : {customer['CompanyName']}")
    print(f"Contacto  : {customer['ContactName']} ({customer['ContactTitle']})")
    print(f"Dirección : {customer['Address']}")
    print(f"          : {customer['PostalCode']} {customer['City']} ({customer['Country']})")
    print(f"Teléfono  : {customer['Phone']}")
    print(f"Fax       : {customer['Fax']}")


#'CustomerID', 'CompanyName', 'ContactName', 'ContactTitle', 'Address', 'City', 'Region', 'PostalCode', 'Country', 'Phone', 'Fax'

file = open(".\\Ficheros\\clientes.json", "rt", encoding="UTF-8")
dataJSON = file.read()
file.close()

customers = json.loads(dataJSON)

# print(type(dataJSON)) 
# print(type(customers)) 
# print(len(customers)) 
# print(customers[0].keys())

# Cód ANATR ANTON
id = (input("ID del Cliente: ")).upper()
result = list(filter(lambda x: x['CustomerID'] == id, customers))
if(len(result) > 0):
    PrintData(result[0])
else:
    print(f"No existe ningún cliente con identificador {id}.")