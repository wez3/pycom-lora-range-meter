import time
import pycom
import binascii
import socket
import sys
from network import LoRa

# Disable heartbeat LED and do startup round
pycom.heartbeat(False)

pycom.rgbled(0x140000) # Red
time.sleep(1)
pycom.rgbled(0x001400) # Green
time.sleep(1)
pycom.rgbled(0x000014) # Blue

while True:
    # Initialize LoRa in LORAWAN mode.
    lora = LoRa(mode=LoRa.LORAWAN)

    # create an OTAA authentication parameters
    app_eui = binascii.unhexlify('')
    app_key = binascii.unhexlify('')

    print("DevEUI: %s" % (binascii.hexlify(lora.mac())))
    print("AppEUI: %s" % (binascii.hexlify(app_eui)))
    print("AppKey: %s" % (binascii.hexlify(app_key)))

    # join a network using OTAA (Over the Air Activation)
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

    # wait until the module has joined the network
    while not lora.has_joined():
        pycom.rgbled(0x140000) # Red
        time.sleep(0.5)
        print('Not yet joined...')

    print('OTAA joined')
    pycom.rgbled(0x001400) # Green

    # create a LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    # set the LoRaWAN data rate
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    print('Sending data (uplink)...')
    s.send('Here I am')


    s.setblocking(False)
    data = s.recv(64)
    print('Received data (downlink)', data)
    time.sleep(60)
