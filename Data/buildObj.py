from setType import readType

def buildObject(_objName,_objValues,_type):
    # remove '#' from the start of the string
    objName = _objName[1:]
    # take the saved list, give it type list and save all its values to it
    objValues = readType(_objValues,_type)
    # empyy list
    typeList = []
    i=0
    print('in buildObj objValues',objValues)
    print('in buildObj len of objValues,',len(objValues))
    while i<= len(objValues)/2:
        print('in buildObj while i value',i)
        typeList.append(objValues[i+1])
        typeList.append(objValues[i+2])
        #objAttrType = readType(objValues[i+1],objValues[i+2])
        i = i+3
    readTL = []
    i=0
    while i <= len(typeList)/2:
        readTL.append(readType(typeList[i],typeList[i+1]))
        i+=2
