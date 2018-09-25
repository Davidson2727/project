from Synth import Synth 
from DataPath import DataPath
class Controller:
	def __init__(self):
		self.__synth = Synth()
		#self.__PureDataConnector()
		self.__dataPath = DataPath()
	
	def receiver(self, data):
		if data[0] == 'f' or data[0] == 'v':
			self.__setSynthState(data)
			self.__setPureDataConnectorState(data)
		if data[0] == 'w':
			self.__toDataPath()
		if data[0] == 'o':
			self.__fromDataPath()
	
	def __setSynthState(self,data):	
		if data[0] == 'f':
			self.__synth.setFrequency(int(data[1:]))
		if data[0] == 'v':
			self.__synth.setVolume(int(data[1:]))
			
	def __getSynthState(self):
		volume = 'v' + str(self.__synth.getVolume())
		frequency = 'f' + self.__synth.getFrequency()
		return [volume, frequency]
	
	def __toDataPath(self):
		__dataPath.flush(self.__synth.getSynthState())
	
	def __fromDataPath(self):
		self.__dataPath.open()
		fileState =self. __dataPath.getFileState()
		for i in fileState:
			self.receiver(i)
		
		
	def __setPureDataConnector(self, data):
		int = 1 #dummy statement
		pass
		
	
	
