# -*- coding: utf-8 -*-
import wave
import numpy as np
import scipy.signal as signal

framerate = 44100   # 采样频率
time = 10           # 持续时间

t = np.arange(0, time, 1.0/framerate)

# 调用scipy.signal库中的chrip函数，
# 产生长度为10秒、取样频率为44.1kHz、100Hz到1kHz的频率扫描波
wave_data = signal.chirp(t, 100, time, 1000, method='linear') * 10000

# 由于chrip函数返回的数组为float64型，
# 需要调用数组的astype方法将其转换为short型。
wave_data = wave_data.astype(np.short)

# 打开WAV音频用来写操作
f = wave.open(r"data/sweep.wav", "wb")

f.setnchannels(1)           # 配置声道数
f.setsampwidth(2)           # 配置量化位数
f.setframerate(framerate)   # 配置取样频率
comptype = "NONE"
compname = "not compressed"

# 也可以用setparams一次性配置所有参数
# outwave.setparams((1, 2, framerate, nframes,comptype, compname))

# 将wav_data转换为二进制数据写入文件
f.writeframes(wave_data.tostring())
f.close()
