import requests
from datetime import datetime

USER = YOUR-USER
TOKEN = YOUR-TOKEN
ID = YOUR-ID
today = datetime.now()

pixela_url = 'https://pixe.la/v1/users'
graph_url = f'{pixela_url}/{USER}/graphs'
value_url = f'{pixela_url}/{USER}/graphs/{ID}'
change_url = f'{pixela_url}/{USER}/graphs/{ID}/{today.strftime("%Y%m%d")}'


user_params = {
    'token': TOKEN,
    'username': USER,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

graph_conf = {
    'id': ID,
    'name': 'Walking Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': TOKEN,
}

day = input('Write date in yyyyMMdd: ')
how_much = input('How much did you walk totally? ')

value_params = {
    'date': day,
    'quantity': how_much
}

change_params = {
    'quantity': '5'
}

requests.post(url=value_url, json=value_params, headers=headers)
