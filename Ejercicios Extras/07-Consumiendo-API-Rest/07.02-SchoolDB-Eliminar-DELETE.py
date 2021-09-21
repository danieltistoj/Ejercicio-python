import requests, json

url = 'http://school.labs.com.es/api/students/'
headers = { 'Content-Type' : 'application/json' }

id = input('ID Alumno: ')

response = requests.delete(url + id, headers=headers)
if(response.status_code == 200):
    print(f'Alumno eleminado correctamente.')
    print(f'Data: {response.text}')
else:
    print('Error:', response.reason)