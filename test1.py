# -*- encoding:utf-8 -*-
import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import matplotlib.pyplot as plt

sample_rate, sigs = wf.read('data/qpd.wav')
print(sample_rate)      # 8000采样率
print(sigs.shape)   # (3251,)
sigs = sigs / (2 ** 15) # 归一化
times = np.arange(len(sigs)) / sample_rate
freqs = nf.fftfreq(sigs.size, 1 / sample_rate)
ffts = nf.fft(sigs)
pows = np.abs(ffts)
plt.figure('Audio')
plt.subplot(121)
plt.title('Time Domain')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Signal', fontsize=12)
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')
plt.plot(times, sigs, c='dodgerblue', label='Signal')
plt.legend()
plt.subplot(122)
plt.title('Frequency Domain')
plt.xlabel('Frequency', fontsize=12)
plt.ylabel('Power', fontsize=12)
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')
plt.plot(freqs[freqs >= 0], pows[freqs >= 0], c='orangered', label='Power')
plt.legend()
plt.tight_layout()
plt.show()