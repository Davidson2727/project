from AbstractController import AbstractController
from SoundModel import SoundModel

class VolumeController(AbstractController):
	def __init__(self, view, model):
		super().__init__(view,model)
	def control(self, evt):
		self.model.setAmplitude(evt.value)