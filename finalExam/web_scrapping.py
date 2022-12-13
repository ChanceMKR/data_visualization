# 1122
# web scraping
import os 
os.chdir(r"C:\Users\user\Desktop\sc\data_visualization")
import requests
r = requests.get('https://github.com/bbeomjin')
r.status_code ## 200이라고 나오면 제대로 된 것
html = r.text
print(html)

import re
remove_escape = re.compile(r'\r|\n|\t')
html_clean = remove_escape.sub(' ', html)

z = re.findall('<(div class="p-note user-profile)([^>]+)>', html_clean)
from bs4 import BeautifulSoup
r = requests.get('https://github.com/bbeomjin')
html = r.text
soup = BeautifulSoup(html, 'html.parser')

# soup.find_all("div", attrs= {"class":"user-profile-bio"})
soup.find_all("div", attrs= {"class":"p-note"})
repos = soup.find_all("span", attrs= {"class":"repo"})
repos[0].text
repos[0].contents
[s.text for s in repos]

# attribute가 class일때만 가능 ( tag.class > 하위 tag)
soup.select(r"div.user-profile-bio > div")[0].text
soup.select(r"span.repo")
soup.select(r"div.p-note > div")[0].text


r = requests.get(r"https://finance.naver.com/marketindex/")
r.status_code

html = r.text
soup = BeautifulSoup(html, "html.parser")
value = soup.select(r"span.value")
names = soup.select(r"h3.h_lst > span.blind")
changes = soup.select(r"span.change")
rise_fall = soup.select(r"div.head_info > span.blind")

len(value)
value[0].text
values = [float(re.sub(r",", "", s.text)) for s in value]
names = [s.text for s in names]
# [float(s.text) for s in changes]
changes = [-float(c.text)if rf.text == "하락" else float(c.text)  for c, rf in zip(changes, rise_fall)]

import pandas as pd
import numpy as np
market_index = pd.DataFrame({"name" : names,
                             "values" : values,
                             "changes" : changes})
dat_list=[]
for i in range(1, 60):
    r = requests.get(r"https://finance.naver.com/sise/sise_index_time.naver?code=KPI200&thistime=20221124145200&page={page}".format(page=i))
    r.status_code
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    value = soup.select(r"td.number_1")
    date = soup.select(r"td.date")
    dates = [s.text for s in date]
    values = [re.sub(",", "", s.text) for s in value]
    values_mat = np.array(values).reshape(-1, 4)
    temp = np.concatenate([np.array(dates)[:, None], values_mat], axis=1)
    temp_dat = pd.DataFrame(temp, columns = ["date", "close", "variance", "volume", "price"])
    dat_list.append(temp_dat)
    
data = pd.concat(dat_list, axis = 0, ignore_index=True) # 행결합
data2 = data.loc[~(data == u"\xa0").all(axis=1), :].copy()# .c
data2["date"] = "2022-11-24 " + data2.date
data2["date"] = pd.to_datetime(data2.date, format = "%Y-%m-%d %H:%M")
data2.loc[:, data2.columns != "date"]
data2.head()

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
hm = mdates.DateFormatter("%H:%M")

fig, axes = plt.subplots(1, 1)
axes.plot(data2.date, data2.close)
axes.xaxis.set_major_formatter(hm)


#r = requests.get(r"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=103")  # 에러 발생한다.
r = requests.get("https://google.com")

# 웹브라우저에서 접속하는 것처럼 만들기
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

r = requests.get(r"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=104", headers = headers)
r.status_code
html = BeautifulSoup(r.text, "html.parser")
headlines = html.select("a.cluster_text_headline")
headlines[0]

headlines_text = [s.text for s in headlines]

import re

headlines_text[-1]
cleaner = re.compile("\[.*\]") # . : 아무거나  * : 몇번나오든 상관 없이 
clean_text = [cleaner.sub("", s) for s in headlines_text]  # 대괄호 안에 있는 모든 글자를 찾아서 ""로 대체한다.

