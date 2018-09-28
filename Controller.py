from Synth import Synth 
from DataPath import DataPath
class Controller:
	def __init__(self):
		self.__synth = Synth()
		#self.__PureDataConnector()
		self.__dataPath = DataPath()
	
	def receiver(self, data):
		if data[0] == 'o':
			self.__newDataSession(data[1:])
			print("data[1:] " + data[1:])
		if data[0] == 'f' or data[0] == 'v':
			self.__setSynthState(data)
			#self.__setPureDataConnectorState(data)
		if data[0] == 'w':
			self.__toDataPath()
		
	def __newDataSession(self, data):
		print("new session " + data)
		if self.__dataPath.processDataFileName(data):
			self.__fromDataPath()
			#can return stuff
	
	def __fromDataPath(self):
		dataState = self.__dataPath.getDataState()
		for i in dataState:
			self.receiver(i)
	
	def __toDataPath(self):
		self.__dataPath.dataWrite(self.__getSynthState())
	
	def __setSynthState(self,data):	
		if data[0] == 'f':
			self.__synth.setFrequency(int(data[1:]))
		if data[0] == 'v':
			self.__synth.setVolume(int(data[1:]))
			
	def __getSynthState(self):
		volume = 'v' + str(self.__synth.getVolume())
		frequency = 'f' + str(self.__synth.getFrequency())
		return [volume, frequency]
		
	#def __setPureDataConnector(self, data):
	#	int = 1 #dummy statement
	#	pass
		
	
	
