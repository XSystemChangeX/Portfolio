import urllib.request 
import json



def address(lat,lon):
  key='bdc_0381972e9e9d4df5aed19424be9c602a'
  url=f'https://api-bdc.net/data/reverse-geocode?latitude={lat}&longitude={lon}&localityLanguage=en&key={key}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result