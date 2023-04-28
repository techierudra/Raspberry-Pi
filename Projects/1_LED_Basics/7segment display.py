import RPi.GPIO as GPIO
import time

# Define the pins for each segment of the display
segments = (14, 15, 18, 23, 24, 25, 8)

# Define the pins for the common cathode
cathode = 7

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(segments, GPIO.OUT)
GPIO.setup(cathode, GPIO.OUT)

# Define the segments needed for each number
numbers = {
    0: (1, 1, 1, 1, 1, 1, 0),
    1: (0, 1, 1, 0, 0, 0, 0),
    2: (1, 1, 0, 1, 1, 0, 1),
    3: (1, 1, 1, 1, 0, 0, 1),
    4: (0, 1, 1, 0, 0, 1, 1),
    5: (1, 0, 1, 1, 0, 1, 1),
    6: (1, 0, 1, 1, 1, 1, 1),
    7: (1, 1, 1, 0, 0, 0, 0),
    8: (1, 1, 1, 1, 1, 1, 1),
    9: (1, 1, 1, 1, 0, 1, 1)
}


# Define a function to display a number on the 7-segment display
def display_number(number):
    # Turn off all segments
    GPIO.output(segments, 0)

    # Turn on the segments for the given number
    for pin in range(0, 7):
        GPIO.output(segments[pin], numbers[number][pin])

    # Turn on the common cathode to display the number
    GPIO.output(cathode, 0)

    # Wait for a short time
    time.sleep(1)

    # Turn off the segments and the common cathode
    GPIO.output(segments, 0)
    GPIO.output(cathode, 1)


# Display the numbers 0 to 9 in order
for i in range(0, 10):
    display_number(i)

# Clean up the GPIO pins
GPIO.cleanup()

