
import math


def readType(_value,_type):
    if _type == 'int':
        return int(_value)
    elif _type == 'float':
        return float(_value)
    elif _type == 'bool':
        if _value == 'True':
            return True
        else:
            return False
    elif _type == 'list':
        value = _value.strip("[]")
        value = value.split(',')
        for i in range(len(value)):
            value[i] = value[i].strip()
            value[i] = value[i].strip("'")
        z=0
        listLength = math.ceil(len(value)/2)
        returnList = []
        while z <= listLength:
            returnList.append(readType(value[z],value[z+1]))
            z+=2


        return returnList
    elif _type == 'None':
        return None
    else:
        return _value


def writeType(_value):
    value = _value
    thisType = str(type(value)).split()
    thisType[1] = thisType[1].replace('>','')
    thisType =thisType[1].split()
    thisType =thisType[0].split('.')
    thisType = thisType[-1].replace("'",'')
    thisType = '"'+thisType+'"'

    return thisType
