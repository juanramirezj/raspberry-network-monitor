import sys
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18,8)
luminosidad = int( sys.argv[3] )
if sys.argv[2] == '1':
   pixels[int(sys.argv[1])] = (0,luminosidad,0)
else:
   pixels[int(sys.argv[1])] = (luminosidad,0,0)
