import numpy as np
import sounddevice as sd
import speech_recognition as sr
from scipy.io import wavfile

recogniser = sr.Recognizer()
fr = 44100
seconds = 10
print('The recording has started')

data = sd.rec(int(seconds*fr),samplerate=fr,channels=2)


sd.wait()
y = (np.iinfo(np.int32).max * (data/np.abs(data).max())).astype(np.int32)
print('Finished recording')
wavfile.write('new_rec.wav', fr, y)


sound = sr.AudioFile('new_rec.wav')

with sound as source:
    audio = recogniser.record(source)

text = recogniser.recognize_google(audio)
print(text)