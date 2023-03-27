# Created By: Harsh Patel

import requests
import json

print("==================================================")
print("               WEATHER FETCHER APP                ")
print("==================================================")

city = input('Enter City name: ')
country = input('Enter Country name: ')

url = "https://api.weatherapi.com/v1/current.json?key=<YOUR API KEY>&q=" + \
    city + ",%20" + country + "&aqi=yes"

data = requests.get(url)
loaded = json.loads(data.text)
print()
print()
print("Location: " + loaded['location']['name'] +
      ", "+loaded['location']['country'])
print("Temperature(in `C):", loaded['current']['temp_c'], "`C")
print("Temperature(in `F):", loaded['current']['temp_f'], "`F")
print("Wind blowing at", loaded['current']['wind_kph'], "KM/h in",
      loaded['current']['wind_degree'], "degree", loaded['current']['wind_dir'])
print("Feels like", loaded['current']['feelslike_c'], "`C")
print("Visibility(in KMs):", loaded['current']['vis_km'])
