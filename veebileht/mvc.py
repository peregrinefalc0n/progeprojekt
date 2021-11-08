
import classes
import vars
import copy

#db access methods

#create/add
#read
#update
#delete

def addEntry(datafile, entry):
    try:
        with open(datafile, 'a', encoding='UTF-8') as db:
            db.write(str(entry) + '\n')
    except Exception as e:
        print(e)


#find entry with the exact name, if not found, returns False
def readEntry(datafile, entryname):
    try:
        with open(datafile, 'r', encoding='UTF-8') as db:
            for line in db:
                if line == '\n':
                    break
                else:
                    linedata = eval(line.strip())
                    if linedata['eventname'] == entryname:
                        return linedata
                    else:
                        return False
    except Exception as e:
        print(e)

def readAllEntry(datafile):
    
    try:
        templist = []
        with open(datafile, "r", encoding="UTF-8") as db:
            for line in db:
                if line == '\n':
                    break
                else:
                    templist.append(eval(line.strip()))

        ret = classes.EventDataList(vars.getNewID())
        ret.datalist = copy.deepcopy(templist)

        return ret
    except Exception as e:
        print(e)



def updateEntry(entry):
    
    try:
        pass
    except Exception as e:
        print(e)



def deleteEntry(entry):
    
    try:
        pass
    except Exception as e:
        print(e)
