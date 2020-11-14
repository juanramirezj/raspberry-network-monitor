import os
import sys
import board
import neopixel
from random import seed
from random import randint
import datetime
from sense_hat import SenseHat

sense = SenseHat()

pixels = neopixel.NeoPixel(board.D18,8)


def enciendeRGB(led, estado, luminosidad):
   if estado:
      pixels[led] = (0,luminosidad,0)
      sense.set_pixel(led,7, 0, luminosidad,0)
   else:
      pixels[led] = (luminosidad,0,0)
      sense.set_pixel(led,7, luminosidad,0,0)

   return

def randomRGB(led, luminosidad):
   r = randint(0, luminosidad)
   g = randint(0, luminosidad)
   b = randint(0, luminosidad)
   pixels[led] = (r,g,b)
   sense.set_pixel(led,7,r,g,b)
   return

p0 = 0 == os.system('ping -qc 1 www.facebook.com     >> /dev/null')
p1 = 0 == os.system('ping -qc 1 www.bci.cl     >> /dev/null')
p2 = 0 == os.system('ping -qc 1 www.tevapharm.com     >> /dev/null')
p3 = 0 == os.system('ping -qc 1 www.instagram.com     >> /dev/null')
p4 = 0 == os.system('ping -qc 1 www.latercera.com     >> /dev/null')
p5 = 0 == os.system('ping -qc 1 www.amazon.com     >> /dev/null')
p6 = 0 == os.system('ping -qc 1 www.pcfactory.cL   >> /dev/null')

now = datetime.datetime.now()
if now >= now.replace(hour=8) and now <= now.replace(hour=22):
   lumi = int(sys.argv[1] )
   sense.low_light = False
else:
   lumi = int(sys.argv[2] )
   sense.low_light = True

for y in range (1,8):
    for x in range (0,8):
        p = sense.get_pixel(x,y)
        p[0] = int(p[0] * (0.2 + max(y,6)/10))
        p[1] = int(p[1] * (0.2 + max(y,6)/10))
        p[2] = int(p[2] * (0.2 + max(y,6)/10))

        sense.set_pixel(x,y-1, p) 

enciendeRGB(0, p0, lumi)
enciendeRGB(1, p1, lumi)
enciendeRGB(2, p2, lumi)
enciendeRGB(3, p3, lumi)
enciendeRGB(4, p4, lumi)
enciendeRGB(5, p5, lumi)
enciendeRGB(6, p6, lumi)
randomRGB(7, lumi)





