import pyaudio
import sys
from datetime import datetime
import wave

class Recorder:
	def __init__(self, queue):
		self.queue = queue

	def record(self, minutes):

		chunk = 1024
		FORMAT = pyaudio.paInt16
		CHANNELS = 1
		RATE = 44100
		RECORD_SECONDS = 5
		TOTAL_RECORD_TIME_MIN=int(minutes) #in minutes


		for i in range((int)(TOTAL_RECORD_TIME_MIN*60/RECORD_SECONDS)):
			WAVE_OUTPUT_FILENAME = '../dataset/raw/'+str(datetime.now()).replace(' ', '-').replace('.', '-')+".wav"
			p = pyaudio.PyAudio()
			stream = p.open(format=FORMAT,
			                channels=CHANNELS, 
			                rate=RATE, 
			                input=True,
			                output=True,
			                frames_per_buffer=chunk)

			print(str(i)+ " recording started")
			frames=[]
			for i in range(0, (int)(44100 / chunk * RECORD_SECONDS)):
				data = stream.read(chunk)
				frames.append(data)
			    # check for silence here by comparing the level with 0 (or some threshold) for 
			    # the contents of data.
			    # then write data or not to a file

			print("recording done")

			stream.stop_stream()
			stream.close()
			p.terminate()
			wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
			wf.setnchannels(CHANNELS)
			wf.setsampwidth(p.get_sample_size(FORMAT))
			wf.setframerate(RATE)
			wf.writeframes(b''.join(frames))
			wf.close()
			if self.queue is not None:
				self.queue.put(WAVE_OUTPUT_FILENAME, block=True, timeout=RECORD_SECONDS);


if __name__ == "__main__":
	recorder = Recorder(None)
	recorder.record(sys.argv[1])
