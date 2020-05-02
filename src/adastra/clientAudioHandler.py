import urllib
from config import config

class ClientAudioHandler:
	def handle(self, frames):
		frames = [item for sublist in frames for item in sublist]
		req = urllib.request.Request(url = config["serverUrl"]+":"+str(config["serverPort"])+"/detect", data = bytes(frames))
		req.add_header('Content-Length', '%d' % len(frames))
		req.add_header('Content-Type', 'application/octet-stream')
		with urllib.request.urlopen(req) as f:
			return f.read()
