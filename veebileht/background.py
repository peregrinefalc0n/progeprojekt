#from background_task import background
from veebileht import scraper
from veebileht.models import Event
from veebileht.translate import addEvent, getEventDetails
from veebileht import classes
import time
from random import randint
import veebileht.constants

#@background(schedule=10)
def run_scheduled():

    #sleep to delay scrape, can be overridden in veebileht/constants.py
    delay = veebileht.constants.timings['delay']
    print("Delay is", delay)
    if delay == 0:
        time.sleep(randint(60, 120) * 60)
    else:
        time.sleep(delay)
    
    #first: run scrape
    print('Running scheduled scrape')
    datamatrix = scraper.run()

    #delay to make sure scrape was successful
    print("Waiting 5 seconds fo scraper to finish")
    time.sleep(5)

    #second: save scraped data to database
    print("All data: ", datamatrix)

    print("Add events one by one")
    for page in datamatrix:
        for event in page:
            addEvent(event['Event_Name'], event['Event_Time'], event['Event_Place'])
            print("Added event:" + getEventDetails(event["Event_Name"]))
    print("----------------Events added!----------------")

