class DataPath:
	def __init__(self):
		self.__fileState = []
	def flush(self, data):
		file = open("data.txt", 'w')
		for i in data:
			file.write(str(i) + "\n")
	
	def open(self, string = 'data.txt'):
		file = open(string, 'r')
		for i in file:
			self.__fileState.append(i.rstrip('\n'))
	
	def getFileState(self):
		return self.__fileState
		
			