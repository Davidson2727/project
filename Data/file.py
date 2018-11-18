from Data.dataObject import dataObj
from collections import OrderedDict
from Data.translator import translator
import datetime

class file(dataObj):
    def __init__(self):
        self.fileName = None
        self.createDate = None

    def __dir__(self):
        return ['fileName','createDate']

    def setFileName(self,_fileName):
        self.fileName = _fileName

    def getFileName(self):
        return self.fileName

    def setCreateDate(self):
        date = datetime.datetime.now()
        date = date.strftime('%m_%d_%Y_%H:%M:%S')
        self.createDate = date

    def getCreateDate(self):
        return self.createDate
    # maybe delete because this doesnt go to the database
    def create(self):
        return translator.createObject(self)

    def save(self):
        self.setCreateDate()
        self.setFileName('Synth_Save')
        saveObj = self
        proof = saveObj.buildDict(saveObj)
        del saveObj
        fileName = self.getFileName()+'_'+self.getCreateDate()+'.txt'
        f = open(fileName,"w+")
        for k,v in proof.items():
            f.write('%s %s\n'%(k,v))
        f.close()

    def load(self):
        f = open('file2.txt','r')
        r = f.readlines()
        for i in r:
            if i[0][0] == '#':
                print(i)


    def buildDict(self,_obj):
        # create an OrderedDict object
        myDict = OrderedDict()


        # for this object get its name, in this program is is either refTest, objTest or objTest2
        # add '#' to the front of it to identify it as a object
        # when reconstructing later.
        objNameType ='#'+_obj.__class__.__name__

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

            print('#########################################')
            print(_obj,i)
            print('#########################################')
            # get the value of the attribute
            v = getattr(_obj,i)
            # get the type of the attribute
            thisType = v.__class__.__name__
            # verify the attribute is not primitive
            primitive = not hasattr(v, '__dict__')
            if(type(v)==type([])):
                for j in range(len(v)):
                    v[j] = v[j].__class__.__name__
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
                print('########################################')
                print('call buildDict on obj',v)
                print('########################################')
                objDict = self.buildDict(v)
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                print(objDict)
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                # add '#' to the first attribute in the subObject dictionary
                myDict['#'+thisType] = objDict
                # iterate through the subObjects dictionary and add it to
                # this dictionary
                for key, value in objDict.items():
                    myDict[key] = value

                # return the dictionary to where is was called from

        return myDict
