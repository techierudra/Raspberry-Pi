import RPi.GPIO as GPIO
import time

led = 14

def blink(pin):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(0.5)
        return

GPIO.setmode(GPIO.BCM)

GPIO.setup(led, GPIO.OUT)

for i in range(0,10):
        blink(led)
GPIO.cleanup()
