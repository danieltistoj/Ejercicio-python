import requests, json
from datetime import datetime


def InfoBus(item):
    data = {}
    data['line'] = item['line']

    if(item['estimateArrive'] < 60):
        data['time'] = 'está en la parada'
    else:
        time = item['estimateArrive'] / 60
        if(time >= 20):
            data['time'] = 'llegará en 20 min o más'
        else:
            data['time'] = f'llegará aproximadamente en {time:1.0f} min.'
    
    data['distance'] = item['DistanceBus']
    data['message'] = f'el {data["line"]} {data["time"]} ({data["distance"]} m.)'

    return data

url = {
    'Base'      : 'https://openapi.emtmadrid.es/v1/',
    'Login'     : 'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/',
    'StopInfo'  : 'https://openapi.emtmadrid.es/v2/transport/busemtmad/stops/<stopId>/arrives/'
}

headers = { 'X-ClientId' : 'escribe tu client ID', 'passKey' : 'escribe tu pass key'}
token = None

response = requests.get(url['Login'], headers=headers)
if(response.status_code == 200):
    #print(response.text)
    #print('token:', response.json()['data'][0]['accessToken'])
    token = response.json()['data'][0]['accessToken']
else:
    print('Error:', response.reason)

if(token != None):
    stopId = input('Número de Parada: ')
    headers = { 'accessToken' : token }
    data = {
        'cultureInfo' : 'ES',
        'Text_StopRequired_YN' : 'Y',
        'Text_EstimationsRequired_YN' : 'Y',
        'Text_IncidencesRequired_YN' : 'Y',
        'DateTime_Referenced_Incidencies_YYYYMMDD' : datetime.now().date().strftime('%Y%m%d')
    }   

    response = requests.post(url['StopInfo'].replace('<stopId>', stopId), headers=headers, data=json.dumps(data))
    if(response.status_code == 200):
        data = list(map(InfoBus, response.json()['data'][0]['Arrive']))
        print(data)
        for item in data:
            print(f'{item["message"]}')
    else:
        print('Error:', response.reason)