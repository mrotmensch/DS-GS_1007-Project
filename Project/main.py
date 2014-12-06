from location_class import *
from userInput import get_manual_input, convert_address
import sys

def main():
  address = get_manual_input()
  address= convert_address(address)
  
  print address
  wifi = NearestWifi()
  print wifi.search_results(address)
  
  while True:
    more = raw_input("Type Y for next 5 results: ")
    if more.lower() == 'y':
      print wifi.search_results(address)
    else:
      sys.exit()
  

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    sys.exit()