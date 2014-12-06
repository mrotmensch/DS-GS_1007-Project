from location_class import *
from userInput import get_manual_input, convert_address
from userOutput import output_map, get_output_coord
import sys

def main():
  address = get_manual_input()
  address= convert_address(address)
  
  wifi = NearestWifi()
  
  print "Searching for: \n" + address + '\n\n\n'
  search_results = wifi.search_results(address)
  print search_results
  
  output_map(wifi.long_,wifi.lat,search_results)

  while True:
    more = raw_input("Type Y for next 5 results or C to change address: ")
    if more.lower() == 'y':
      search_results = wifi.search_results(address)
      print search_results
      output_map(wifi.long_,wifi.lat,search_results)
    elif more.lower() == 'c':
      main()
    else:
      sys.exit()
  

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    sys.exit()