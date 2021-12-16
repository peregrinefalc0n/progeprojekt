from django.shortcuts import render
from django.http import HttpResponse
from veebileht.translate import *
from veebileht.models import Event
import datetime
from veebileht.background import run_scheduled
from veebileht.constants import *
# Create your views here.

#req - resp 
#view function is a function that takes a request and returns a response
#its a request handler

import threading

t = threading.Thread(target=run_scheduled)
t.setDaemon(True)
t.start()

def returnwebpage(request):

    #testMethod()
    #run_scheduled()
    #testRemoveMethod()

    #
    print('page was accessed')

    allevents = getAllEventsDetails()


    filldata = {
        #site heading
        'heading' : 'IT Üritused',
        #quick glance events at the top of the webpage
        'ev1name': allevents[0]['name'],
        'ev1place': allevents[0]['place'],
        'ev1time': allevents[0]['time'],

        'ev2name': allevents[1]['name'],
        'ev2place': allevents[1]['place'],
        'ev2time': allevents[1]['time'],

        'ev3name': allevents[2]['name'],
        'ev3place': allevents[2]['place'],
        'ev3time': allevents[2]['time'],
        
        #main event list of ALL upcoming events
        'events' : allevents
        #
    }

    return render(request, 'index.html', filldata)
