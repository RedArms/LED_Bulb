import pytuya 
import time
d = pytuya.BulbDevice('eb24ee55d15b03d5166pwb', '192.168.0.101', '783cb6fa9e058b5c')
d.set_version(3.3)  
d.turn_on()


a = 255 
b = 0
c = 0


def rgb_rainbow():
    while True:
        a = 255 
        b = 0
        c = 0
        while b < 255:
            d.set_colour(a,b,c)
            b += 5
        while a !=0:
            d.set_colour(a,b,c)
            a -= 5
        while c < 255:
            d.set_colour(a,b,c)
            c += 5
        while b !=0:
            d.set_colour(a,b,c)
            b -= 5
        while a < 255:
            d.set_colour(a,b,c)
            a += 5
        while c !=0:
            d.set_colour(a,b,c)
            c -= 5

rgb()



time.sleep(1)

d.turn_off()



data = d.status()
print('Dictionary %r' % data)


