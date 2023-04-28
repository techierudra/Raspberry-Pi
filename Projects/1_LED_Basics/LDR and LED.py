from gpiozero import LED, LightSensor
from time import sleep

# Define the GPIO pin for the LED
led = LED(14)

# Define the GPIO pin for the LDR
ldr = LightSensor(18)

while True:
    # Read the value of the LDR (between 0 and 1)
    ldr_value = ldr.value

    # Turn the LED on or off based on the LDR value
    if ldr_value < 0.5:
        led.on()
    else:
        led.off()

    # Wait a short time before reading the LDR again
    sleep(0.1)
