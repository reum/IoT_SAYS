#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys

BuzzerPin = 19 # Raspberry Pi Pin 17-GPIO 17

def setup():
	GPIO.setmode(GPIO.BCM) # Set GPIO Pin As Numbering
	GPIO.setup(BuzzerPin, GPIO.OUT)
	#GPIO.output(BuzzerPin, GPIO.HIGH)

def on():
	GPIO.output(BuzzerPin, GPIO.LOW)
	#GPIO.output(BuzzerPin, True)

def off():
	GPIO.output(BuzzerPin, GPIO.HIGH)
	#GPIO.output(BuzzerPin, False)

def beep(Delay):
        time.sleep(Delay)
	GPIO.cleanup() # Release resource
        time.sleep(Delay)
        
if __name__ == '__main__': # Program start from here
        if len(sys.argv) != 2:
            exit()

        delay = sys.argv[1]
        delay = float(delay)
    
        setup()
	try:
		beep(delay);
	except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
		destroy()
