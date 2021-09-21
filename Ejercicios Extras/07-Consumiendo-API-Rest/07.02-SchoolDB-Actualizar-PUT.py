import requests, json

url = 'http://school.labs.com.es/api/students/'
id = input('ID Alumno: ')
data = None
headers = { 'Content-Type' : 'application/json' }

response = requests.get(url + id)
if (response.status_code == 200):
    data = response.json()
    for key in data.keys():
        if(key == 'id'): 
            continue
        print(f'{key}: {data[key]}')
else:
    print(f'Error: {response.reason}')

nombre = input(f'Nombre ({data["firstName"]}): ')
if(nombre != ''):
    data['firstName'] = nombre

apellidos = input(f'Nombre ({data["lastName"]}): ')
if(apellidos != ''):
    data['lastName'] = apellidos

classID = input(f'Clase ({data["classId"]}): ')
if(classID != ''):
    data['classId'] = int(classID)


url = 'http://school.labs.com.es/api/students/' + str(data['id'])

response = requests.put(url, data=json.dumps(data), headers=headers)
if (response.status_code == 204):
    print(f'Registro modificado correctamente')
else:
    print(f'Error: {response.reason}')