import pyaudio
import wave

chunk = 1024
format = pyaudio.paInt16
channels = 1
rate = 44100

p =pyaudio.Pyaudio()

stream = p.open(format=format
                ,channels=channels
                ,rate=rate
                ,input=True
                ,frames_per_buffer=chunk)

print("start recording...")

frames = []
seconds = 10
for i in range(0, int(rate / chunk *seconds)):
    data = stream.read(chunk)
    frames.append(data)