from collections import OrderedDict
from Data.sqlTranslator import *
from Data.buildDict import buildDict

class dataObject:

    def __init__(self):
        pass
    def create(self,schemaType):
        return sqlTranslator.insert(self,schemaType)
    def read(self,columns,conditions):
        return sqlTranslator.select(self,columns,conditions)
    def update(self):
        return sqlTranslator.update(self)
    def delete(self):
        return sqlTranslator.update(self)
    def checkLogin(self,columns,conditions):
        return sqlTranslator.login(self,columns,conditions)
