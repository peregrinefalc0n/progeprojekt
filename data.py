
#A full version of the event class
class MITSEventFull:
    def __init__(self, name, startdate, starttime, enddate, endtime, participants, description):
       
        #Name of the event, always exists
        self.name = name
        #Starting date of the event, always exists
        self.startdate = startdate
        #Starting time of the event, always exists
        self.starttime = starttime
        #End date of event, can be nonexistent
        self.enddate = enddate
        #End time of event, can be nonexistent
        self.endtime = endtime
        #Number of participants currently taking part
        self.participants = participants
        #The description of the event
        self.description = description

    def toDictionary(self):
        return dict({'name': self.name,
                    'startdate': self.startdate,
                    'starttime': self.starttime,
                    'enddate': self.enddate,
                    'endtime': self.endtime,
                    'participants': self.participants,
                    'description': self.description})

#Simple version of the event with only name, date and time
class MITSEventSimple:
    def __init__(self, name, startdate, starttime):

        #Name of the event, always exists
        self.name = name
        #Starting date of the event, always exists
        self.startdate = startdate
        #Starting time of the event, always exists
        self.starttime = starttime

    def toDictionary(self):
        return dict({'name': self.name, 'startdate': self.startdate, 'starttime': self.starttime})

class EventDataList:
    def __init__(self, id):
        self.id = id
        self.datalist = []

    def addEvent(self, event):
        self.datalist.append(event)

    def removeEvent(self, event):
        self.datalist.remove(event)

    def toString(self):
        s = f'id: {self.id}, '
        for i in self.datalist:
            s += str(i.toDictionary()) + ', '
        return s

    def getLastEvent(self):
        return self.datalist.pop()
    
    def getEventByName(self, name):
        for i in self.datalist:
            if(i.name == name):
                return i