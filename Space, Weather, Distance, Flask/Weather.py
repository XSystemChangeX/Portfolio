import urllib.request 
import json



def the_Weather(lat,lon):
  key='953156af1d8912580a0dc0e5c43c3fe3'
  url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'

  request = urllib.request.urlopen(url)
  result = json.loads(request.read())

  return result
