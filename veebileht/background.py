from background_task import background
from veebileht import scraper
from veebileht.translate import addEvent
from veebileht import classes
import time

@background(schedule=60)
def run_scheduled():

    for i in range(60,0, -1):
        print(i, 'seconds until scrape')
        time.sleep(1)

    print('Running scheduled scrape')
    datamatrix = scraper.scrape_page()
    
    #TODO proper data read-in from datamatrix
    print(datamatrix)
