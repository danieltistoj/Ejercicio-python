import requests

url = 'https://www.zippopotam.us/es/'
postalCode = input('Código Postal: ')

response = requests.get(url + postalCode)
if (response.status_code == 200):
    data = response.json()
        
    for d in data['places']:
        print('Ciudad:', d['place name'])
        print('Región:', d['state']) 
        print('Longitud:', d['longitude']) 
        print('Latitud:', d['latitude'])   
        print('')
else:
    print(f'Error: {response.reason}')