import matplotlib.pyplot as plt
import numpy as np
from Classes.location_class import *
from userInterface.userInput import get_manual_input, convert_address

def plot_barchart(DF):
  '''
  this function plots the number of free wifi spots in the five boroughs as a histogram
  '''

  fig = plt.figure()
  ax = fig.add_subplot(111)

  plot_data = DF['Borough'].value_counts()
  
  row_labels = list(plot_data.index)

  plot_data.plot(plot_data,kind='bar',figsize = (10,10), alpha = 0.8)

  ax.set_ylabel('Count of Wifi Spots')
  xtickNames = ax.set_xticklabels(row_labels)
  plt.setp(xtickNames, rotation=45, fontsize=12)
  ax.grid(False)

  fig.savefig('Free Wifi by Borough.png')
  plt.close()

  plt.draw()
