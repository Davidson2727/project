from FileController import FileController

class DataController:
	
	def __init__(self):
		self.__fileController = FileController()
	
	def saveFile(self, data):
		self.__fileController.setDataState(data)
		self.__fileController.dataWrite()
		
	def openFile(self, fileName):
		self.__fileController.processDataFileName(fileName)
		return self.__fileController.getDataState()
