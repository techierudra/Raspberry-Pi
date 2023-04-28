from gpiozero import Button, LEDBoard
from time import sleep
import random

# Define the GPIO pins for the 7-segment display
segments = LEDBoard(2, 3, 4, 5, 6, 7, 8, 9)

# Define the GPIO pin for the button
button = Button(17)

while True:
    if button.is_pressed:
        # Generate a random number between 0 and 9
        number = random.randint(0, 9)

        # Convert the number to a list of boolean values for each segment
        pattern = [
            number in [0, 2, 3, 5, 6, 7, 8, 9],  # A
            number in [0, 1, 2, 3, 4, 7, 8, 9],  # B
            number in [0, 1, 3, 4, 5, 6, 7, 8, 9],  # C
            number in [0, 2, 3, 5, 6, 8, 9],  # D
            number in [0, 2, 6, 8],  # E
            number in [0, 4, 5, 6, 8, 9],  # F
            number in [2, 3, 4, 5, 6, 8, 9],  # G
            number == 0,  # DP
        ]

        # Turn on the segments for the chosen number
        segments.value = pattern

    # Wait a short time before checking the button again
    sleep(0.1)
