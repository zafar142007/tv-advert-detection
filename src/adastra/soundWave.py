import wave
from datetime import datetime
import pyaudio
import numpy as np
from config import config

class SoundWave:
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = config["samplingRate"]
	
	def __init__(self):
		pass
	
	#frames should be a Python 'bytes' object (array of bytes)
	def save(self, frames, filePath, sampleSize):
		WAVE_OUTPUT_FILENAME = filePath+str(datetime.now()).replace(' ', '-').replace('.', '-')+'.wav'
		wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		wf.setnchannels(self.CHANNELS)
		wf.setsampwidth(sampleSize)
		wf.setframerate(self.RATE)
		wf.writeframes(frames)
		wf.close()
		return WAVE_OUTPUT_FILENAME