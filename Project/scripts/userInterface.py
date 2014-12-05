'''
Dec 1 2014

@author: lucy wang

'''
import re
import sys
from pygeocoder import Geocoder
from pygeolib import GeocoderError

def get_manual_input():
  
  address_input = raw_input('Address to search: ')
  if address_input == "":
    raise EmptyStringException

  return address_input

def convert_address(address_input):
    validate_address(address_input)
    address = user_location(address_input)
    latitude, longitude = get_coordiates(address)

    return address, latitude, longitude
  
def validate_address(address):

  try:
    address = Geocoder.geocode(address)
  except GeocoderError:
    print "The address entered cannot be found"
    sys.exit(1)

