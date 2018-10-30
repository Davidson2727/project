from pyo import *
from ToList.Node import Node

class LinkedList:

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

    def isEmpty(self):
        return self.head == None

    def addHead(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        temp.setLast(None)
        self.head = temp

    def addTail(self,item):
        temp = Node(item)
        if self.head is None:
            self.head = self.tail = temp
        else:
            self.tail.setNext = temp
        self.tail = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
