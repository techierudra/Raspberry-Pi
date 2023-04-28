#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bluetooth
import RPi.GPIO as GPIO
import time

led1 = 2
led2 = 3
led3 = 4
led1_status = 0
led2_status = 0
led3_status = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup((led1,led2,led3),GPIO.OUT)

def Blink(numTimes,speed):
        for i in range(0,numTimes):
                GPIO.output((led1,led2,led3),(1,1,1))
                print "Blinking " + str(i+1)
                time.sleep(speed)
                GPIO.output((led1,led2,led3),(0,0,0))
                time.sleep(speed)
        print ("Done Blinking LED")

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_sock.bind(("",port))
server_sock.listen(1)

client_sock,address = server_sock.accept()
print "Accepted connection from ",address
while True:

 data = client_sock.recv(1024)
 print "received [%s]" % data
 if (data == "1"):
        led1_status = ~led1_status
        GPIO.output(led1,led1_status)
        if led1_status:
                print ("LED1 ON")
        else:
                print ("LED1 OFF")
 if (data == "2"):
        led2_status = ~led2_status
        GPIO.output(led2,led2_status)
        if led2_status:
                print ("LED2 ON")
        else:
                print ("LED2 OFF")
 if (data == "3"):
        led3_status = ~led3_status
        GPIO.output(led3,led3_status)
        if led3_status:
                print ("LED3 ON")
        else:
                print ("LED3 OFF")

 if (data == "5"):
        print ("LED Blink")
        Blink(10,0.1)
 if (data == "e"):
        print ("Exit")
        break

client_sock.close()
server_sock.close()