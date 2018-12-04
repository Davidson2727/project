from pyo import *
from wx import *
from SoundModel import SoundModel
from FrequencySlider2 import FrequencySlider2
from OutputButton import OutputButton
from VolumeSlider import VolumeSlider

class WaveGenerator3:
	def __init__(self, panel):
		self.defineFields(panel)
	
	def defineFields(self,panel):
		self.panel = panel
		self.volumeSlider = None
		self.frequencySlider = None
		self.outputButton = None
		self.activated = False
		self.chosenSource = None
		self.soundModel = None
		self.waveDictionary = {"None":None, 											\
							   "Sine":Sine(), 											\
							   "Saw":Osc(table = SawTable().normalize()), 				\
					           "Square":Osc(table = SquareTable().normalize()), 		\
					           "Music":SfPlayer("/Users/jorgesalas/documents/python/christmas.wav.download/christmas.wav", loop=True)}
		self.transformPanelLink = None
		self.frameLink = None
		
	def setSource(self, sourcechoice):
		if self.activated:
			self.soundModel.stop()
			self.frequencySlider.setupSlider(choice = sourcechoice)
			print("is activated")
			
		chosenSource = self.waveDictionary[sourcechoice]
		print("chose", chosenSource)
		self.chosenSource = chosenSource
		self.soundModel = SoundModel(chosenSource)
		print("chose", chosenSource)
		
		if  not self.activated:
			print("about to activate")
			self.waveGeneratorStructure()
			self.setup()
			self.activated = True
			self.refresh()
			
	def waveGeneratorStructure(self):
		print("wave gen")
		self.frequencySlider = FrequencySlider2(self.panel, self.soundModel)
		self.volumeSlider = VolumeSlider(self.panel, self.soundModel)
		self.outputButton = OutputButton(self.panel, self.soundModel)
	
	def setup(self):
		print("setup")
		box = BoxSizer(VERTICAL)
		box.Add(self.frequencySlider.getWidget())
		box.Add(self.volumeSlider.getWidget())
		box.Add(self.outputButton.getWidget())
		self.panel.SetSizer(box)
	
	def refresh(self):
		self.frameLink.Layout()
		self.frameLink.Fit()
	
	def isActivated(self):
		return self.activated
		
	def linkTransformPanel(self, transformPanel):
		self.transformPanelLink = transformPanel
	
	def linkFrame(self, frame):
		self.frameLink = frame
		
	def getSource(self):
		return self.chosenSource

			
		
		