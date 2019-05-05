#!/usr/bin/env python3

import urllib.request
from urllib.request import urlopen
import json
import re

def get_ip_address():
	'''
	Function that returns the user public IP address based on response from http://checkip.dyndns.com/
	'''
	data = str(urlopen('http://checkip.dyndns.com/').read())
	return re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(data).group(1)

user_ip = str(get_ip_address()) 

# Get users location
url = 'http://ipinfo.io/' + user_ip + '/json'
response = urlopen(url)
data = json.load(response)
city = data['city']
country = data['country']

# Get weather data
weather_response = urlopen('http://api.openweathermap.org/data/2.5/weather?q={},{}'.format(city, country))
#weather_response_test = urlopen('https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22')
weather_data = json.load(weather_response)
print('City:\t\t' + weather_data['name'] + ', ' + weather_data['sys']['country'])
print('Weather:\t' + weather_data['weather'][0]['main'])
print('Description:\t' + weather_data['weather'][0]['description'])
print('Temperature:\t' + str(round((5/9) * (weather_data['main']['temp'] - 32), 2)) + ' C')