from soundWave import SoundWave

class ConsoleAudioHandler:
	def __init__(self, queue, filePath):
		self.queue = queue		
		self.soundWave = SoundWave()
		self.filePath = filePath

	def handle(self, frames):
		WAVE_OUTPUT_FILENAME = self.soundWave.save(b''.join(frames), self.filePath, 2)
		if self.queue is not None:
			self.queue.put(WAVE_OUTPUT_FILENAME, block=True);
		return ""
