# -*- coding: utf-8 -*-

import os
import sys
import board
import neopixel
from random import seed
from random import randint
#import date
import datetime
from time import sleep

#board.D21 measns GPIO21 (physical pin 40)
pixels = neopixel.NeoPixel(board.D21,8)
#pixels = neopixel.NeoPixel(board.D10,8)


def enciendeRGB(led, estado, luminosidad):
    lumi0 = 1 
    lumif = luminosidad
    lumis = 5 
    p = 0.1

    if estado:
      for i in range(lumi0, lumif, lumis):
         pixels[led] = (0,i,0)
         sleep(p)
    else:
      for i in range(lumi0, lumif, lumis):
         pixels[led] = (i,0,0)
         sleep(p)
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

p1 = 0 == os.system('ping -qc 3 docker.local     >> /dev/null')
enciendeRGB(1, p1, lumi)

#NVR
p2 = 0 == os.system('ping -qc 3 192.168.0.155     >> /dev/null')
enciendeRGB(2, p2, lumi)

#BALCON
p3 = 0 == os.system('ping -qc 3 192.168.0.161     >> /dev/null')
enciendeRGB(3, p3, lumi)

p4 = 0 == os.system('ping -qc 3 repo2020.local     >> /dev/null')
enciendeRGB(4, p4, lumi)

#ROUTER PRIMER PISO
p5 = 0 == os.system('ping -qc 3 192.168.0.199     >> /dev/null')
enciendeRGB(5, p5, lumi)

#ROUTER JR-15 SEGUNDO PISO
p6 = 0 == os.system('ping -qc 3 192.168.0.2   >> /dev/null')
enciendeRGB(6, p6, lumi)


#ROUTER JR-5 Y JR-6 SEGUNDO PISO
p7 = 0 == os.system('ping -qc 3 192.168.0.1   >> /dev/null')
enciendeRGB(7, p7, lumi)




dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
if (not p0 and not p1 and not p2 and not p3 and not p4 and not p5 and not p6 and not p7):
    f = open("/home/pi/ErrorRed.txt","a")
    f.write('Error de conexión internet a las %s\n\r'% ( dt_string))
    f.close()



