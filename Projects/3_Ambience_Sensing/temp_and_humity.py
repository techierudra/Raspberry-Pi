import Adafruit_DHT  //sudo pip3 install Adafruit_DHT
import time

# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor = Adafruit_DHT.DHT11

# Set GPIO pin number
gpio_pin = 4

while True:

    # Get temperature and humidity from DHT11 sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio_pin)

    # Print values to console
    if humidity is not None and temperature is not None:
        print('Temperature = {0:0.1f}C  Humidity = {1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
    time.sleep(1)