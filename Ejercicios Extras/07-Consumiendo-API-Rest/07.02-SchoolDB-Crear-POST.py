import requests, json

url = 'http://school.labs.com.es/api/students/'

#{"firstName":"Ana","lastName":"Sánchez","dateOfBirth":"2006-05-09","classId":1}
data = {}
data['firstName'] = input('Nombre: ')
data['lastName'] = input('Apellidos: ')
data['dateOfBirth'] = input('Fecha de Nacimiento (yyyy-mm-dd): ')
data['classId'] = int(input('Clase (1, 2 o 3): '))

headers = { 'Content-Type' : 'application/json' }

response = requests.post(url, data=json.dumps(data), headers=headers)
if(response.status_code == 201):
    alumno = response.json()
    print(f'Identificador asignado {alumno["id"]}')
else:
    print('Error:', response.reason)