import board
import neopixel
pixels = neopixel.NeoPixel(board.D18,8)
for i in range(8):
   pixels[i] = (0,0,0)

