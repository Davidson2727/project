from collections import OrderedDict
from Data.setType import writeType
def buildDict(_obj):
    # create an OrderedDict object
    myDict = OrderedDict()
    # for this object get its name, in this program is is either refTest, objTest or objTest2
    # add '#' to the front of it to identify it as a object
    # when reconstructing later.
    #objNameType ='#'+_obj.__class__.__name__
    objNameType =_obj.__class__.__name__

    # add the object name as key and 'Value' as value to the dictionary
    myDict[objNameType] = _obj.__class__.__name__
    ########################################
    # Look in the definition of each class.
    # there is a method called __dir__ that
    # only returns a list of all the class
    # attributes for that class then iterate
    # over all attributes of that object
    ########################################
    for i in dir(_obj):
        attrName = i
        # get the value of the attribute
        v = getattr(_obj,i)
        # get the type of the attribute
        thisType = v.__class__.__name__
        # verify the attribute is not primitive
        primitive = not hasattr(v, '__dict__')
        # if v is a list
        if(type(v)==type([])):
            # iterate through the list
            newList = []
            for j in range(len(v)):
                newList.append(v[j])
                newList.append(writeType(v[j]))
            myDict[i] = newList
        # if the value is primitive add this to the dictionary
        elif primitive == True:
            myDict[i] = v
            ########################################
            # if the value is NOT primitive call
            # getInfo(v). this else statement will
            # only activate if the the attribute
            # being examined is another object
            ########################################
        else:
            ########################################
            # call getInfo method again if the value
            # being evaluated is an object
            ########################################
            objDict = buildDict(v)
            # add '#' to the first attribute in the subObject dictionary
            objList = []
            for key,value in objDict.items():
                objList.append(key)
                objList.append(value)
                objList.append(writeType(value))
            myDict['#'+attrName] = objList
            # iterate through the subObjects dictionary and add it to
            # this dictionary
            #for attribute, value in objDict.items():
                #myDict[key] = value
            # return the dictionary to where is was called from
    return myDict
