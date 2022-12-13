from pydub import AudioSegment
import pydub
from pydub.playback import play
import os

os.getcwd()
# os.chdir(r".\finalExam")

audio = AudioSegment.from_file(
    "./data/metallic-beat-short/metallic-beat-short.wav", format="wav")

play(audio)

audio.frame_rate
audio.sample_width
2**16/2
audio.channels

x = audio.get_array_of_samples()
x

import matplotlib.pyplot as plt
plt.plot(x, linewidth=0.25)
 
len(x) / 2 / 2 
44100 * 2 * 2

boost_audio = audio + 20
play(boost_audio)
play(audio)

y = boost_audio.get_array_of_samples()
plt.plot(y, linewidth=0.25)
plt.plot(x, linewidth=0.25)

boost_audio.export("./data/boost_audio.wav", format="wav")

import numpy as np
x = np.linspace(0, 4*np.pi, num=44100*2*2)
y = np.sin(x)
plt.plot(y)
noise = np.random.uniform(-0.3, 0.3, 44100*2*2)
plt.plot(x, y)

y = (np.sin(x) + noise)*2**15

my_sound = AudioSegment(np.int16(y).tobytes(),
                        frame_rate = 44100,
                        sample_width = 2,
                        channels=2)

play(my_sound)

x = audio.get_array_of_samples()
x[:10]
dct = np.fft.fft(x, n = 1000) 
dct  # j는 복소수

dct2 = np.abs(dct)
dct2

fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x)
axes[1].plot(dct2)
axes[0].set_title("Time domain")
axes[1].set_title("Frequency domain")
axes[0].set_xlabel("Time")
axes[1].set_xlabel("Freq") # -> 이걸 가지고 분류한다

gun = AudioSegment.from_file(r"./data\THP - Gun Kit\Gun Sound Effect/ak47-1.wav", format="wav")
knife = AudioSegment.from_file(r"./data\THP - Gun Kit\Gun Sound Effect/knife_hit1.wav", format="wav")
gun_x = gun.get_array_of_samples()
knife_x = knife.get_array_of_samples()
gun_dct = np.abs(np.fft.fft(gun_x, n=1000))
knife_dct = np.abs(np.fft.fft(knife_x, n=1000))

fig,axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(gun_dct)
axes[1].plot(knife_dct)


# 분류알고리즘 -> 로지스틱 회귀로 분류한다
folder = os.listdir("./data/THP - Gun Kit/Gun Sound Effect")
folder

audio_list = []
label_list = []
for file in folder:
    try:
        audio = AudioSegment.from_file(r"./data/THP - Gun Kit/Gun Sound Effect/" + file, format="wav")
        x = audio.get_array_of_samples()
        feature = np.abs(np.fft.fft(x, n=1000))
        audio_list.append(feature)
        label_list.append(file)
    except:
        continue

len(audio_list)
label_list    

import re
import pandas as pd
r = re.compile("[_|-]")
labels = [r.split(s)[0] for s in label_list]

mat = np.vstack(audio_list) # -> 행렬을 만들어준다.
mat.shape
dat = pd.DataFrame(mat)
dat.columns = ["V" + str(i) for i in range(1, 1001)]
dat["labels"] = labels

train_dat = dat.loc[dat.labels.isin(["m4a1", "usp", "knife"]), :].copy()
train_dat["y"] = np.where(train_dat.labels == "knife", 1, 0)
train_dat.y

train_dat.drop(columns = "labels", inplace=True)


from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver = "liblinear", random_state=0)

# 디자인 매트릭스 만들기
X = train_dat.drop(columns = "y").values # -> array로 바꿔준다.
y = train_dat.y.values

fit_res = model.fit(X, y)
pred_y = fit_res.predict(X)

pd.crosstab(y, pred_y) # 실제 0인데 1로 예측한거 1개

