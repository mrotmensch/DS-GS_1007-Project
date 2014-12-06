from location_class import *
from userInput import get_manual_input, convert_address
#from userOutput import output_map
import sys

def main():
  address = get_manual_input()
  address= convert_address(address)
  
  
  wifi = NearestWifi()
  print "searching for \n" + address + '\n\n\n'
  print wifi.search_results(address)
  

  while True:
    more = raw_input("Type Y for next 5 results or C to change address: ")
    if more.lower() == 'y':
      print wifi.search_results(address)
    elif more.lower() == 'c':
      main()
    else:
      sys.exit()
  

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    sys.exit()