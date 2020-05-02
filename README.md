Adastra
=======

This is a utility to detect TV advertisements by audio through a trained artificial neural network. The training dataset was collected from various Indian news channels comprising 5 second audios. The ultimate aim is to develop an Android app that could mute the idiot box when advertisements are playing and vice versa.

Setup
=====

Install anaconda 3.7. Probably use a Docker image with Anaconda preinstalled.

Then install the following libraries.

Server:

conda install -c conda-forge librosa

conda install -c conda-forge keras

conda install -c anaconda flask

Client:

conda install -c anaconda urllib3

conda install -c anaconda pyaudio

Run the scripts from a conda shell from root directory 

./server.sh

./serverClient.sh

This will 

1. start a local classification server listening for requests,

2. start to record 5 second audios from the default audio device and then try to classify if it is an advertisement or not by sending it to the local server.

The configurations are in the config.json file.

The server and the client could be on different machines.
