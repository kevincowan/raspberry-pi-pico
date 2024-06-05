# This program uses a Pi Pico W and a button to call a URL
# In this case it was a URL of an AWS Lambda
# The Lambda called the Voice Monkey API and made Alexa speak
# You can call any URL you want

import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine
import utime
import urequests

ssid = 'network_name'
password = 'password'

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)


def connect():
    #Connect to WLAN
    pico_led.on()  
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    pico_led.off()  
    return ip


def sendmessage():
    # Send message
    pico_led.off()    
    url = "https://your_url"
    
    while True:
        if button.value() == 1:
            pico_led.on()
            response = urequests.get(url)
            data1 = response.json()
            data2 = response.status_code
            print(data1)
            print(data2)
            utime.sleep(2)
            pico_led.off()


try:
    ip = connect()
    sendmessage()
except KeyboardInterrupt:
    machine.reset()
