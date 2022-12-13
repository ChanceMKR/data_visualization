import pandas as pd
import numpy as np
import re
import requests
from bs4 import BeautifulSoup
from konlpy.tag import Komoran
import matplotlib.pyplot as plt
import matplotlib
from selenium import webdriver
from PyKomoran import *

matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False


headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
r = requests.get(r"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=104", headers = headers)
r.status_code
html = BeautifulSoup(r.text, "html.parser")
headlines = html.select(r"a.cluster_text_headline")
headlines_text = [s.text for s in headlines]

cleaner = re.compile("\[.*\]") # . : 아무거나  * : 몇번나오든 상관 없이 
clean_text = [cleaner.sub("", s) for s in headlines_text]
len(clean_text)


ko = Komoran()
full_text = ", ".join(clean_text)
words = ko.nouns(full_text) # 굳이 하나하나 for문으로 넣을 필요 없다. -> 문장들을 다 이어붙여서 넣어도 명사뽑는데에는 지장이 없다.
counts = pd.value_counts(words)
counts.loc[counts>=3].plot.bar()


driver = webdriver.Chrome(r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe")
driver.get(r"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=104")
html = BeautifulSoup(driver.page_source, "html.parser")
body = html.select(r"dt > a")
[s.text for s in body]


r = requests.get(r"https://www.sciencekids.co.nz/pictures/flags.html")
r.status_code
html = BeautifulSoup(r.text, "html.parser")
a = html.select(r"td.style54")
a[0].select("img")[0].attrs["src"]

flags_url = [s.select("img")[0].attrs["src"] for s in a if len(s.select("img")) != 0]
flags_url[0]

url = r"https://www.sciencekids.co.nz"
cleaner = re.compile("^[.]{2,}")   # ^는 처음부분, {2,}은 두개까지만 찾기

flags_image = []
for i in range(0, len(flags_url)):
    b = url + cleaner.sub("", flags_url[i])
    rr = requests.get(b)
    img = Image.open(BytesIO(rr.content))
    flags_image.append(img)

flags_image[10].show()
