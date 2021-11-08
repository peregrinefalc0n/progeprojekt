
from veebileht.models import Event

#This file contains methods for manipulating database to display
#data in the webpage, to "translate" data from db to webpage


#for reference:
#class Event(models.Model):
#    name = models.TextField()
#    starttime = models.IntegerField()
#    endtime = models.IntegerField(blank=True, null=True)
#    description = models.TextField(blank=True, null=True)
#    participants = models.IntegerField(blank=True, null=True)


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



def getEventDetails(eventname):
    e = Event.objects.filter(name = eventname)[0].__dict__
    ret = {}
    for key in e.keys():
        if key == "_state":
            continue
        if e[key] is not None:
            ret[key] = e[key]
    return ret



def addEvent(name, starttime, endtime = None, description = None, participants = None):
    if not Event.objects.filter(name = name).exists():
        event = Event(name = name, starttime = starttime, endtime = endtime, description = description, participants = participants)
        event.save()
    else:
        print("Event already exists.")



def removeEvent(name):
    t = Event.objects.filter(name = name)
    t.delete()


#this method is currently temporarily used in views.py to display data
def execute():
    addEvent("lol", 1, 2)
    addEvent("lmao", 10000)

    return getAllEventsDetails()