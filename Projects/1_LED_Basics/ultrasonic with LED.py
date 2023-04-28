from gpiozero import LED
import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the LED and ultrasonic sensor
led = LED(14)
GPIO_TRIGGER = 23
GPIO_ECHO = 24

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # Set the trigger to high
    GPIO.output(GPIO_TRIGGER, True)

    # Wait for a short time and then set the trigger to low
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    # Wait for the echo pin to go high and then start a timer
    start_time = time.time()
    while GPIO.input(GPIO_ECHO)==0:
        start_time = time.time()

    # Wait for the echo pin to go low and then stop the timer
    stop_time = time.time()
    while GPIO.input(GPIO_ECHO)==1:
        stop_time = time.time()

    # Calculate the time difference and convert to distance in centimeters
    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2

    return distance

while True:
    # Read the distance measured by the ultrasonic sensor
    dist = distance()

    # Turn the LED on or off based on the distance
    if dist < 20:
        led.on()
    else:
        led.off()

    # Wait a short time before measuring the distance again
    time.sleep(0.1)
