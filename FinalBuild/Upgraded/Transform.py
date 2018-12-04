from wx import *
from pyo import *
from TransformModel import TransformModel
from TransformSlider import TransformSlider
from OutputButton import OutputButton

class Transform:
	def __init__(self, panel):
		self.defineFields(panel)
	
	def defineFields(self, panel):
		self.panel = panel
		self.propertySliderA = None
		self.proterySliderB = None
		self.stateButton = None
		self.activated = False
		self.chosenTransform = None
		self.transformModel = None
		self.transformDictionary = None
		self.transformPanelLink = None
		self.frameLink = None
		self.sourcePanel = None
		self.source = None
	
	def setTransform(self, choice):
		if not self.activated:
			self.defineDictionary(choice)
			
		if self.activated:
			self.transformModel.stop()
			self.transformSlider.setParameters(choice)
			
		chosenTransform = self.transformDictionary[choice]
		self.chosenSource = chosenTransform
		self.transformModel = TransformModel(self.chosenSource)
	
		if  not self.activated:
			self.transformStructure()
			self.setup()
			self.activated = True
			self.refresh()
	
	def transformStructure(self):
		self.transformSlider = TransformSlider(self.panel, self.transformModel)
		self.stateButton = OutputButton(self.panel, self.transformModel)
		
	def setup(self):
		box = BoxSizer(VERTICAL)
		box.Add(self.transformSlider.getWidget())
		box.Add(self.stateButton.getWidget())
		self.panel.SetSizer(box)
	
	def defineDictionary(self, choice):
		self.transformDictionary = {"Chorus":Chorus(self.source), 							\
					 			    "Harmonizer":Harmonizer(self.source), 					\
				                    "FrequencyShift": FreqShift(self.source), 				\
				                    "Reverb":STRev(self.source), 							\
				                    "Distortion": Disto(self.source)}
	
	def refresh(self):
		self.frameLink.Layout()
		self.frameLink.Fit()
			
	def getTransform(self):
		return self.chosenTransform
	
	def setFrameLink(self, frame):
		self.frameLink = frame
	
	def setupSource(self):
		self.source = self.sourcePanel.getSource()
		print(self.source)
	
	def link(self, sourcePanel):
		self.sourcePanel = sourcePanel
		print(sourcePanel.getSource())
	