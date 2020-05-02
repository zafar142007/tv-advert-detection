from recorder import Recorder
from clientAudioHandler import ClientAudioHandler
import sys

class ClientRunner:
	def __init__(self, minutes):
		clientAudioHandler = ClientAudioHandler()
		Recorder().record(minutes, clientAudioHandler)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		minutes = sys.argv[1];
	else:
		minutes = None
	runner = ClientRunner(minutes)