import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import re
import requests
import string
from PIL import Image
import cv2
import matplotlib.image as mpimg
import matplotlib.dates as mdates
from sklearn.cluster import KMeans
from bs4 import BeautifulSoup
from konlpy.tag import Komoran
from selenium import webdriver
import io
import pydub
from pydub import AudioSegment
from pydub.playback import play
import random

os.getcwd()

matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }


# 1번

audio = AudioSegment.from_file(r"C:\Users\user\Desktop\sc\data_visualization\finalExam\기말고사 데이터\audio\spring\Your Love.mp3", format="mp3")
audio.frame_rate
x = audio.get_array_of_samples()
x


dct = np.abs(np.fft.fft(x, n=1000))
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x)
axes[1].plot(dct)
axes[0].set_xlabel("Time domain")
axes[1].set_xlabel("Frequency domain")




# 2번

random.sample(os.listdir(r"C:\Users\user\Desktop\sc\data_visualization\finalExam\기말고사 데이터\audio/winter"), 1)

def function1(path, season):
    path1 = random.sample(os.listdir(path + "/" + season), 1)
    audio = AudioSegment.from_file(path + "/" + season + "/" + path1[0])
    x = audio.get_array_of_samples()
    dct = np.abs(np.fft.fft(x, n=1000))
    axes[0].plot(x)
    axes[1].plot(dct)
    axes[0].set_xlabel("Time domain")
    axes[1].set_xlabel("Frequency domain")
    
function1(path = r"C:\Users\user\Desktop\sc\data_visualization\finalExam\기말고사 데이터\audio", season = "winter")


# 3번
img = Image.open(r"C:\Users\user\Desktop\sc\data_visualization\finalExam\기말고사 데이터\image/이상한 나라의 수학자.jpg")
kernel = np.array([[0,-1,0],
                   [-1,4,-1],
                   [0,-1,0]])
img_data = np.array(img)
out = cv2.filter2D(img_data, -1, kernel)
out_img = Image.fromarray(out)
out_img.show()


# 4번
def po(dt):
    r = requests.get(r"https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&tg=0&date=202212{date}".format(date=dt))
    r.status_code
    html = BeautifulSoup(r.text, "html.parser")
    tit = html.select(r"div.tit5>a")
    tit_list = [t.text for t in tit]
    point = html.select(r"td.point")
    point_list = [float(p.text) for p in point]
    data = pd.DataFrame(zip(tit_list, point_list))
    return data

data10 = po(10)
data11 = po(11)

data = pd.merge(data10, data11, how="inner", on=0)
data["point"] =( data["1_x"] + data["1_y"])/2

# 5번
strings = "Chunsoo : chulsoo1234@naver.com, Younghee ; YH0516@gnu.ac.kr, Beomjin;bjpark@gmail.co.kr, Sion : goat1312@hanmail.net"
z = re.compile(
    '''
    ([a-zA-Z]+)
    \s*[:;]\s*
    ([a-zA-Z0-9]+@[a-z]+.[a-z]*.[a-z]*)+,*

    ''', re.VERBOSE)

a = z.findall(strings)
pd.DataFrame(a, columns = ["name", "email"])
