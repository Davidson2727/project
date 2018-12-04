from pyo import *
class TransformModel:
	def __init__(self, source):
		self.source = source
		self.transform = None
		self.on = True
	
	def setValues(self, value):
		if isinstance(self.source, Chorus):
			self.source.setDepth(value)
		elif isinstance(self.source, Harmonizer):
			self.source.setTranspo(value)
		elif isinstance(self.source, FreqShift):
			self.source.setShift(value)
		elif isinstance(self.source, STRev):
			self.source.setRevtime(value)
		else: #this might be bad
			self.source.setDrive(value)
	
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