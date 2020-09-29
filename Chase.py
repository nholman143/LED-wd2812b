"""
LED chase animation loop
"""

import board
import time
import neopixel
#Name leds, set pin location, and led count
pixels = neopixel.NeoPixel(board.D18, 120)

#Set value to zero, x will be used for indexing
#Since indexing starts at zero and will be adding 1 before the animations start
#Keep set to -1
x = -1

while True:

#Adds +1 to index
    x = x+1
    time.sleep(0.001)
#Light up LED
    pixels[x] = (0, 0, 255)
#Turn off LED
    time.sleep(0.001)
    pixels[x] = (0, 0, 0)

#Since indexing starts at 0 take the number of LED and subtract one
#This will start over the index count once all LEDS have been lit
    if x == 109:
        x = -1
        
    
    
    