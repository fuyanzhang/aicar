import librosa as sa
from dtw import dtw
from numpy.linalg import norm

x,sr = sa.load("data/testing/apple/Apple.wav")
mfcc_1 = sa.feature.mfcc(x,sr)

y,sr_y = sa.load("data/testing/apple/apple15.wav")
mfcc_2 = sa.feature.mfcc(y,sr_y)

z,sr_z = sa.load("data/testing/banana/banana15.wav")
mfcc_3 = sa.feature.mfcc(z,sr_z)

dist,cost,acc_cost,path = dtw(mfcc_1.T,mfcc_2.T,dist=lambda x,y: norm(x-y,ord=1))
print(dist) 

dist1,cost1,acc_cost1,path1 = dtw(mfcc_1.T,mfcc_3.T,dist=lambda x,y: norm(x-y,ord=1))
print(dist1) 

dist2,cost2,acc_cost2,path2 = dtw(mfcc_2.T,mfcc_3.T,dist=lambda x,y: norm(x-y,ord=1))
print(dist2)  