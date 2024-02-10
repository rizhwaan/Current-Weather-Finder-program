import json
import requests

# API - to fetch temperature of a city

city_name=input('Enter a City Name:')
api_key='USER API KEY'

# To build the Api URL

api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
get_server_information=requests.get(api_url)
json_data=get_server_information.json()

#for pretty formating the json data

pretty_data=json.dumps(json_data,indent=4)
print(pretty_data)

#to fetch specific data from json

D=json_data["weather"][0]['description']
print(D)

T=json_data["main"]["temp"]
print(T)

print(f'The current Weather Description is{D} & Temp. is{T}')