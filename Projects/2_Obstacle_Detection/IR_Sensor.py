import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
  if GPIO.input(4):
    print ("Obstacle not Found")
    time.sleep(0.5)
  else:
        print("Obstacle Found")
        time.sleep(0.5)