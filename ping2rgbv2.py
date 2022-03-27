import os
import sys
import board
import neopixel
from random import seed
from random import randint
#import date
import datetime

pixels = neopixel.NeoPixel(board.D21,8)


def enciendeRGB(led, estado, luminosidad):
   if estado:
      pixels[led] = (0,luminosidad,0)
   else:
      pixels[led] = (luminosidad,0,0)
   return

def randomRGB(led, luminosidad):
   r = randint(0, luminosidad)
   g = randint(0, luminosidad)
   b = randint(0, luminosidad)
   pixels[led] = (r,g,b)
   return

now = datetime.datetime.now()
if now >= now.replace(hour=8) and now <= now.replace(hour=22):
   lumi = int(sys.argv[1] )
else:
   lumi = int(sys.argv[2] )

for led in range(0,8):
    randomRGB(led,lumi)

p0 = 0 == os.system('ping -qc 3 www.facebook.com     >> /dev/null')
enciendeRGB(0, p0, lumi)

p1 = 0 == os.system('ping -qc 3 www.bci.cl     >> /dev/null')
enciendeRGB(1, p1, lumi)

p2 = 0 == os.system('ping -qc 3 www.tevapharm.com     >> /dev/null')
enciendeRGB(2, p2, lumi)

p3 = 0 == os.system('ping -qc 3 www.instagram.com     >> /dev/null')
enciendeRGB(3, p3, lumi)

p4 = 0 == os.system('ping -qc 3 www.latercera.com     >> /dev/null')
enciendeRGB(4, p4, lumi)

p5 = 0 == os.system('ping -qc 3 www.amazon.com     >> /dev/null')
enciendeRGB(5, p5, lumi)

p6 = 0 == os.system('ping -qc 3 www.pcfactory.cL   >> /dev/null')
enciendeRGB(6, p6, lumi)

p7 = 0 == os.system('ping -qc 3 www.microsoft.com   >> /dev/null')
enciendeRGB(7, p7, lumi)




dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
if (not p0 and not p1 and not p2 and not p3 and not p4 and not p5 and not p6 and not p7):
    f = open("/home/pi/ErrorRed.txt","a")
    f.write('Error de conexión internet a las %s\n\r'% ( dt_string))
    f.close()



