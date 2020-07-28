import librosa.display
import matplotlib.pyplot as plt
from dtw import dtw
from numpy.linalg import norm
import numpy as np
y,sr = librosa.load('data/11.wav')
y1,sr1 = librosa.load('data/前进1.wav')
y2,sr2 = librosa.load('data/qpd.wav',sr=22050,mono=True,offset=0.0,duration=3)

#提取特征
plt.subplot(1, 4, 1)
mfcc = librosa.feature.mfcc(y,sr)
librosa.display.specshow(mfcc)
plt.subplot(1, 4, 2)
mfcc1 = librosa.feature.mfcc(y1,sr1)
mfcc1.shape
librosa.display.specshow(mfcc1)
plt.subplot(1, 4, 3)
mfcc2 = librosa.feature.mfcc(y2,sr2)
librosa.display.specshow(mfcc2)

plt.subplot(1, 4, 4)
x = np.array(mfcc.T).reshape(-1,1)
y = np.array(mfcc1.T).reshape(-1,1)
z = np.array(mfcc2.T).reshape(-1,1)

plt.plot(x, label='x')
# plt.plot(y, label='y')
plt.plot(z, label='z')
plt.title('Our three temporal sequences')
plt.legend()
# dist1, cost1, acc_cost1, path1 = dtw(mfcc.T, mfcc1.T, dist=lambda x, y: norm(x - y, ord=1))
# print(dist1)

# dist2, cost2, acc_cost2, path2 = dtw(mfcc.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
# print(dist2)

plt.show()