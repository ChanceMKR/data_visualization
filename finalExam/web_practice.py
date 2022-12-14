import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from konlpy.tag import Komoran
import string
from PIL import Image
import io

matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False


headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

r = requests.get(r"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100", headers = headers)
r.status_code
html = r.text
soup = BeautifulSoup(html, 'html.parser', from_encoding="cp949")

for s in soup.select(r"span.tx"):
    print(s.text)
    

r = requests.get(r"https://comic.naver.com/webtoon/weekday")
r.status_code
html = BeautifulSoup(r.text, "html.parser")
html.select(r"a.title")[4].text


r = requests.get(r"https://www.youtube.com/watch?v=Wdpw6idowII")
r.status_code
BeautifulSoup(r.text, "html.parser")


r = requests.get(r"https://comic.naver.com/webtoon/weekday")
r.status_code
html = BeautifulSoup(r.text, "html.parser")
a = html.select(r"div.thumb>a>img")
a[4].attrs["src"]

    
thumb_image = []
for i in a:
    url = i.attrs["src"]
    img = Image.open(io.BytesIO(requests.get(url).content))
    thumb_image.append(img)
    
thumb_image[4].show()
    

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

r = requests.get(r"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=104", headers = headers)
r.status_code
html = BeautifulSoup(r.text, "html.parser")
headlines = html.select("a.cluster_text_headline")
headlines_text = [s.text for s in headlines]
cleaner = re.compile("\[.*\]|'")
clean_text = [cleaner.sub("", s).strip() for s in headlines_text]
