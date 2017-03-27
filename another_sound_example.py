#! C:\Python27

import math
import pyaudio

PyAudio = pyaudio.PyAudio

BITRATE = 16000
FREQUENCY1 = 350
FREQUENCY2= 440
LENGTH = 1.5 #seconds

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''

for x in range(NUMBEROFFRAMES):
    WAVEDATA = WAVEDATA + chr(int(math.sin(x/((BITRATE/(FREQUENCY1+FREQUENCY2))/math.pi))*127+128))

# fill remainder of frameset with silence
for x in range(RESTFRAMES):
    WAVEDATA = WAVEDATA + chr(128)

p = PyAudio()
stream = p.open(format = p.get_format_from_width(1),
                channels = 1,
                rate = BITRATE,
                output = True)
stream.write(WAVEDATA)
stream.stop_stream()
stream.close()
p.terminate()