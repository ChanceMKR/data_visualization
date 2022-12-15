import pandas as pd
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
import os
import pydub
from pydub import AudioSegment
from pydub.playback import play
os.getcwd()


raccoon = mpimg.imread(r"./image data analysis data/Raccoon image.jpg")
plt.imshow(raccoon)
plt.axis("off")

img = Image.open("./image data analysis data/Raccoon image.jpg")
img.show()
img.mode
img.size
img.format


logo = Image.open(r"./image data analysis data/python_logo.png")
img.paste(logo)
img.show()

img.convert("L").show()


audio = AudioSegment.from_file("./data/metallic-beat-short/metallic-beat-short.wav", format="wav")
audio.frame_rate
audio.sample_width
x = audio.get_array_of_samples()


dct = np.abs(np.fft.fft(x, n = 1000))
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x)
axes[1].plot(dct)


gun = AudioSegment.from_file(r"./data/THP - Gun Kit/Gun Sound Effect/ak47-1.wav", format="wav")
knife = AudioSegment.from_file(r"./data/THP - Gun Kit/Gun Sound Effect/ak47-1.wav", format="wav")
gun_x = gun.get_array_of_samples()
knife_x = knife.get_array_of_samples()
gun_dct = np.abs(np.fft.fft(gun_x, n=1000))
knife_dct = np.abs(np.fft.fft(knife_x, n=1000))

fig,axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(gun_dct)
axes[1].plot(knife_dct)

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
    
label_list

r = re.compile("[_|-]")
labels = [r.split(s)[0] for s in label_list]

mat = np.vstack(audio_list)
mat.shape
dat = pd.DataFrame(mat)
dat.columns = ["V" + str(i) for i in range(1, 1001)]
dat["labels"] = labels
