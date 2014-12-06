'''
Dec 1 2014

@author: lucy wang

'''
import re
import sys
from pygeocoder import Geocoder
from pygeolib import GeocoderError

from geoCoding.geoCoding import user_location
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
    address = Geocoder.geocode(address_input)
  except GeocoderError as G:
    print "we should change this later"

  if address.valid_address != True:
    print "raise exception."
    sys.exit()


  try:
    address = user_location(address_input)
  except GeocoderError:
    print "Address entered is not valid"

  return address

     
