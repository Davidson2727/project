from Data.dataObject import dataObject
from collections import OrderedDict
from Data.makeDate import makeDate
from Data.setType import readType, writeType
from Data.buildDict import buildDict
from Data.buildObj import buildObject
from Util import Config
from Util.EnumData import Bools, Nums
import os

class file(dataObject):
    def __init__(self):
        self._userId = None
        self._userName = None
        self._fileName = None
        self._createDate = makeDate()
        self._type = None
        self._contents= None
        self._activeStatus = None

    def __dir__(self):
        return ['_fileName','_createDate','_contents','_userName','_type','_activeStatus','_userId']

    def setFileName(self,_fileName):
        self._fileName = _fileName

    def getFileName(self):
        return self._fileName

    def setCreateDate(self):
        self._createDate = makeDate()

    def getCreateDate(self):
        return self._createDate

    def save(self,_input):
        self.setFileName(_input[2])
        self._activeStatus = '1'
        proof = buildDict(self)
        #fileName = self.getFileName()+'_'+self.getCreateDate()+'.txt'

        path = _input[1]
        f = open(path,"w+")
        for k,v in proof.items():
            vType = writeType(v)
            f.write('~%s~%s~%s\n'%(k,v,vType))
        f.read()
        f.close()
        print('before cloud save')
        print(_input[0])
        if _input[0]!=Nums.SAVE.value:
            file = open(path)
            contentsString = ""
            self._contents = file.read()
            file.close()
            os.remove(path)
            self._userName = Config.sysUser.getUserName()
            self._userId = Config.sysUser.getUserId()
            self._type = self.__class__.__name__
            print('$$$$$$$$$$$$$$$$$$$$$')
            self.create('fileSchema')

    def load(self,path):
            lines = [line.rstrip('\n') for line in open(path)]
            for i in lines:
                keyValue = i.split('~')
                if keyValue[1][0] == '#':
                    buildObject(keyValue[1],keyValue[2],keyValue[3])
                if hasattr(self,keyValue[1]):
                    keyValue[2] = readType(keyValue[2],keyValue[3])
                    setattr(self,keyValue[1],keyValue[2])
