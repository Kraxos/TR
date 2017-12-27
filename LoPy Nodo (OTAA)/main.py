""" OTAA Node example compatible with the LoPy Nano Gateway """

from machine import UART
from network import LoRa
import pycom
import socket
import binascii
import struct
import time
import config

# UART Data Transmission (Raspberry Pi)
pycom.heartbeat(False) # turn off heartbeat

uart1 = UART(1, 115200, bits=8, parity=None, stop=1)
uart1.init(baudrate=115200, bits=8, parity=None, stop=1, timeout_chars=2, pins=("P3", "P4"))
uart1.write("Connected...")

# initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)

# create an OTA authentication params
dev_eui = binascii.unhexlify('00 6D 13 E0 C6 53 09 5F'.replace(' ','')) ## Parameters have altrady been replaced with the ones in TTN
app_eui = binascii.unhexlify('70 B3 D5 7E D0 00 78 55'.replace(' ',''))
app_key = binascii.unhexlify('3E 36 4E 3D AE 98 85 F6 A9 94 48 59 C8 64 4B C7'.replace(' ',''))

# set the 3 default channels to the same frequency (must be before sending the OTAA join request)
lora.add_channel(0, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)
lora.add_channel(1, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)
lora.add_channel(2, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)

# join a network using OTAA
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0, dr=config.LORA_NODE_DR)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not joined yet...')

# remove all the non-default channels
for i in range(3, 16):
    lora.remove_channel(i)

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, config.LORA_NODE_DR)

# make the socket blocking
s.setblocking(False)

time.sleep(5.0)

'''
for i in range (200):
    s.send(b'PKT #' + bytes([i]))
    time.sleep(4)
    rx, port = s.recvfrom(256)
    if rx:
        print('Received: {}, on port: {}'.format(rx, port))
time.sleep(6)
'''

while True:
    if uart1.any():
        data = uart1.readall()
        pycom.rgbled(0xFF0000) # set LED to RED on if data received
        print ('Data received from RPi')
        if data == b'send':
            s.send("data")
            pycom.rgbled(0x00FF00) # set LED to GREEN if data is b'send'
	    rx, port = s.recvfrom(256)
    	    if rx:
            	print('Received: {}, on port: {}'.format(rx, port))
	time.sleep(5)
