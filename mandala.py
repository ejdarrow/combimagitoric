# IMPORTING PACKAGES

import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.playback import play
from PIL import Image
import time
import math
from multiprocessing import Process


# PREPARING THE AUDIO DATA

# Audio file, .wav file
wavFile = "test_audio.wav"

# Retrieve the data from the wav file
data, samplerate = sf.read(wavFile)

n = len(data)  # the length of the arrays contained in data
Fs = samplerate  # the sample rate
print(n)
print(Fs)
# Working with stereo audio, there are two channels in the audio data.
# Let's retrieve each channel seperately:
ch1 = np.array([data[i] for i in range(n)])  # channel 1
#ch2 = np.array([data[i] for i in range(n)])  # channel 2
print(len(ch1))

# x-axis and y-axis to plot the audio data
result = Image.new(mode="RGB",size=(100,100))
for i in ch1:
    

print(np.max(ch1))
result = Image.frombytes(mode="RGB", size=math.sqrt(n))
result.save("result.png")
# You can run the two lines below to plot the audio data contained in the audio file
#plt.plot(time_axis, sound_axis)
#plt.show()



