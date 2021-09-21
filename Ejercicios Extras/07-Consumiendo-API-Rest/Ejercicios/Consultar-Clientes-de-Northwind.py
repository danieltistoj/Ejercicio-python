import requests

url = 'http://api.labs.com.es/v1.0/clientes.ashx'
params = { }
id = input('Identificador del cliente: ')

params['id'] = id

response = requests.get(url, params=params)

if (response.status_code == 200):
    if('application/json' in response.headers['Content-Type'].split(';')):
        data = response.json()

        if(len(data) > 0):
            for d in data:
                print(f'{d["CustomerID"]:>14}#  {d["CompanyName"]}')
                print(f'{"Contacto:":>15}  {d["ContactName"]} ({d["ContactTitle"]})')
                print(f'{"Dirección:":>15}  {d["Address"]}')
                print(f'{"":<15}  {d["PostalCode"]} {d["City"]}')
                print(f'{"":<15}  ({d["Country"]})')
                print(f'{"Tel/Fax:":>15}  {d["Phone"]} {d["Fax"]}')
                print('')
        else:
            print(f'El identificador ({id}) no pertence a ningún cliente.')
    else:
        print('No se puede procesar el contenido.') 
else:
    print(f'Error: {response.reason}')