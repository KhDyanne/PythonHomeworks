import requests
import time
from datetime import datetime
import pytz
import sys

apiKey='885422cd05b14d549aa110429250602'
city1='Grenoble'
city2='Braunschweig'
url1=f'https://api.weatherapi.com/v1/current.json?key={apiKey}&q={city1}&aqi=no'
url2=f'https://api.weatherapi.com/v1/current.json?key={apiKey}&q={city2}&aqi=no'

response1=requests.get(url1)
data1=response1.json()

response2=requests.get(url2)
data2=response2.json()

condition1=data1['current']['condition']['text']
temperature1=data1['current']['temp_c']
tz_id1=data1['location']['tz_id']
zone1=pytz.timezone(tz_id1)

condition2=data2['current']['condition']['text']
temperature2=data2['current']['temp_c']
tz_id2=data2['location']['tz_id']
zone2=pytz.timezone(tz_id2)

weather_condition_city1=f"\nWeather in {city1}: {condition1}\nTemperature: {temperature1}°C"
weather_condition_city2=f"\nWeather in {city2}: {condition2}\nTemperature: {temperature2}°C\n"

print(weather_condition_city1)
print(weather_condition_city2)


while True:
    time1 = datetime.now(zone1).strftime("%Y-%m-%d %H:%M:%S")
    time2 = datetime.now(zone2).strftime("%Y-%m-%d %H:%M:%S") 
    
    sys.stdout.write(f"\rCurrent Time in {city1}: {time1} | Current Time in {city2}: {time2}")
    sys.stdout.flush()
    
    time.sleep(1)