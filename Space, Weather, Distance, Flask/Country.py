import urllib.request 
import json


def country(name):
  url = f'https://restcountries.com/v3.1/alpha?codes={name}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result 