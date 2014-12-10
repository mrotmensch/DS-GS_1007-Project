import matplotlib.pyplot as plt
import numpy as np
from Classes.location_class import *
from userInput import get_manual_input, convert_address
def heat_map(DF):
    '''
    TODO
    '''
    Provider = DF.Provider
    Borough = DF.Borough


    new_df = pd.get_dummies(Provider)
    new_df['Borough'] = Borough
    map_data = new_df.groupby('Borough').sum()


    map_data_trans = map_data.T
    fig, ax = plt.subplots()
    heatmap = ax.pcolor(map_data_trans, cmap=plt.cm.Blues)

    column_labels = map_data_trans.columns
    row_labels = map_data_trans.index

    print map_data_trans.shape

    # want a more natural, table-like display
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    #ax.set_yticks(rotation = 35)

    #put the major ticks at the middle of each cell
    ax.set_xticks(np.arange(map_data_trans.shape[1])+0.5, minor=False)
    ax.set_yticks(np.arange(map_data_trans.shape[0])+0.5, minor=False)

    ax.set_xticklabels(column_labels, minor=False)
    y = ax.set_yticklabels(row_labels, minor=False)
    ax.labelsize(8)


    #plt.setp(y, rotation=35)
    #ax.set_aspect(0.5)
    
    #plt.tight_layout()
    plt.show()


#http://stackoverflow.com/questions/14391959/heatmap-in-matplotlib-with-pcolor.

if __name__ == '__main__':
    address = get_manual_input()
    address= convert_address(address)
    wifi = NearestWifi()
    search_results = wifi.search_results(address)

    heat_map(wifi.clean_data)

