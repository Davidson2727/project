from Transform import Transform
from wx import *
class TransformPanel:
	def __init__(self, panel):
		self.defineFields(panel)
		self.transformPanelStructure()
		self.setup()
		
	def defineFields(self, panel):
		self.transformPanel = panel
		self.comboBoxPanel = Panel(self.transformPanel)
		self.transformSliderPanel = Panel(self.transformPanel)
		self.transform = None
		self.comboBox = None
		self.frameLink = None
		
	def transformPanelStructure(self):
		self.transform = Transform(self.transformSliderPanel)
		self.comboBox = ComboBox(self.comboBoxPanel, choices = ["---",               \
																  "Chorus",           \
															  	  "Harmonizer",       \
															      "FrequencyShift",   \
															      "Reverb",           \
															      "Distortion"])
		 #i can bind multiple events 
	
	def setup(self):
		self.box = BoxSizer(HORIZONTAL)
		self.box.Add(self.comboBoxPanel)
		#self.box.Add(self.transformSliderPanel)
		self.transformPanel.SetSizerAndFit(self.box)
	
	def setTransformType(self, evt):
		self.transform.setTransform(evt.GetString())
		self.setupSliders()
		evt.Skip()
	
	def setupSliders(self):
		self.box.Add(self.transformSliderPanel)
		self.transformPanel.SetSizerAndFit(self.box)
		self.refresh()
		
	def refresh(self):
		self.frameLink.Layout()
		self.frameLink.Fit()
	
	def Show(self):
		self.comboBox.Show()
		self.refresh()
	
	def Hide(self):
		self.comboBox.Hide()
		self.refresh()
		
	def setTransfromLink(self, transform):
		self.transform.setTransformLink(transform)
	
	def setComponentLink(self, source):
		self.transfrom.setComponentLink(source)
		
	def setFrameLink(self, frame):
		self.frameLink = frame
		self.transform.setFrameLink(frame)
		
	def getSource(self):
		return self.transform.getSource()
	
	def isOn(self):
		return self.transform.isOn()
	
	def getPanel(self):
		return self.transformPanel
	
	def updateSource(self):
		print("updating")
	
	def Bind(self, handler):
		self.comboBox.Bind(EVT_COMBOBOX, handler)
		self.comboBox.Bind(EVT_COMBOBOX, self.setTransformType)
		
	def setupSource(self):
		self.transform.setupSource()
		
	def link(self, sourcePanel):
		self.transform.link(sourcePanel)
	
	def getTransform(self):
		return self.transform.getTransform()
		
	