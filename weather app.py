import requests
import json

api_key = '4fdc8111b231a07988ac8ae62b229843'
city = input('Enter city name:')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

data = requests.get(url)
paylod = (json.loads(data.text))

temprature = paylod['main']['temp']
description = paylod['weather'][0]['description']

print(f'{city} - {round(temprature - 273.15)} \n Description - {description}')


