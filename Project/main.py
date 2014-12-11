
'''
Created by: Lucy Wang.
Modified by: Maya Rotmensch and Lucy Wang.

'''

import requests
from Classes.location_class import *
from userInterface.userInput import get_manual_input, convert_address
from graphicOutput.mapOutput import mapOutput, mapImage
from graphicOutput.heatmap import heat_map
from graphicOutput.barchart import plot_barchart
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
      new_index = [1,2,3,4,5]
      result = search_results[show_results].set_index([new_index])
      print result 
      
      url = mapOutput(wifi.long_, wifi.lat,search_results)
      image = mapImage(url)
      image.show()

      heat_map(wifi.clean_data)
      plot_barchart(wifi.clean_data)
      break
    
    except requests.ConnectionError as c:
      print "Please make sure you are connected to the internet"
    
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
      result = search_results[show_results].set_index([new_index])
      print result

      url = mapOutput(wifi.long_, wifi.lat,search_results)
      image = mapImage(url)
      image.show()
      
    elif more.lower() == 'c':
      main()
    else:
      print " \n you chose to terminate the program... goodbye!"
      sys.exit()
  

if __name__ == '__main__':

  main()
  
