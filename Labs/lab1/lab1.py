from engi1020.arduino import *
x=temp_celsius(0)
print(x)
y=-0.07*x+2.1
print(y)
lcd_hsv(y,1, 255)

