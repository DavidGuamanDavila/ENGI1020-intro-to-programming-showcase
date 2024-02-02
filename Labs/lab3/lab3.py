
from engi1020.arduino import *

# In Part 3.1 of Lab 3, we want to read our analog input device
# and manipulate the LCD output. We also want to manipulate the alarm
# IFF the button is NOT pressed. Specific sections referenced in
# below pseudocode

"""
Pseudocode from Preparation page (for Procedure 3.1)

    read the input devices (ref Procedure 3.1.1)

    convert the input analog reading to an output value for LCD Screen
    manipulate LCD screen output (ref Procedure 3.1.2)

    if the reading is above a given _threshold value_ AND the digital input
    {button} is NOT pressed (ref Procedure 3.1.3) 
        manipulate digital output device to show "alarm criteria" met
        (ref Procedure 3.1.3) 
"""
while True :
    x = temp_celsius(1)
    print(x)
    y = -0.07 * x + 20 * 0.07
    print(y)
    lcd_hsv(y,1, 255)
    
    buttonpress = digital_read(8)
    
    if x > 23 and buttonpress == 1:
            digital_write(3,1)
            
    else: 
            digital_write(3,0)
    
    



# In Part 3.2 of Lab 3, we will test as per the preparation test matrix

# In Part 3.3 of Lab 3, we will watch a video and use example
# to implement infinite loop in lab, and observe result
    
