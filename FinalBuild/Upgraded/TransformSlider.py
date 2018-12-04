from pyo import *
from wx import *
from TransformController import TransformController

class TransformSlider:
	def __init__(self, panel, model):
		self.defineFields()
		self.createWidget(panel)				
		self.setupSlider(model.getSource())
		TransformController(self.widget, model)
		
	def defineFields(self):
		self.chorus = [0, 5, 1, False]
		self.harm = [-7, 0, -7, False]
		self.freqShift = [0, 50, 0, False]
		self.reverb = [0, 5, 1, False]
		self.disto = [0, 1, 0, False]
		self.type = {"Chorus":self.chorus,"Harmonizer":self.harm, \
					 "FrequencyShift":self.freqShift, "Reverb":self.reverb, \
					 "Distortion":self.disto}
		self.widget = None
		
	
	def createWidget(self, panel):
		self.widget = PyoGuiControlSlider(parent= panel, minvalue=0, maxvalue=1, \
						init=0.5, pos=(0,0), size=(200, 16), log=False, \
						integer=False, powoftwo=False, orient=HORIZONTAL)
	
	def setupSlider(self, model = None, choice = "None"):
		list = None
		if choice == "Chorus" or isinstance(model, Chorus):
			list = self.type["Chorus"]
		elif choice == "Harmonizer" or isinstance(model, Harmonizer):
			list = self.type["Harmonizer"]
		elif choice == "FrequencyShift" or isinstance(model, FreqShift):
			list = self.type["FrequencyShift"]
		elif choice == "Reverb" or isinstance(model, STRev):
			list = self.type["Reverb"]
		else: #this might be bad
			list = self.type["Distortion"]
		self.widget.setValue(list[2])
		self.widget.log = list[3]
		self.widget.minvalue = list[0]
		self.widget.maxvalue = list[1]
	
	def getWidget(self):
		return self.widget