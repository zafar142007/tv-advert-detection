import os
from soundWave import SoundWave
import librosa
from config import config 

class BasicAudioProvider:
	def __init__(self, frames):
		self.frames = frames
		self.soundWave = SoundWave()

	def provide(self):
		output = []
		WAVE_OUTPUT_FILENAME = self.soundWave.save(self.frames, config["tmpPath"], 2)
		y, sr = librosa.load(WAVE_OUTPUT_FILENAME, mono=True)
		os.remove(WAVE_OUTPUT_FILENAME)
		return y, sr