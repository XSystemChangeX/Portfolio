from ISS import ISS_location
from Weather import the_Weather
from Distance import Thedistance
from ReverseGeo import address
from Country import country

data =ISS_location()
lat,lon = data[0],data[1]

#Weather which is pulled from Weather.py, subsequenly from my API key...grabbing lat,lon, which is pulled from ISS.py###

weather = the_Weather(lat,lon)

temp_c = round(weather["main"]["temp"]- 273.15,2)
description = weather["weather"][0]["description"]
print(str(temp_c),"C",description)





#reverse geolocation, gives us the location of the ISS, through API, which allows us to see the country code from Lat/Lon.
add = address(lat,lon)

#Prints the country Code, if nothing then it prints "The ISS is over water, and through country(location)[0]["flags"]["png"] pull/print the flag PNG url for the country###
print("Country Code is :",add["countryCode"])
if(add["countryCode"]==""):
  print("The ISS is over water !")
else:
  location = add["countryCode"]
  print(add["countryCode"])
  flag = country(location)[0]["flags"]["png"]
  print(flag)


#the distance between ISS and yourself(Kingston, Ontario)

distance= Thedistance(lat,lon,44.230480,-76.481247)
print(f"You are {distance} away from the ISS in KM ! ")








