from wx import *
from WaveGenerator3 import WaveGenerator3
from pyo import *
class SourcePanel:
	def __init__(self, comboBoxPanel, sourcePanel):
		self.defineFields()
		self.sourcePanelStructure(comboBoxPanel, sourcePanel)
		
	def defineFields(self):
		self.comboBox = None
		self.sourceSliders = None
		self.box = None
		self.activated = False
		
	def sourcePanelStructure(self, comboBoxPanel, sourcePanel):
		self.comboBox = ComboBox(comboBoxPanel, choices = ["---", "Sine", "Saw", "Square", "Music"])
		self.sourceSliders = WaveGenerator3(sourcePanel)
		
	def setSlidersSource(self, evt):#do the stop here maybe?
		print(evt.GetString())
		self.sourceSliders.setSource(evt.GetString()) #activated field in WaveGenerator3
		evt.Skip() 
	
	def link(self, transformPanel):
		self.sourceSliders.linkTransformPanel(transformPanel)
	
	def setFrameLink(self, frame):
		self.sourceSliders.linkFrame(frame)
	
	def isActivated(self):
		return self.sourceSliders.isActivated()	
	
	def getPanel(self):
		return self.sourcePanel	
	
	def getSource(self):
		return self.sourceSliders.getSource()
	
	def Bind(self, handler):
		self.comboBox.Bind(EVT_COMBOBOX, handler)
		self.comboBox.Bind(EVT_COMBOBOX, self.setSlidersSource)
		
		
		
	
		