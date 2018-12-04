from wx import *
from AbstractController import AbstractController
from State import State

class ButtonStateController(AbstractController):
	def __init__(self, view, model):
		super().__init__(view, model) #change something here to do the algorithm
		
	def control(self, evt):
		#setsource after parsing which are on and which are off
		self.model.setState()                    
		self.view.SetLabel(self.model.getState())