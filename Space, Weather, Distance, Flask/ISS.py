import urllib.request 
import json


def ISS_location():
  url='http://api.open-notify.org/iss-now.json'

  request = urllib.request.urlopen(url)
  result = json.loads(request.read())

  lat = result['iss_position']['latitude']
  lon = result['iss_position']['longitude']



  print("Google Map: ","https://www.google.com/maps/place/"+lat +"+"+lon )
  return lat,lon