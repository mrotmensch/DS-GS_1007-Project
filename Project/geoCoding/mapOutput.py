'''

Dec 8, 2014

@author: 

'''

from motionless import *
from cStringIO import StringIO
from PIL import Image
import os
import urllib

def getCoordinates(plot_results):
  lon = list(plot_results.Long_)
  lat = list(plot_results.Lat)

  return lon, lat

def mapOutput(user_lon, user_lat, search_results):
  dmap = DecoratedMap()
  dmap.add_marker(LatLonMarker(lat = user_lat, lon = user_lon, label = 'A', color = 'blue'))
  
  i = 1
  results_lon, results_lat = getCoordinates(search_results)
  for lat_coord, lon_coord in zip(results_lat, results_lon):
    dmap.add_marker(LatLonMarker(lat = lat_coord, lon = lon_coord, label = str(i), color = 'red'))
    i += 1
  return dmap.generate_url()

def mapImage(url):
  buffer_image = StringIO(urllib.urlopen(url).read())
  image = Image.open(buffer_image)
  
  return image

def closeMap():
  os.popen('killall display')
