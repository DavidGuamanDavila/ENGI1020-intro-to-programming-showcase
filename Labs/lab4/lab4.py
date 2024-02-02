###ENGI1020 - Fall 2020
###Lab 4 Starting Script
###(c) Lori Hogan, <your name here>

from engi1020.arduino import *
from time import sleep


# In Part 3.1.1 of Lab 4, we want to get the AVERAGE of ten samples

# averagevalue = 0

# for i in range(10):
    
#     readvalue = analog_read(1)
#     print(readvalue)
#     sleep(0.1)
#     averagevalue += readvalue
    
# Avg = averagevalue/10
# print(Avg)

#TODO - Test this using print() before moving on to next part

# In Part 3.1.2 of Lab 4, we want to implement our flow chart 
#   from Prep Design (b)
SMsetting = 90 #TODO - Replace 0 with reasonable output for device
RDthreshold = 500 
#TODO - Implement branching that incrementally manipulates output depending
#       on average input

servo_move(5,0)
while True:
    averagevalue = 0

    for i in range(10):
        readvalue = analog_read(1)
        sleep(0.1)
        averagevalue += readvalue   
    Avg = averagevalue/10
    
    if Avg <= RDthreshold:
        SMsetting += 5
    elif Avg > RDthreshold:
        SMsetting -= 5
        
    if SMsetting >= 180:
        SMsetting = 180
    elif SMsetting <= 0:
        SMsetting = 0
        
    servo_move(5, SMsetting)
    sleep(1)
    print("AvgRead: {0}, RDsetting: {1}".format(Avg, SMsetting)) 



