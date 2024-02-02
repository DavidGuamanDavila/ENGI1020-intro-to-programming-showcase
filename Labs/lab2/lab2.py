# Lab 2 Starting Script
# ENGI1020 - Fall 2020
# (c) Lori Hogan, <Anton Guaman>

from engi1020.arduino import *

choice = int(input('Press 1 to test digital input (button or touch sensor), 2 to test analog input (rotary dial)'))

if choice == 1:
    
    print('Digital input being tested')
    # Here is where you will implement Procedure 3.1
     
    inputs = digital_read(4)
    
    if inputs == 1:
        
        digital_write(2,1)
    
elif choice == 2:
    
    print('Analog input being tested')
    # Here is where you will implement Procedure 3.2
    
    inputj = analog_read(0)
    
    if inputj < 600:
        
        print("Low")
        print(inputj)
        
    else: 
        print("High")
        print(inputj)
    
else:
    print('Incorrect selection. Run script again!')
