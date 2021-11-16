import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

fr = 44100
seconds = 10
print('The recording has started')

data = sd.rec(int(seconds*fr),samplerate=fr,channels=2)


sd.wait()
y = (np.info(np.int32).max * (data/np.abs(data).max())).astype(np.int32)
print('Finished recording')
write('new_rec.wav',fr,y)