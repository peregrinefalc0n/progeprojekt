
from veebileht.models import Event
from datetime import *

#This file contains methods for manipulating database to display
#data in the webpage, to "translate" data from db to webpage


#for reference:
#class Event(models.Model):
#    name = models.TextField()
#    starttime = models.IntegerField()
#    endtime = models.IntegerField(blank=True, null=True)
#    description = models.TextField(blank=True, null=True)
#    participants = models.IntegerField(blank=True, null=True)

#get a dict of all events in db
def getAllEventsDetails():
    e = Event.objects.all()
    ret = {}
    for obj in e:
        a = obj.__dict__
        ret[a['name']] = {}
        for key in a.keys():
            if key == "_state":
                continue
            if a[key] is not None:
                ret[a['name']][key] = a[key]
    return ret


#get the details of a single event by event name string
def getEventDetails(eventname):
    e = Event.objects.filter(name = eventname)[0].__dict__
    ret = {}
    for key in e.keys():
        if key == "_state":
            continue
        if e[key] is not None:
            ret[key] = e[key]
    return ret


#adds the new event to db
def addEvent(name, starttime, endtime = None, description = None, participants = None):
    if not Event.objects.filter(name = name).exists():
        event = Event(name = name, starttime = starttime, endtime = endtime, description = description, participants = participants)
        event.save()
    else:
        print("Event already exists.")


#deletes the specified event from db
def removeEvent(name):
    t = Event.objects.filter(name = name)
    t.delete()


#this method is currently temporarily used in views.py to display data for testing purposes
def testMethod():
    addEvent("Rooside sõda", 4500000)
    addEvent("Mälumäng", 56000000)
    addEvent("Arturi kallistamine", 90880008)