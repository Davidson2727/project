from AbstractController import AbstractController
from SoundModel import SoundModel
from pyo import *

class FrequencyController(AbstractController):
	def __init__(self, view, model):
		super().__init__(view,model)
		
	def control(self, evt):
		self.model.setFrequency(evt.value)