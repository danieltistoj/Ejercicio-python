import requests, pprint

# Utilizamos la función get() para realizar llamadas a microservicios en modo GET

url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url)

# Una vez procesada la solicitud y recibida la respuesta podemos ver el código de estado
# La propiedad REASON nos informa del código de estado en modo texto.
print('Código de Estado:', response.status_code)
print('Estado:', response.reason)

# El código de estado 200 indica que la solicitus se ha procesado OK
if (response.status_code == 200):
    # La propiedad HEADERS es un diccionario que contiene la información de la cabecera del mensaje
    print('Cabeceras:', response.headers)
    print('Tipo del Contenido:', response.headers['Content-Type'])
    
    # El contenido de la respuesta lo encontramos en:
    #  - propiedad TEXT en formato texto
    #  - propiedad CONTENT como un array de bytes
    #  - función JSON() como objeto, normalmente un diccionario
    if (response.headers['Content-Type'] == 'application/json'):
        data = response.json()
        print('Latitud:', data['iss_position']['latitude'])
        print('Longitud:', data['iss_position']['longitude'])
        print('Timestamp:', data['timestamp'])
        print('Mensaje:', data['message'])
    else:
        print('Contenido:', response.text)
        print('Contenido:', response.content)
else:
    print('Error:', response.reason)

print('======================================================================')

# Utilizamos la función post() para realizar llamadas a microservicios en modo POST
url = 'https://postman-echo.com/post'

params1 = { 'param1' : 'demo', 'param2' : 'demo'}
headers1 = { 'content-type' : 'application/json' }
data1 = { 'Nombre' : 'Borja', 'Apellidos' : 'Cabeza' }

response = requests.post(url, params=params1, data=data1, headers=headers1)

print('Código de Estado:', response.status_code)
print('Estado:', response.reason)

if (response.status_code == 200):
    print('Cabeceras:', response.headers)
    print('Contenido:', response.text)
else:
    print('Error:', response.reason)
