
#!!!
#Because we are using the models.py, these are currently unused 

# A full version of the event class
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



#Simple version of the event with only name, date and time
class MITSEventSimple:
    def __init__(self, name, time):

        #Name of the event, always exists
        self.name = name
        #Starting date of the event, always exists
        self.time = time



#Simple EventList class
class EventDataList:
    def __init__(self, id):
        self.id = id
        self.datalist = []