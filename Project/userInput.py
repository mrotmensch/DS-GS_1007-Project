'''
Dec 1 2014

@author: lucy wang

'''
import re
import sys
from pygeocoder import Geocoder
from pygeolib import GeocoderError
<<<<<<< HEAD
from geoCoding.geoCoding import user_location
=======
from geoCoding.geoCoding import user_location, get_coordinates
>>>>>>> 2e977fa02516fc8ca5004310d2dc1bbcfc3463af
from customExceptions.customExceptions import *

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
  try:
    address = user_location(address)
  except GeocoderError:
    print "Address entered is not valid"

  return address

     
