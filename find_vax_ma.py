# Copyright Michelle Daniels 2021
# This is a simple script that will alert the user while COVID vaccine appointments are available at one of the specified sites.
# This only works for Massachusetts and the format of vaxfinder.mass.gov webpages as of 2/18/2021.

from bs4 import BeautifulSoup
from datetime import datetime
from playsound import playsound
from pprint import pprint
import requests 
import time as time

# add or replace URLs for the sites you care about. this only works with URLs that start with vaxfinder.mass.gov
URLS = {'natick': 'https://vaxfinder.mass.gov/locations/natick-natick-mall/',
        'gillette': 'https://vaxfinder.mass.gov/locations/gillette-stadium/',
        'fenway': 'https://vaxfinder.mass.gov/locations/fenway-park/'}
# increase this if you only want notifications when a larger block of appointments is available
MIN_AVAILABLE = 1
# This is a Windows 10 system sound. Change it to whatever you want.
ALARM_FILE = 'C:\Windows\Media\Alarm01.wav'
# this controls how long the script sleeps before iterating through the sites again
SLEEP_INTERVAL_SECONDS = 5


def getdata(url): 
    r = requests.get(url) 
    return r.text

def availability(url):
    htmldata = getdata(url) 
    soup = BeautifulSoup(htmldata, 'html.parser') 
    # look for the table of available slots
    res = soup.find_all('td')
    total_available = 0
    # the number of available slots for each date is the third column of the table
    if len(res) >= 3:
        for item in res[2::3]:
            num_available = int(item.text)
            total_available += num_available

    return total_available

def main():
    print('Running with URLs:')
    pprint(URLS)

    num_attempts = 0
    while True:
        for location, url in URLS.items():
            num_available = availability(url)
            if num_available >= MIN_AVAILABLE :
                print('\n{} - Total availability at {}: {} {}'.format(datetime.now().strftime("%m/%d/%Y - %H:%M:%S"), location, availability(url), url))
                playsound(ALARM_FILE)
        num_attempts += 1
        print('attempts: {}'.format(num_attempts), end='\r')
        time.sleep(SLEEP_INTERVAL_SECONDS)

if __name__ == '__main__':
    main()
