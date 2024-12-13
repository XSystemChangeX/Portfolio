import geopy.distance


def Thedistance(coords_1_lat,coords_1_lon,coords_2_lat,coords_2_lon):
  coords_1 = (coords_1_lat, coords_1_lon)
  coords_2 = (coords_2_lat, coords_2_lon)

  return round((geopy.distance.distance(coords_1, coords_2).km),2)