import radio
import random
from microbit import *
radio.on()
my_ipaddress="192.34.1.5"
my_macaddress="D4:6B:44:1G:3A:Z4"
finding_ip="192.168.1.41"
arp_frame=my_ipaddress+my_macaddress+finding_ip
radio.config(address=1)
rad_send=1
arp_table = [[]]
state=0
while True:
    if state==0 :

            if button_a.was_pressed():

                radio.send(arp_frame)

                state=1

    rece=radio.receive()
    if state==1:
        display.show(Image.SAD)


        if rece != None:
            state=0
            display.show(Image.HAPPY)
            sleep(300)
            display.clear()
            sleep(500)
            display.show(Image.HAPPY)
            sleep(300)
            display.clear()
            sleep(500)
            arp_table.append(rece)
            for i in arp_table:
                display.show(i)
            sleep(500)
            display.clear()













