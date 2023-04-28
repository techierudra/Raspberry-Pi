import sys
from time import sleep
import urllib2

thingtweet_api_key = '5GJDTK0NW80KWZCI'
status = 'I am Tweeting from My Raspberry Pi Device'

# main() function
def main():
    print 'starting...'

    baseURL = 'https://api.thingspeak.com/apps/thingtweet/1/statuses/update?api$
    f = urllib2.urlopen(baseURL)
    print 'Tweeting on your behalf\n Your Status is %s' % status
    print f.read()
    f.close()
    print 'exiting.'
    exit()

# call main
if __name__ == '__main__':
    main()






