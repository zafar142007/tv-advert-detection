from queue import Queue
import librosa
import os
from soundWave import SoundWave
from config import config

class ServerAudioProvider:
	def __init__(self, queue):
		self.queue = queue;
		self.soundWave = SoundWave()

	def provide(self):
		frames = self.queue.get(block=True, timeout=20);
		output = []
		WAVE_OUTPUT_FILENAME = self.soundWave.save(frames, config["tmpPath"], 2)
		y, sr = librosa.load(WAVE_OUTPUT_FILENAME, mono=True)
		os.remove(WAVE_OUTPUT_FILENAME)
		return y, sr