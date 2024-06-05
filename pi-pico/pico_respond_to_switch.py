# This makes the Pico W respond to pressing a switch
# Pressing the switch will toggle the LED on and off
# The button is connected to Pin 14
# The LED is connected to Pin 15 - use a resistor!

import machine
import utime

led_external = machine.Pin(15, machine.Pin.OUT)
button       = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        
        if led_external.value() == 0:
            led_external.value(1)
            utime.sleep(2)
        else:
            led_external.value(0)
            utime.sleep(2)
