# -*- coding: utf-8 -*-
"""
Lab 5

@author: lorih
"""
from time import *
from random import *
from engi1020.arduino import *

    
"""
Turns LED on and off for specified time period

Parameters:
    pin - int in range [2, 8] represents digital port
        LED is connected to
    delay - time in s between turning LED on and off
Returns:
    None
"""
def blinkLed(pin, delay):
    digital_write(pin, 1)
    sleep(delay)
    digital_write(pin, 0)
    sleep(delay)


"""
Checks two digital inputs and indicates which (if any)
 are activated

Parameters:
    pin1 - int in range [2, 8] represents digital port
        one digital input is connected to
    pin2 - int in range [2, 8] represents digital port
        one digital input is connected to, pin1 != pin2
Returns:
    int indicating if neither input is activated (0),
        if one input is activated (pin value), or if
        both inputs are actiuvated (sum of pin values)
"""
def checkDigitalInputs(pin1, pin2):
    val = 0
    if digital_read(pin1) == 1 and digital_read(pin2) == 0:
        val = pin1
    elif digital_read(pin1) == 0 and digital_read(pin2) == 1:
        val = pin2
    elif digital_read(pin1) == 1 and digital_read(pin2) == 1:
        val = pin1+pin2
        
    return val
        
"""
Returns time in specified units between start of game
    and now

Parameters:
    startTime - float, time game started represented by 
        seconds since epoch 
    units - string repesenting return value units
        'm' = milliseconds
        'min' = minutes
        Anything else = seconds
Returns:
    float representing time difference between gameStart
        and now, converted to desired units
"""
def gameTime(startTime, units):
    # TODO 3.2 - Given specification and 'empty' function
    # complete function definition (see video!!)
    duration= time() - startTime
    
    if units == "m":
        duration *= 1000
    elif units == "min":
        duration /= 60
    return duration

# Define variables to hold pin values
b1 = 2
b2 = 4
led = 6
rotary = 0

# Give player choice of games
choice = int(input('Press 1 for Speed Work, 2 for Hot-Cold:'))

# Calculate start time
start = time()
if choice == 0:
    print('You are testing gameTime() Function')
    input('Press enter after approximately five seconds')
    print('gameTime() calculated', gameTime(start,"s") , 'seconds')
    
if choice == 1:
    print('You chose Speed Work')
    
    #TODO 3.1 - Change LCD screen to white
    lcd_rgb(225, 225, 225)
    waitTime = randint(1, 6)
    sleep(waitTime)
    lcd_rgb(255,0,0)
    #TODO 3.3 - Implement loop algorithm 
    winner = checkDigitalInputs(b1, b2)
    while  winner == 0:
        sleep(0.05)
        winner = checkDigitalInputs(b1, b2)
        
    lcd_rgb(0, 255, 0)
    
   
    #TODO 3.4 - Print winner and game time
    print(gameTime(start, 's'))
    print(winner)
    
    
elif choice == 2:
    print('You chose Hot-Cold')
    
    #TODO 3.1 - Blink LED for 1s
    
    #TODO 3.3 - Implement loop algorithm
    
    #TODO 3.4 - Print rotary setting and game time 
    
    
    
    
    



