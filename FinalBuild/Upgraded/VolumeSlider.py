from pyo import *
from wx import *
from VolumeController import VolumeController

class VolumeSlider:
	def __init__(self, panel, source):
		self.defineFields()
		self.createWidget(panel)
		VolumeController(self.widget, source)
		
	def defineFields(self):
		self.widget = None 
	
	def createWidget(self, panel):
		self.widget = PyoGuiControlSlider(parent= panel, minvalue=0, maxvalue=18, \
						init=12, pos=(0,0), size=(200, 16), log=False, \
						integer=False, powoftwo=False, orient=HORIZONTAL)
	def getWidget(self):
		return self.widget
	