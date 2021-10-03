import board
import neopixel
# Docs and Links:
# https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel
# https://circuitpython.readthedocs.io/projects/neopixel/en/latest/api.html
# https://avwx.docs.apiary.io/#reference/0/metar/get-metar-report

pixel = neopixel.NeoPixel(board.D18, 2, pixel_order=neopixel.RGBW, auto_write=False)
pixel[0] = (30, 0, 0, 0)
pixel[1] = (0, 0, 30, 0)
pixel.show()
