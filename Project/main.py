from Classes.location_class import *
from userInput import get_manual_input, convert_address
from userOutput import output_map, get_output_coord
from geoCoding.mapOutput import mapOutput, mapImage,closeMap
import sys

def main():

  while True:
    try: 
      address = get_manual_input()
      address= convert_address(address)
    
      wifi = NearestWifi()
    
      print "Searching for: \n" + address + '\n\n'
      search_results = wifi.search_results(address)
      show_results = ['Name','Location','Location_T','SSID','Type','distance']
      print search_results[show_results].reset_index(drop = True)
      
      
      url = mapOutput(wifi.long_, wifi.lat,search_results)
      image = mapImage(url)
      image.show()
      break

    except UnreadableData as u:
      print u

    except (EmptyStringException, NotInNYException, GeocoderError, InvalidInputException, Address_not_valid) as e:
      print "Please enter a valid address in NYC to search"

    except KeyboardInterrupt as k :
      print " \n you chose to terminate the program... goodbye!"
      sys.exit()
  

  while True:
    more = raw_input("Type Y for next 5 results or C to change address: ")
    if more.lower() == 'y':
      search_results = wifi.search_results(address)
      print search_results[show_results]#.reset_index(drop = True)
      
      url = mapOutput(wifi.long_, wifi.lat,search_results)
      image = mapImage(url)
      image.show()
      
    elif more.lower() == 'c':
      main()
    else:
      print " \n you chose to terminate the program... goodbye!"
      sys.exit()
  

if __name__ == '__main__':
  #try:
  main()
  
