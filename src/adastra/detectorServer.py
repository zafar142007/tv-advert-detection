from flask import Flask, request
from serverAudioProvider import ServerAudioProvider
from detect import Detector
from queue import Queue
from threading import Thread
from config import config

queue = Queue(maxsize=100);

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():
	data = request.get_data(cache=False, as_text=False, parse_form_data=False)
	queue.put(data, block=True)	
	return "OK"

def worker():
	provider = ServerAudioProvider(queue)
	detector = Detector(provider);
	detector.detect()

if __name__ == '__main__':
	t = Thread(target=worker)
	t.start()

	app.run(debug=True, port=config["serverPort"])


