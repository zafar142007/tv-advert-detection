import keras
import librosa
import numpy as np
from config import config

class Detector:
	def __init__(self, dataSource):

		self.mean =np.load(config["modelPath"]+config["model"]+'_mean.npy')
		self.var=np.load(config["modelPath"]+config["model"]+'_var.npy')
		self.provider = dataSource
		self.model = keras.models.load_model(config["modelPath"]+config["model"]+'.h5');

	def classify(self):
		print('reading for detection ')
		y, sr = self.provider.provide() #y is bytes and sr is sampling rate
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
		scaled_features = np.divide(np.subtract(features , self.mean),np.sqrt(self.var));
		prediction = self.model.predict(np.array([scaled_features]));
		print(prediction)
		if prediction[0][0] > prediction[0][1] :
			return 'AD'
		else:
			return 'NON-AD'	

	def detect(self):
		print('started detection')
		while True:
			try: 
				print(self.classify())
			except Exception as e:
				print('Error: '+ str(e))
				break
