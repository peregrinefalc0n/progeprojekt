from django.shortcuts import render
from django.http import HttpResponse
from veebileht.translate import *
from veebileht.models import Event
import datetime
# Create your views here.

#req - resp 
#view function is a function that takes a request and returns a response
#its a request handler

def returnwebpage(request):

    #get max three events with only their name and date
    allevents = getAllEventsDetails()



    threeevents = []
    n=0
    for i in allevents:
        if n >= 3:
            break
        else:
            date = datetime.datetime.fromtimestamp(allevents[i]['starttime'])
            s = f"Üritus {allevents[i]['name']} toimub {date} "
            threeevents.append(s)
        n += 1

    ev1 = ''
    ev2 = ''
    ev3 = ''

    l = len(threeevents)
    if(l == 1):
        ev1 = threeevents[0]
    elif(l == 2):
        ev1 = threeevents[0]
        ev2 = threeevents[1]
    else:
        ev1 = threeevents[0]
        ev2 = threeevents[1]
        ev3 = threeevents[2]    

    filldata = {
        #site heading
        'heading' : 'IT Üritused',
        #quick glance events at the top of the webpage
        'ev1': ev1,
        'ev2': ev2,
        'ev3': ev3,
        #main event list of ALL upcoming events
        'events' : allevents
        #
    }

    return render(request, 'index.html', filldata)
