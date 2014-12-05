'''
Dec 1 2014

@author: lucy wang

'''
import re
import sys
from pygeocoder import Geocoder
from pygeolib import GeocoderError
from geoCoding.geoCoding import user_location, get_coordinates
from customExceptions.customExceptions import EmptyStringException

def get_manual_input():
  '''
  this function takes an input from the user
  '''
  address_input = raw_input('Address to search: ')
  if address_input == "":
    raise EmptyStringException

  return address_input

def convert_address(address_input):
  '''
  this function converts an inputed address into a geocoder formatted address and coordinates

  user_location and get_coordinates are functions built in the geoCoding module
  '''
  validate_address(address_input)
  address = user_location(address_input)
  latitude, longitude = get_coordinates(address)

  return address, latitude, longitude
  
def validate_address(address):
  '''
  this function checks whether the user input is a valid address
  '''
  try:
    address = Geocoder.geocode(address)
  except GeocoderError:
    print "The address entered cannot be found"
    sys.exit(1)

