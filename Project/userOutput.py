from pylab import *
from mpl_toolkits.basemap import Basemap
import matplotlib.pylot as plt
import numpy as np

def get_output_coord(search_results):
  
  max_lat = search_results.Lat.max()
  min_lat = search_results.Lat.min()
  max_lon = search_results.Long_.max()
  min_lon = serach_results.Long_.min()
  plot_results = search_results[['Lat','Long_','SSID']]

  return max_lat, min_lat, max_lon, min_lon, plot_results

def output_map(user_long,user_lat, search_results):
  """ user_lat, user_long: lat and long coordinates of the user address
  """
  
  max_lat, min_lat, max_lon, min_lon, plot_results = get_output_coord(search_results)
  
  pylab.rcParams['figure.figsize'] = (8.0,6.4)

  max_lat = max_lat + 1
  min_lat = min_lat - 1
  max_lon = max_lon + 1
  min_lat = min_lat - 1

  map = Basemap('merc',  user_lat,  user_long, 'h', 0.1, min_long, min_lat, max_long, max_lat)
  map.drawcoastlines()
  map.drawcountries()
  map.fillcontinents(color = 'white')
  map.drawmapboundary()

  lon = list(plot_results.Long_)
  lat = list(plot_results.Lat)
  label = list(plot_results.SSID)
  x,y = map(lon, lat)
  map.plot(x, y, 'bo', markersize=11)
  
  for label, xpt, ypt in zip(labels,x,y):
    plt.text(xpt,ypt,label)

  plt.show()