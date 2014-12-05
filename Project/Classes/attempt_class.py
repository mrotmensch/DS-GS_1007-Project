import sys
import math as mt
import re
import pandas as pd
import numpy as np
import urllib2
import csv
from pygeocoder import Geocoder

import sys

from Math_calculations.distance import *

class UnreadableData(Exception):
    pass


class MyClass:
    """A simple example class"""
    def __init__(self):
        self.file_name = "NYC_Free_Public_Wifi.csv"
        try:
            self.data = pd.read_csv(self.file_name)
        except:
            raise UnreadableData("File cannot load. Please make sure file exists")

    def cleanData(self):
        columns = ['Boro','Type','Provider','Name','Location','Lat','Long_','X','Y','Location_T','City','SSID']
        df_cut = self.data[columns]
        boro = {'BK': 'Brooklyn', 'MN': 'Manhattan', 'SI':'Staten Island', 'QU':'Queens', 'BX':'Bronx'}
        df_cut['Borough'] = df_cut['Boro'].apply(lambda name: boro[name])
        df_cut2 = df_cut.drop('Boro',1)
        df_dropNaN = df_cut2.dropna(subset = ['Lat','Long_'])
        df_new = df_dropNaN.replace(np.nan,"Unknown")
        self.clean_data = df_new
        return 

    def __df_boro(self, address):
        street, city, state, zipcode = address.replace(' ','').split(",")
        df_mask = self.clean_data.loc[(self.clean_data["Borough"] == city)]
        return df_mask

    def find_loc(self, address):
        df = self.__df_boro(address)
        df["distance"] = df.apply(lambda row: distance(lat2,long2,row['Lat'], row['Long_']), axis=1)
        df_new = df.sort(columns = "distance")
        return df_new

    #def search_results(self):
    #    __find_loc(self)





x = MyClass()
x.cleanData()
print x.clean_data.head()
address = "390 South 2nd Street, Brooklyn, NY 11211, USA"

print x.find_loc(address)

