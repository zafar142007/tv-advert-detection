from record import Recorder
from queue import Queue
from threading import Thread
import keras
import librosa
import numpy as np
import sys

MODEL='model-2020-04-28-09_10_51-166346'
mean =np.load('../model/'+MODEL+'_mean.npy')
var=np.load('../model/'+MODEL+'_var.npy')

class Detector:
	def __init__(self, minutes):
		self.queue = Queue(maxsize=100)
		self.recorder = Recorder(self.queue)
		self.minutes=minutes;
		self.model = keras.models.load_model('../model/'+MODEL+'.h5');

		t = Thread(target=self.worker)
		t.start()

	def worker(self):
		self.recorder.record(self.minutes)

	def detect(self):
		print("started detection")
		while True:
			try:
				file = self.queue.get(block=True, timeout=10)
				print("reading file for detection "+ file)
				y, sr = librosa.load(file, mono=True, duration=5)
				rmse = librosa.feature.rms(y=y)
				chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
				spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
				spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
				rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
				zcr = librosa.feature.zero_crossing_rate(y)
				mfcc = librosa.feature.mfcc(y=y, sr=sr)
				features = np.array([np.mean(chroma_stft), np.mean(rmse), np.mean(spec_cent), np.mean(spec_bw), np.mean(rolloff), np.mean(zcr)] , dtype = np.float32)   
				for e in mfcc:
					features = np.append(features, np.mean(e))
				scaled_features = np.divide(np.subtract(features , mean),np.sqrt(var));
				prediction = self.model.predict(np.array([scaled_features]));
				print(prediction)
				if prediction[0][0] > prediction[0][1] :
					print("AD")
				else:
					print("NON-AD")
			except Exception:
				print("End")
				break
if __name__ == "__main__":
	detector = Detector(sys.argv[1]);
	detector.detect()
