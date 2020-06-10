'''from apixu.client import ApixuClient
api_key = 'e1aa06f2f78c861965b05b96ea20b366' #your apixu key
client = ApixuClient('070f3c2952168202c7a321026dac81ce')
current = client.current(q="india")
print(current)'''
import requests, json 
api_key = "070f3c2952168202c7a321026dac81ce"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "coimbatore"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
response = requests.get(complete_url) 
x = response.json()
print(x)
print(x["name"])
