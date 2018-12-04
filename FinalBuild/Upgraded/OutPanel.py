from wx import *
from pyo import *
from OutputButton import OutputButton
from State import State
	
class OutPanel:
	def __init__(self, rowPanel):
		self.defineFields(rowPanel)
		self.outputPanelStructure()
		
	def defineFields(self, rowPanel):
		self.rowElementPanel = Panel(rowPanel) 
		self.buttonPanel = None
		self.soundPanel = None
		self.button = None
		self.state = None
		
	def outputPanelStructure(self):
		self.buttonPanel = Panel(self.rowElementPanel)
	
	def setup(self):
		buttonBox = BoxSizer(HORIZONTAL)
		buttonBox.Add(self.buttonPanel)
		self.rowElementPanel.SetSizerAndFit(buttonBox)
	
	def link(self, soundPanel):
		self.soundPanel = soundPanel
	
	def getPanel(self):
		return self.rowElementPanel
	
	def addButton(self, source):
		self.state = State(source)
		self.button = OutputButton(self.buttonPanel, self.state)
		self.setup()
		
	def setSource(self, source):
		self.state.setSource(source)
	