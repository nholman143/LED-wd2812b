"""
RGB Script for WS2812b and Raspberry Pi
"""
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 110)


def sequence_light_up(count, color):
    """
    Lights up each LED Individually
    :param color: LED Color
    :param count: LED Count
    :return:
    """
    for x in range(count):
        # Count needs to be +1 the amount of individual pixels
        time.sleep(.001)
        # Change the above in the parentheses to adjust time delay
        pixels[x] = color


def sequence_light_off(count):
    """
    Individually turns LEDs Off
    :param count: LED count
    :return:
    """
    for x in range(count):
        # Count needs to be +1 the amount of individual pixels
        time.sleep(.001)
        # Change the above in the parentheses to adjust time delay
        pixels[x] = (0, 0, 0)


def light_chase(count, color):
    """
    Individually turn on each LED then turn off
    :param count: LED Count
    :param color: LED Count
    :return:
    """
    for x in range(count):
        # Count needs to be +1 the amount of individual pixels
        time.sleep(.001)
        # Change the above in the parentheses to adjust time delay
        pixels[x] = color
        time.sleep(.001)
        # Change the above in the parentheses to adjust time delay
        pixels[x] = (0, 0, 0)


def solid_color(color):
    """
    Turns LEDs On
    :param color: LED Color, can be used to turn off LEDs as well
    :return:
    """
    # Fills all the LEDs to the color which will be called later
    pixels.fill(color)


while True:
    sequence_light_up(111, (0, 0, 255))
    sequence_light_off(111)
    sequence_light_up(111, (0, 255, 0))
    sequence_light_off(111)
    solid_color((0, 0, 255))
    solid_color((0, 0, 0))
    solid_color((255, 0, 0))
    solid_color((0, 0, 0))
    solid_color((0, 255, 0))
    light_chase(111, (0, 0, 255))
    light_chase(111, (0, 255, 0))
    light_chase(111, (255, 0, 0))
    light_chase(111, (0, 255, 0))
    if input("Type exit to exit: ") == "exit":
        break
