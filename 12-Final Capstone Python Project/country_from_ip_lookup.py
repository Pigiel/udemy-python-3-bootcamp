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
ip = data['ip']
city = data['city']
region = data['region']
country = data['country']
location = data['loc']
org = data['org']

# Print details
print('IP:\t\t' + ip)
print('City:\t\t' + city)
print('Region:\t\t' + region)
print('Country:\t' + country)
print('Location:\t' + location)
print('Organization:\t' + org)