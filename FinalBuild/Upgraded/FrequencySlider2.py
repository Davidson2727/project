from wx import *
from pyo import *
from SoundModel import SoundModel
from FrequencyController import FrequencyController

class FrequencySlider2:
	def __init__(self, panel, model):
		self.defineFields()
		self.createWidget(panel)				
		self.setupSlider(model)
		FrequencyController(self.widget, model)
		
	def defineFields(self):
		self.pureTone = [20, 20000, 1000, True]
		self.music = [-5,5,1, False]
		self.type = {"None":-1,"Sine":1, "Saw":1, "Square":1, "Music":0}
		self.widget = None
		
	
	def createWidget(self, panel):
		self.widget = PyoGuiControlSlider(parent= panel, minvalue=20, maxvalue=20000, \
						init=1000, pos=(0,0), size=(200, 16), log=True, \
						integer=False, powoftwo=False, orient=HORIZONTAL)
	
	def setupSlider(self, model = None, choice = "None"):
		if self.type[choice] != 0 and (self.type[choice] == 1 or              \
		   isinstance(model.getSource(), Sine) or \
		   isinstance(model.getSource(), Osc)):
			self.widget.setValue(self.pureTone[2])
			self.widget.log = self.pureTone[3]
			self.widget.minvalue = self.pureTone[0]
			self.widget.maxvalue = self.pureTone[1]
		else:
			self.widget.setValue(self.music[2])
			self.widget.log = self.music[3]
			self.widget.minvalue = self.music[0]
			self.widget.maxvalue = self.music[1]
	
	def getWidget(self):
		return self.widget
			
			
		
		
	   
	   