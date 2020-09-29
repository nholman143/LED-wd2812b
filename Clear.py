"""
Simple Script to Clear out LEDS
"""

import board
import time
import neopixel

#Name leds, set pin location, and led count
pixels = neopixel.NeoPixel(board.D18, 110)

pixels.fill((0, 0, 0))
 
