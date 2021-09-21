import requests, json

url = 'http://school.labs.com.es/api/students/'
headers = { 'Content-Type' : 'application/json' }

id = input('ID Alumno: ')

response = requests.get(url + id, headers=headers)
if(response.status_code == 200):
    data = response.json()
    print(f'   Nombre: {data["firstName"]}')
    print(f'Apellidos: {data["lastName"]}')
    print(f'    Clase: {data["classId"]}')
    print(f'Fecha Nac: {data["dateOfBirth"]}')
else:
    print('Error:', response.reason)