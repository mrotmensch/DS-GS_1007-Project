from location_class import *
from userInput import get_manual_input, convert_address
from userOutput import output_map, get_output_coord
from geoCoding.mapOutput import mapOutput, mapImage,closeMap
import sys

def main():
  address = get_manual_input()
  address= convert_address(address)
  
  wifi = NearestWifi()
  
  print "Searching for: \n" + address + '\n\n\n'
  search_results = wifi.search_results(address)
  show_results = ['Name','Location','Location_T','SSID','Type','distance']
  print search_results[show_results].reset_index(drop = True)
  
  url = mapOutput(wifi.long_, wifi.lat,search_results)
  image = mapImage(url)
  image.show()
  #output_map(wifi.long_,wifi.lat,search_results)

  while True:
    more = raw_input("Type Y for next 5 results or C to change address: ")
    if more.lower() == 'y':
      closeMap()
      search_results = wifi.search_results(address)
      print search_results[show_results].reset_index(drop = True)
      url = mapOutput(wifi.long_,wifi.lat,search_results)
      image = mapImage(url)
      #output_map(wifi.long_,wifi.lat,search_results)
    elif more.lower() == 'c':
      main()
    else:
      sys.exit()
  

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    sys.exit()