from dataObject import dataObj
from collections import OrderedDict
from translator import translator
from makeDate import makeDate
from setType import readType, writeType
from buildDict import buildDict
from buildObj import buildObject

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
        self.createDate = makeDate()

    def getCreateDate(self):
        return self.createDate
    # maybe delete because this doesnt go to the database
    def create(self):
        return translator.createObject(self)

    def save(self):
        self.setCreateDate()
        self.setFileName('Synth_Save')
        proof = buildDict(self)
        fileName = self.getFileName()+'_'+self.getCreateDate()+'.txt'
        f = open(fileName,"w+")
        for k,v in proof.items():
            vType = writeType(v)
            f.write('~%s~%s~%s\n'%(k,v,vType))
        f.close()

    def load(self,_path):
            lines = [line.rstrip('\n') for line in open('file2.txt')]
            for i in lines:
                keyValue = i.split('~')
                if keyValue[1][0] == '#':
                    print('\n\n\n############################')
                    print('buildObject')
                    buildObject(keyValue[1],keyValue[2],keyValue[3])
                    print('############################')
                if hasattr(self,keyValue[1]):
                    keyValue[2] = readType(keyValue[2],keyValue[3])
                    setattr(self,keyValue[1],keyValue[2])
                else:

                    print('no attr by that name',keyValue[1])
