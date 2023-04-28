import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)

# Define the pins for each segment of the display
segments = (14, 15, 18, 23, 24, 25, 8)

# Define the pins for the common cathode and the button
cathode = 7
button = 4

# Set up the GPIO pins as outputs and inputs
GPIO.setup(segments, GPIO.OUT)
GPIO.setup(cathode, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
    9: (1, 1, 1, 1, 0, 1, 1)}

# Define a variable to hold the current number
number = 0

# Function to update the display with the current number
def update_display():
    global number
    for pin in range(0, 7):
        GPIO.output(segments[pin], numbers[number][pin])
    GPIO.output(cathode, 0)

# Update the display with the starting number
update_display()

# Main loop to detect button presses and update the display
while True:
    # Detect a button press
    input_state = GPIO.input(button)
    if input_state == False:
        # Increase the number by 1 and wrap around to 0 if the number is 9
        number = (number + 1) % 10
        # Update the display with the new number
        update_display()
        # Wait for a short time to debounce the button
        time.sleep(0.2)

# Clean up the GPIO pins
GPIO.cleanup()
