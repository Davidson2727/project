from Data.dataObject import dataObject
from collections import OrderedDict
from Data.makeDate import makeDate
from Data.setType import readType, writeType
from Data.buildDict import buildDict
from Data.buildObj import buildObject
from Util import Config

class file(dataObject):
    def __init__(self):
        self._userId = None
        self._userName = None
        self._fileName = None
        self._createDate = None
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

    def save(self,saveCommand):
        self.setCreateDate()
        self.setFileName('Synth_Save2')
        self._contents = 'empty'
        self._type = 'empty'
        self._userName = 'empty'
        self._userId = 'empty'
        if Config.sysUser.getUserName()==None:
            self._userName = 'empty'
            self._userId = 'empty'
        else:
            self._userName = Config.sysUser.getUserName()
            self._userId = Config.sysUser.getUserId()
        self._activeStatus = '1'
        proof = buildDict(self)
        fileName = self.getFileName()+'_'+self.getCreateDate()+'.txt'
        f = open(fileName,"w+")
        for k,v in proof.items():
            vType = writeType(v)
            f.write('~%s~%s~%s\n'%(k,v,vType))
        f.read()
        f.close()
        file = open(fileName)
        contentsString = ""
        self._contents = file.read()
        file.close()
        if saveCommand == 3:
            if Config.sysUser.getUserName()==None:
                return 'error'
            else:
                self._userName = Config.sysUser.getUserName()
                self._userId = Config.sysUser.getUserId()
                self.create('fileSchema')

    def load(self,fileName):
            fileNameTxT += fileName+'.txt'
            lines = [line.rstrip('\n') for line in open(fileNameTxT)]
            for i in lines:
                keyValue = i.split('~')
                if keyValue[1][0] == '#':
                    buildObject(keyValue[1],keyValue[2],keyValue[3])
                if hasattr(self,keyValue[1]):

                    keyValue[2] = readType(keyValue[2],keyValue[3])
                    setattr(self,keyValue[1],keyValue[2])
