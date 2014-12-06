from pylab import *
from mpl_toolkits.basemap import Basemap
import matplotlib.pylot as plt
import numpy as np

def output_map(user_lat, user_long,lllong,lllat,urlong,urlat,wifi):
  pylab.rcParams['figure.figsize'] = (8.0,6.4)

  map = Basemap(projection='merc', lat_0 = user_lat, lon_0 = user_long, resolution = 'h', area_thresh = 0.1 , llcrnrlon = lllong, llcrnrlat= lllat, ,urcrnrlon = urlong, urcrnrlat = urlat)
   
  map.drawcoastlines()
  map.drawcountries()
  map.fillcontinents(color = 'white')
  map.drawmapboundary()

  lon = list(wifi[0])
  lat = list(wifi[1])
  label = list(wifi[2])
  x,y = map(lon, lat)
  map.plot(x, y, 'bo', markersize=11)
  
  for label, xpt, ypt in zip(labels,x,y):
    plt.text(xpt,ypt,label)

  plt.show()