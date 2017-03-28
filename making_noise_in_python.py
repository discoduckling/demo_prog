import math
import numpy
import pyaudio

def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)

def play_tone(stream, frequency=350, length=5, rate=44100):
    chunks = []
    chunks.append(sine(frequency, length, rate))
    chunk = numpy.concatenate(chunks) * 0.25
    stream.write(chunk.astype(numpy.float32).tostring())

def play_dial_tone(stream, f1, f2, length=5, rate=44100):
    chunks = []
    chunks.append(sine(frequency, length, rate))
    chunk = numpy.concatenate(chunks) * 0.25
    stream.write(chunk.astype(numpy.float32).tostring())

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream1 = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)
    # stream2 = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)
    play_tone(stream1)
    play_tone(stream1, frequency=440)
    # play_dial_tone(stream1, 350, 440)
    # play_tone(stream2, frequency=440)
    stream1.close()
    stream2.close()
    p.terminate()