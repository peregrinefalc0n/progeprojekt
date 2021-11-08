
import classes
import vars
import copy

#db access methods

#create/add
#read
#update
#delete

def addEntry(datafile, entry):
    with open(datafile, 'a', encoding='UTF-8') as db:
        db.write(entry)

#find entry with given name
def readEntry(datafile, entryname):
   with open(datafile, 'a', encoding='UTF-8') as db:
       for line in db:
           linedata = eval(line.strip())
           if linedata
    
def readAllEntry(datafile):
    templist = []
    with open(datafile, "r", encoding="UTF-8") as db:
        for line in db:
            templist.append(eval(line.strip()))

    ret = classes.EventDataList(vars.getNewID())
    ret.datalist = copy.deepcopy(templist)

    return ret

def updateEntry(entry):
    pass

def deleteEntry(entry):
    pass
