import radio
from microbit import *
radio.on()
radio.config(address=1)
ip_Adress="192.1.1.41"
Mac_Address="0K:1B:44:11:3A:B7"
my_address=ip_Adress+Mac_Address
state=0
hel=0
while True:
    if state==0:
        rad=radio.receive()
        if rad!=None:
            if rad[:10]=="192.34.1.5":
                state=1





    if state==1:
        if rad != None:
            radio.send(my_address)
            display.show(Image.HAPPY)
            hel=hel+1










