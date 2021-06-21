""" environment variables """
from machine import Pin, Signal
from micropython import const
from collections import namedtuple
Network = namedtuple("Network", ["ssid", "password"])
wifi = Network('IoT', 'ItsoutThere')
# blue or green led on pin 5
led = Signal(Pin(5, Pin.OUT), invert=True)
