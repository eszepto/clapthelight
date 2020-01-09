import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
import numpy as np


fs, data = wavfile.read('C:/Users/Be/Desktop/test.wav') # load the data
a = data.T[0] # this is a two channel soundtrack, I get the first track

#norm_data=[(ele/2**16.) for ele in a] # this is 16-bit track, b is now normalized on [-1,1)

fft_data = fft(a) # calculate fourier transform (complex numbers list)
fft_freq = [x for x in range(0,len(fft_data))]
d = len(fft_data)/2  # you only need half of the fft list (real signal symmetry)

fft_data = abs(fft_data)


chunk_size = 44100
num_chunk  = len(fft_data) // chunk_size
sn = []
for chunk in range(0, num_chunk):
    sn.append(np.mean(fft_data[chunk*chunk_size:(chunk+1)*chunk_size]**2))

print(sn)

logsn = 20*np.log10(sn)

print(logsn)

plt.plot(logsn,'r')
plt.show()