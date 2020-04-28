Install anaconda 3.7. Probably use a Docker image with Anaconda preinstalled.
Then
conda install -c conda-forge librosa
conda install -c anaconda pyaudio
conda install -c conda-forge keras

Run the program from a conda shell by 
python detect.py <number of minutes you want the program to run>

This will start to record 5 second audios from the default audio device and then try to classify if it is an advertisement or not.
