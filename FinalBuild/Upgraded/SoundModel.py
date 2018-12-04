from pyo import *
from wx import *

class SoundModel:
	def __init__(self, wave):
		self.source = wave
		self.on = True
	def setFrequency(self, value):
		if isinstance(self.source, Sine) or isinstance(self.source, Osc):
			self.source.setFreq(value)
		else: 
			self.source.setSpeed(value)
	
	def setAmplitude(self, value):
		self.source.mul = value
	
	def setSource(self,wave):
		self.source = wave
	
	def getSource(self):
		return self.source
	
	def setState(self):
		if self.on:
			self.source.stop()
		else:
			self.source.out()
		self.on = not self.on
	
	def stop(self):
		self.on = False
		self.source.stop()
			
	
	def getState(self):
		if self.on:
			return "On"
		else:
			return "Off"
	