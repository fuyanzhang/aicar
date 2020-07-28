import librosa as sa
from dtw import dtw
from numpy.linalg import norm
import os

def getFiles(path):
    objects = []
    for currentDir,subdirs,files in os.walk(path):
        for file in files:
            if file.endswith('.wav'):
                path = os.path.join(currentDir,file)
                objects.append(path)   
    return objects
files= getFiles("data/cmd")

in_file=files[3]
result_file="xxxxx"
resultdist=-100
x,sr = sa.load(in_file)
mfcc_1 = sa.feature.mfcc(x,sr)
for index in range(len(files)):
    if index == 3:
        continue
    else:
        tmp_file = files[index]
        tmp,sr_tmp = sa.load(tmp_file)
        mfcc_tmp = sa.feature.mfcc(tmp,sr_tmp)
        dist,cost,acc_cost,path = dtw(mfcc_1.T,mfcc_tmp.T,dist=lambda x,y: norm(x-y,ord=1))
        if resultdist == -100:
            resultdist = dist
            result_file = tmp_file
        else:
            if dist<resultdist:
                 resultdist = dist
                 result_file =  tmp_file
print("----------")
print (result_file)               