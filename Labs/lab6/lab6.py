# -*- coding: utf-8 -*-
"""
ENGI1020 - Fall 2020 - Lab 6
Lori Hogan (c)2020
"""

from engi1020.arduino import *
from time import *
import matplotlib.pyplot as plt
import numpy as np 
##TODO 3.3 - Will need to import graphing-related
##          modules


#Global variables (will want to make local in 3.2)
interval = 0.1 #time between samples in seconds
analogPin = 0 #Grove port for analog sensor
buttonPin = 5 #Grove port for button
dataCollection = [] #list to store data from analog
times = []


def gatherinfo(analogPin,buttonPin,interval):
    buttonval= digital_read(buttonPin)
    currentTime = 0
    while buttonval == 0:
        times.append(currentTime)
        currentTime += 0.1 
        tempinput = temp_celsius(0)
        dataCollection.append(tempinput)
        buttonval = digital_read(buttonPin)
        sleep(interval)
        
    sumvalues = 0
    for i in dataCollection:
        sumvalues += i
    Average= sumvalues/ len(dataCollection)
    return dataCollection, Average
print(gatherinfo(0,5,0.1))

##TODO 3.3 - Modify above function implementation
##          to include plotting of data

plt.plot(times,dataCollection, label = "Average data" )
plt.xlabel("Time (ms)")
plt.ylabel("Temperature(C)")
