import requests, json
from datetime import datetime
from termcolor import colored, cprint

def ParkingInfo(item):
    data = {}
    data['id']      = item['id']
    data['name']    = item["name"]
    data['address'] = item["address"]
    
    if(item['freeParking'] == None):
        data['freeParking'] = 'no disponible'
    else:
        data['freeParking'] = f'{item["freeParking"]:1.0f}'

    return data

url = {
    'Base'          : 'https://openapi.emtmadrid.es/v1/',
    'Login'         : 'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/',
    'ParkingInfo'   : 'https://openapi.emtmadrid.es/v1/citymad/places/parkings/availability/'
}

headers = { 'X-ClientId' : 'escribe tu client ID', 'passKey' : 'escribe tus pass key'}
token = None

response = requests.get(url['Login'], headers=headers)
if(response.status_code == 200):
    token = response.json()['data'][0]['accessToken']
    headers = { 'accessToken' : token }

    response = requests.get(url['ParkingInfo'], headers=headers)
    if(response.status_code == 200):
        data = list(map(ParkingInfo, response.json()['data']))
        
        freeParkingTotal = sum(
            list(map(lambda x: x['freeParking'], 
                list(filter(lambda y: y['freeParking'] != None, response.json()['data'])))))

        for item in data:
            plazas = colored(f'{item["freeParking"]}', 'red', attrs=['reverse'])
            plazas = colored(f'{item["freeParking"]}', 'red') 
            
            print(f'{item["name"]:<30}  Plazas: {plazas}')    
            #print(f'{item["address"]}')
            cprint(f'{item["address"]}', 'blue')
            print('')
        
        plazas = colored(f'{freeParkingTotal}', 'red')  
        print(f'{"Total Plazas:":>39} {plazas}')