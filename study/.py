import requests
import os

url = r'https://www.imiaobige.com/read/49066/2906860.html'
resp = requests.get(url)
resp.encoding = 'utf-8'

print(resp.text)