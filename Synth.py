class Synth:
	def __init__(self):
		self.__volume = 0
		self.__frequency = 0
	
	def getVolume(self):
		return self.__volume
	
	def setVolume(self, _volume):
		self.__volume = _volume
	
	def getFrequency(self):
		return self.__frequency
		
	def setFrequency(self, _frequency):
		self.__frequency = _frequency
		