from detect import Detector
from recorder import Recorder
from threading import Thread
import sys
from queue import Queue
from consoleAudioProvider import ConsoleAudioProvider
from consoleAudioHandler import ConsoleAudioHandler
from config import config

class ConsoleRunner:
	def __init__(self, minutes):
		queue = Queue(maxsize=100);
		self.queue = queue
		self.recorder = Recorder()
		self.minutes=minutes;
		self.consoleAudioHandler = ConsoleAudioHandler(self.queue, config["tmpPath"])
	
		t = Thread(target=self.worker)
		t.start()

		provider = ConsoleAudioProvider(self.queue)

		detector = Detector(provider);
		detector.detect()

	def worker(self):
		self.recorder.record(self.minutes, self.consoleAudioHandler)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		minutes = sys.argv[1];
	else:
		minutes = None
	runner = ConsoleRunner(minutes)

