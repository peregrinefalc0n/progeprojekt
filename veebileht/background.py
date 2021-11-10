from background_task import background
from veebileht import scraper
from veebileht.translate import addEvent
from veebileht import classes
import time

@background(schedule=60)
def run_scheduled():
    time.sleep(1)
    print('Running scheduled scrape')
    datamatrix = scraper.scrape_page()
    
    #TODO proper data read-in from datamatrix
    for i in len(datamatrix[2]):
        addEvent(datamatrix[0][i], datamatrix[1][i])

