from django.shortcuts import render
from django.http import HttpResponse
from veebileht.translate import *
from veebileht.models import Event
import datetime
from veebileht.background import run_scheduled
# Create your views here.

#req - resp 
#view function is a function that takes a request and returns a response
#its a request handler

def returnwebpage(request):

    #testMethod()
    #run_scheduled()
    #testRemoveMethod()

    #
    print('page was accessed')

    #get max three events with only their name and date
    allevents = getAllEventsDetails()

    days = ['Esmaspäeval', 'Teisipäeval', 'Kolmapäeval', 'Neljapäeval', 'Reedel', 'Laupäeval', 'Pühapäeval']

    ev1 = ''
    ev1data = ''
    ev2 = ''
    ev2data = ''
    ev3 = ''
    ev3data = ''

    filldata = {
        #site heading
        'heading' : 'IT Üritused',
        #quick glance events at the top of the webpage
        'ev1': ev1,
        'ev1data': ev1data,
        'ev2': ev2,
        'ev2data': ev2data,
        'ev3': ev3,
        'ev3data': ev3data,
        #main event list of ALL upcoming events
        'events' : allevents
        #
    }

    return render(request, 'index.html', filldata)
