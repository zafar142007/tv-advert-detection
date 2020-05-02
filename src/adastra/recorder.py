import pyaudio
import sys
from datetime import datetime
import wave
import requests
from consoleAudioHandler import ConsoleAudioHandler
from config import config

class Recorder:
	def __init__(self):
		pass		

	def record(self, minutes, audioHandler):

		chunk = 1024
		FORMAT = pyaudio.paInt16
		CHANNELS = 1
		RATE = config["samplingRate"]
		RECORD_SECONDS = config["recordingLengthS"]
		iterations = 1
		step = -1
		if minutes is not None:
			print('Running for '+str(minutes)+ ' minutes')
			iterations = (int)((int)(minutes)*60/RECORD_SECONDS)
			step = 1
		else:
			print('Running forever')
		while iterations > 0:
			p = pyaudio.PyAudio()
			stream = p.open(format=FORMAT,
			                channels=CHANNELS, 
			                rate=RATE, 
			                input=True,
			                output=True,
			                frames_per_buffer=chunk)

			print(str(iterations)+ ' recording started')
			frames=[]
			for i in range(0, (int)(RATE / chunk * RECORD_SECONDS)):
				data = stream.read(chunk)
				frames.append(data)

			print('recording done')
			stream.stop_stream()
			stream.close()
			p.terminate()
			print(audioHandler.handle(frames))
			iterations = iterations - step

if __name__ == '__main__':
	recorder = Recorder()
	if len(sys.argv) > 1:
		recorder.record(sys.argv[1], ConsoleAudioHandler(None, config["datasetPath"]+"raw/")) ##run in dataset collection mode
	else:
		recorder.record(None, ConsoleAudioHandler(None, config["datasetPath"]+"raw/")) #run forever in dataset collection mode