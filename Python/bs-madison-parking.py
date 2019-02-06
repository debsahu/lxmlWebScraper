#!/srv/homeassistant/bin/python3

import requests
from bs4 import BeautifulSoup

i = requests.get('http://www.cityofmadison.com/residents/winter/parking/alternateSideParking.cfm')
root = BeautifulSoup(i.text, 'html.parser')
div = root.select('div.clearfix > strong')
print(div)