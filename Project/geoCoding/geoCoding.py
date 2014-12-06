'''
December 4, 2014

@author: 
'''

from pygeocoder import Geocoder
from pygeolib import GeocoderError
import __builtin__

def user_location(address):
  state_city = set(['new york','New York','ny','NY','Ny','New york','new York'])
  if __builtin__.any(keyword in address for keyword in state_city):
    address_state = Geocoder.geocode(address)
  else:
    address_state = Geocoder.geocode(address + "New York")
  
  return address_state.formatted_address


