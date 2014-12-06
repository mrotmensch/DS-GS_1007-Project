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
  address = validate_address(address_input)
  if address != "Not a Valid Address":
    if validate_ny_address(address):
      address = user_location(address_input)
      return address
    else:
      raise NotInNYException
      print "This address is not in New York"
  else:
    raise InvalidInputException
    print "Address entered is not valid"
  
def validate_address(address):
  '''
  this function checks whether the user input is a valid address
  '''
  try:
    address = Geocoder.geocode(address)
  except GeocoderError:
    return "Not a Valid Address"

  return address

def validate_ny_address(address):

  if address.administrative_area_level_1 != "New York":
    return False
  else:
    return True
     
