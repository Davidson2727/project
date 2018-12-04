from wx import *
from SourcePanel import SourcePanel
from TransformPanel import TransformPanel

class SoundPanel2:
	def __init__(self, rowPanel, frame):
		self.defineFields(rowPanel, frame) 
		self.soundPanelStructure()		   
		self.initialSetup()				   
		
	def defineFields(self,rowPanel, frame):
		self.soundPanel = Panel(rowPanel)
		self.sourcePanel = Panel(self.soundPanel)
		self.comboBoxPanel = Panel(self.soundPanel)
		self.transformListPanel = Panel(self.soundPanel)
		self.outPanelLink= None
		self.box = None
		self.transformList = []
		self.outPanelLink = None
		self.length = 0
		self.frame = frame 
		
	def soundPanelStructure(self):
		self.source = SourcePanel(self.comboBoxPanel, self.sourcePanel)
		self.source.Bind(self.setupFirstTransform) #here is a save point
		self.source.setFrameLink(self.frame)
		
	def initialSetup(self):
		self.box = BoxSizer(HORIZONTAL)
		self.box.Add(self.comboBoxPanel)
		self.box.Add(self.sourcePanel)
		self.box.Add(self.transformListPanel)
		self.soundPanel.SetSizer(self.box)  #sizer and fit doesnt work here
		print("initset")
	
	def setupFirstTransform(self, evt): #creates, links, binds, stores
		print("here")
		panel = Panel(self.transformListPanel)  # i cant seebecause some weird heirarchy
		self.transformPanel = TransformPanel(panel)#
		self.outPanelLink.addButton(self.source.getSource())
		self.transformPanel.link(self.source)
		self.transformPanel.setFrameLink(self.frame)
		self.transformPanel.setupSource()
		self.transformPanel.Bind(self.test) #make first transister carry a created attribute 
		self.transformList.append(self.transformPanel)
		self.length = self.length + 1
		self.frame.Layout()
		self.frame.Fit()
		#self.setupTransform(panel)
	
	def test(self, evt):
		self.outPanelLink.setSource(self.transformPanel.getTransform())
		print("wassup")
		
	
	def setupNextTransform(self, evt):
		self.outPanelLink.setSource(self.transformList[self.length - 1].getTransform())
		transform = TransformPanel(self.soundPanel)
		transform.link(self.transformList[self.length - 1]) #stop after 5 filters
		transform.Bind(self.setupNextTransform)
		self.transformList.append(transform)
		self.setupTransform(transform)
		self.length = self.length + 1
		#somehow construct a list where the button can pase through 
	
	def setupTransform(self, panel):
		self.box.Add(panel)
		self.soundPanel.SetSizer(self.box)
		self.frame.Layout()
		self.frame.Fit()
	
	#linked here when testing iff off, on and off of the button will make one manipulate the list that is what output button does
	
	def link(self, outPanel):
		self.outPanelLink = outPanel
	
	def linkFrame(self, frame):
		print("row", frame)
		self.frame = frame
	
	def getPanel(self):
		return self.soundPanel
		