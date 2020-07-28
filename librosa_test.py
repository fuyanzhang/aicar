import librosa
# import matplotlib.pyplot as plt
# import librosa.display
import hmmlearn.hmm as hl
import numpy as np
import os

def getFiles(path):
    objects = {}
    for currentDir,subdirs,files in os.walk(path):
        for file in files:
            if file.endswith('.wav'):
                label = currentDir.split(os.path.sep)[-1]
                if label not in objects:
                    objects[label] = []
                path = os.path.join(currentDir,file)
                objects[label].append(path)   
    return objects
def featureEx(train_file):
    results = {}
    for k,v in train_file.items():
        mfccs = np.array([])
        for file in v:
            x,sr = librosa.load(file)
            mfcc = librosa.feature.mfcc(x,sr=sr)
            if len(mfccs) == 0:
                mfccs = mfcc
            else:
                mfccs = np.append(mfccs,mfcc)
        results[k]=(mfccs)                
    return results
def train(mfccResult):
    models={}
    for k,v in mfccResult.items():
        model = hl.GaussianHMM(n_components=4,covariance_type='diag',n_iter=1000)
        print(v.shape)
        models[k] = model.fit(v.reshape(-1,1))
    return models        
train_file = getFiles("data/training")
# print(train_file)
mfccResult = featureEx(train_file)
# print(mfccResult)
models = train(mfccResult)
# print(models)

test_x,test_sr = librosa.load("data/testing/apple/Apple.wav")
test_mfcc = librosa.feature.mfcc(test_x,sr=test_sr)
best_score,best_label = None,None
for label,model in models.items():
    score = model.score(test_mfcc.reshape(-1,1))
    print(label +"=="+ str(score))
    if(best_score is None) or (best_score < score):
        best_score = score
        best_label = label

print(best_label)        
    

