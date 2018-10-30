from pyo import *

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.last = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getLast(self):
        return self.last

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setLast(self, newLast):
        self.last = newLast
