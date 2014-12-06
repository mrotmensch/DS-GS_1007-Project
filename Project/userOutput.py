#from pylab import *
import pylab
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

def get_output_coord(search_results):
  
  max_lat = search_results.Lat.max()
  min_lat = search_results.Lat.min()
  max_lon = search_results.Long_.max()
  min_lon = search_results.Long_.min()
  plot_results = search_results[['Lat','Long_','SSID']]

  return max_lat, min_lat, max_lon, min_lon, plot_results

def output_map(user_long,user_lat, search_results):
  """ user_lat, user_long: lat and long coordinates of the user address
  """
  
  max_lat, min_lat, max_lon, min_lon, plot_results = get_output_coord(search_results)
  
  pylab.rcParams['figure.figsize'] = (8.0,6.4)

  max_lat = max_lat + 0.05
  min_lat = min_lat - 0.05
  max_lon = max_lon + 0.05
  min_lat = min_lat - 0.05

  map = Basemap(projection = 'merc',  lat_0= user_lat,  lon_0 = user_long, resolution = 'h', area_thresh = 0.1, llcrnrlon=min_lon, llcrnrlat= min_lat, urcrnrlon=max_lon, urcrnrlat= max_lat)


  map.drawcoastlines()
  map.drawcountries()
  map.fillcontinents(color = 'white')
  map.drawmapboundary()

  lon = list(plot_results.Long_)
  lat = list(plot_results.Lat)
  label = list(plot_results.SSID)
  x,y = map(lon, lat)
  map.plot(x, y, 'bo', markersize=8)
  map.plot(user_long,user_lat, 'ro', markersize=7)
  
  for label, xpt, ypt in zip(label,x,y):
    plt.text(xpt,ypt,label)

  plt.show()