import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import string

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
    


##############################
strings = ["My", "name", "is", "Seongchan", "Kim"]
" ".join(stringss)
LETTERS = list(string.ascii_uppercase)
letters = list(string.ascii_lowercase) 
list(zip(LETTERS, letters))

["-".join([i, j]) for i, j in zip(LETTERS, letters)]

"afeubauvwebuawfibjdksabhquwevb".count("b")

"KSCKSCKSC".replace("SC", "sc")
"KSC".find("S")


