from pyo import *
from SoundModel import SoundModel

class State:
	def __init__(self, source):
		self.source = source
		self.state = True
		self.source.out()
		
	def setState(self):
		self.state = not self.state
		if self.state:
			self.source.out()
		else:
			self.source.stop()
	
	def getState(self):
		if self.state:
			return "On"
		return "off"
	
	def setSource(self, source):
		self.source = source