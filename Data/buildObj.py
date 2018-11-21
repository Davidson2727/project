from Data.setType import readType

def buildObject(_objName,_objValues,_type):
    # remove '#' from the start of the string
    objName = _objName[1:]
    # take the saved list, give it type list and save all its values to it
    objValues = readType(_objValues,_type)
    # empyy list
    typeList = []
    i=0
    while i<= len(objValues)/3:
        typeList.append(readType(objValues[i],objValues[i+1]))
        i = i+3
    return objName
