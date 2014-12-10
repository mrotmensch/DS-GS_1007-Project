'''
Created by: Lucy Wang

Modified by: Lucy Wang and Maya Rotmensch
'''

from motionless import *
from cStringIO import StringIO
from PIL import Image
import os
import urllib

def getCoordinates(plot_results):
  """ This function changes the format of the 5 results we wish to plot on the map into an easily plotted format.
    Args:
        plot_results : a pandas DataFrame containing information on the 5 closest free WiFi locations.
    Returns:
        lon: list of longitude of  the 5 closest locations.
        lat : list of latitude of  the 5 closest locations.
    
  """  
  lon = list(plot_results.Long_)
  lat = list(plot_results.Lat)

  return lon, lat

def mapOutput(user_lon, user_lat, search_results):
  """ 
  TODO.
    
  """  
  dmap = DecoratedMap()
  dmap.add_marker(LatLonMarker(lat = user_lat, lon = user_lon, label = 'A', color = 'blue'))
  
  i = 1
  results_lon, results_lat = getCoordinates(search_results)
  for lat_coord, lon_coord in zip(results_lat, results_lon):
    dmap.add_marker(LatLonMarker(lat = lat_coord, lon = lon_coord, label = str(i), color = 'red'))
    i += 1
  return dmap.generate_url()

def mapImage(url):
  """ 
  TODO.
    
  """ 
  buffer_image = StringIO(urllib.urlopen(url).read())
  image = Image.open(buffer_image)
  
  return image
