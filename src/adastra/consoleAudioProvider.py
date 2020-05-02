from queue import Queue
import librosa

class ConsoleAudioProvider:
	def __init__(self, queue):
		self.queue = queue;

	def provide(self):
		file = self.queue.get(block=True, timeout=20);
		y, sr = librosa.load(file, mono=True)
		return y, sr