import board
import time
import neopixel

#Name leds, set pin location, and led count
pixels = neopixel.NeoPixel(board.D18, 120)

#Simple loop
while True:
#.fill to light up all the leds
    pixels.fill((0, 0, 255))
    time.sleep(1)
    pixels.fill((255, 0, 0))
    time.sleep(1)
