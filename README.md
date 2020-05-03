Adastra
=======

This is a utility to detect TV advertisements by audio through a trained artificial neural network. The training dataset was collected from various Indian news channels comprising 5 second audios. The ultimate aim is to develop an Android app that could mute the idiot box when advertisements are playing and vice versa.

Capabilities
============
The utility could run in three modes.

1. Client-Server mode

In this mode, a server is run which is able to classify incoming audio streams as TV ads or not. A client would record from the default audio device and send these audios to the server over HTTP to classify them as ads/non-ads.

2. Console mode

In this mode, the utility would run on a machine, recording audios from the default audio device, classify them, and print the results.

3. Dataset collection mode

In this mode, a recorder program would run, recording audios from the default audio device and store them in a designated folder for use as dataset. The labelling would be done manually later on this dataset.


Setup
=====

Install anaconda 3.7. Probably use a Docker image with Anaconda preinstalled.

Then install the following libraries.

Server:
------

```
conda install -c conda-forge librosa

conda install -c conda-forge keras

conda install -c anaconda flask
```

Client:
------

```
conda install -c anaconda urllib3

conda install -c anaconda pyaudio
```

Run the scripts from a conda shell from root directory 

```
./scripts/server.sh

./scripts/serverClient.sh <number of minutes to run the program or omit this parameter to run indefinitely>
```

This will 

1. start a local classification server listening for requests,

2. start to record 5 second audios from the default audio device and then try to classify if it is an advertisement or not by sending it to the local server.

The server and the client could be on different machines.

The configurations are in the config.json file.

Console mode
------------

To run in console mode, install all of the above dependencies (both server and client) and run the following from the root directory of this project from a conda shell.

```
./scripts/consoleRunner.sh <number of minutes to run the program or omit this parameter to run indefinitely>
```

Dataset collection mode
------------

To run in console mode, install all of the above dependencies (both server and client) and run the following from the root directory of this project from a conda shell.

```
./scripts/collectDataset.sh <number of minutes to run the program or omit this parameter to run indefinitely>
```

