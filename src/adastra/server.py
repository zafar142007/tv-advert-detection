from flask import Flask, request
from detect import Detector
from config import config
from basicAudioProvider import BasicAudioProvider

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():
	data = request.get_data(cache=False, as_text=False, parse_form_data=False)
	
	provider = BasicAudioProvider(data)
	detector = Detector(provider);
	return detector.classify()

if __name__ == '__main__':
	app.run(debug=True, port=config["serverPort"])