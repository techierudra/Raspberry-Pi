import sys
import RPi.GPIO as GPIO
from time import sleep
import Adafruit_DHT
import urllib2

def getSensorData():
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 14)
    # return dict
    return (str(RH), str(T))

# main() function
def main():
    # use sys.argv if needed
    if len(sys.argv) < 2:
        print('Usage: python anvesh_dht.py ZDFBTTVUUPV9WTWX')
        exit(0)
    print 'starting...'

    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % sys.argv[1]

    while True:
        try:
            RH, T = getSensorData()
            print 'Temp:  %s C  Humidity: %s percent' % (T,RH)
            f = urllib2.urlopen(baseURL +
                                "&field2=%s&field1=%s" % (RH, T))
            print f.read()
            f.close()
            sleep(15)
        except:
            print 'exiting.'
            break

# call main
if __name__ == '__main__':
    main()