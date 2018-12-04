from pyo import *
from wx import *

class AbstractController:
	def __init__(self, view, model):
		view.Bind(self.__getEventType(view), self.control)
		self.view = view
		self.model = model
		
	def __getEventType(self, view):
		if isinstance(view, Button):
			return EVT_BUTTON
		elif isinstance(view, PyoGuiControlSlider):
			return EVT_PYO_GUI_CONTROL_SLIDER
			
	def control(self, evt):
		pass