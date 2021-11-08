
variables = {'id': 0}

def getNewID():
    variables["id"] += 1
    id = int(variables["id"])
    return id

def getCurrentID():
    return variables['id']