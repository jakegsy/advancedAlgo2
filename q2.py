

input = [("x0","x1",4),("x0","x4",2),("x1","x2",4),("x1","x3",3),
         ("x2","x5",3),("x3","x2",1),("x3","x5",1),("x4","x3",1),("x4","x5",3)]

def parseInput(inputs):
    returnDict = {}
    notSource = []
    notDestin = []
    allKeys = []
    for (frm,to,cap) in inputs:
        if(not returnDict.has_key(frm)):
            returnDict[frm] = {'out':[],'in':[]}
        if(not returnDict.has_key(to)):
            returnDict[to] = {'out':[],'in':[]}
        returnDict[frm]['out'].append((to,cap))
        returnDict[to]['in'].append((frm,cap))
        notSource.append(to)
        notDestin.append(frm)
        allKeys.append(to)
        allKeys.append(frm)

    notSource = list(set(notSource))
    notDestin = list(set(notDestin))
    allKeys = list(set(allKeys))

    for keys in returnDict.keys():
        if keys not in notSource:
            returnDict["s"] = keys

    for thing in allKeys:
        if thing not in notDestin:
            returnDict["t"] = thing

    return returnDict


dict = parseInput(input)


print dict
def exists(name,table):
    for (ele,val) in table:
        if (ele == name):
            return True
    return False

def indexing(dict):
    returnTable = []
    for keys in dict.keys():
        if (keys=='s' or keys=='t'):
            continue
        curr = dict[keys]
        for (element,val) in curr['out']:
            name = keys+element
            if(not exists(name,returnTable)):
                returnTable.append((name,val))
        for (element,val) in curr['in']:
            name = element+keys
            if (not exists(name, returnTable)):
                returnTable.append((name,val))
    numEdges = len(returnTable)
    numVert = len(dict.keys()) - 4
    returnTable = returnTable + [0]*(numEdges+numVert)

    return returnTable

table = indexing(dict)


print table[8]