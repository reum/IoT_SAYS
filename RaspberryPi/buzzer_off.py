#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys

# Turn off the buzzer.

BuzzerPin = 19 # Raspberry Pi Pin 17-GPIO 17

def setup():
	GPIO.setmode(GPIO.BCM) # Set GPIO Pin As Numbering
	GPIO.setup(BuzzerPin, GPIO.OUT)

if __name__ == '__main__': # Program start from here
        setup()
	GPIO.cleanup() # Release resource
