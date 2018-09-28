import os
class DataPath:
	def __init__(self):
		self.__dataState = []
		self.__fileName = ""
	def getDataState(self):
		return self.__dataState
		
	def processDataFileName(self, fileName):
		print("here")
		if os.path.isfile(fileName):
			file = open(fileName, 'r')
			self.dataOpen(file)
			self.__fileName = fileName
			file.close()
			return True
		else:
			file = open(fileName,'w')
		self.__fileName = fileName
		file.close()
		print(self.__fileName + "process")
		return False
	
	def dataOpen(self, file):
		for i in file:
			self.__dataState.append(i.rstrip('\n'))
		
	def dataWrite(self, data):
		print(self.__fileName + "datawrite")
		file = open(self.__fileName, 'w')
		for i in data:
			file.write(str(i) + "\n")
		file.close()
	
	
	
		
			