from collections import OrderedDict
from Data.translator import *
from Data.buildDict import buildDict

class dataObject:

    def __init__(self):
        pass
    def create(self,schemaType):
        return translator.insert(self,schemaType)
