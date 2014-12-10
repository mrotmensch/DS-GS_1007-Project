
NYC Free Wifi Project 
======================
Created by Lucy Wang and Maya Rotmesch.
Last Edits made: 12/13/2014


CONTENTS OF THIS FILE
----------------------
 * Introduction
 * Requirements
 * How to run 
 * Expected results


INTRODUCTION
------------

This program was created to help users identify public Wi-Fi locations that are closest to an address-of-interest.
To do so, the user provides the program with an address in NYC and the program finds the 5 nearest Wifi hot-spots and presents them to the user (in the terminal) from closest to farthest. In addition, in order to help to user locate these hot-spots more easily, a map is provided with marker to indicate both the address the user searched for (in blue), and the location of the hot-spots (red). Lastly, the program also saves several figures displaying statistics about the free Wifi locations in NYC.


REQUIREMENTS
-------------
In order to run this program successfully, you must ensure the following packages installed:
(It is possible that the program will run without problem on earlier versions of the required packages. However to ensure optimal performance, please )

    * This program runs on Python 2.7.
    * matplotlib - version 1.4.0
        can be installed via pip install matplotlib
    * pandas - version 15.1
        can be install via pip pandas
    * pygeocoder
        can be installed via pip install pygeocoder
    * motionless
        can be installed via pip install motionless


HOW TO RUN
-----------
To run the program, please navigate to the Project folder where you will find main.py. The entire program is initiated when running : **python main.py** from your terminal. 


EXPECTED RESULTS
----------------

When the program is run from the project folder via **python main.py** a prompt should appear in the terminal, prompting the user to input an address located in NYC. 
Examples of valid input are:

    * 726 Broadway 
    * 726 broadway new york

If the user input cannot be automatically decoded by the pygeocoder module, the program will attempt to auto correct the address. If the address cannot be corrected, the user will be prompted to enter the address again.

Once the user inputs a valid address:

    * A list of the 5 closest Wifi locations will be listed on the terminal screen with useful characteristics to help the user locate the hot-spot (such as: Name of hot-spot, location, location type, SSID - the name of network the user should look for, the type of the network - either free or limited-free, and the distance from the entered address). 
    * A map of the relevant area in NYC will be displayed with a blue marker labeling the address the user searched for (in blue), and a marker denoting the location of the hot-spots (red).
    * a heat-map figure showing the concentration of Wifi networks by a given provider will be saved to file as "heatmap.pdf"
    * a bar graph showing TODO

after the output it displayed, the user will be prompted to either:

    * type 'Y' to displayed the 5 next-closest Wifi hot-spots.
    * type 'C' to search to a different address
    * type any other key to quit the program.



''' Readme Template from https://www.drupal.org/node/2181737'''