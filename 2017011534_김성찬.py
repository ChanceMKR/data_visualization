import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import os
os.getcwd()
from data_processing.read_data import read_fun
plt.rcParams['font.family'] = 'Malgun Gothic'

# bbbeomjin@gmail.com
# 주석처리

# 문제1번
# 1-1번
data_list = []
path = r"C:\Users\user\Desktop\sc\data_visualization\midterm exam datasets\fine_dust\fine_dust"
file_list = os.listdir(path)

for f in file_list:
    data = pd.read_csv(path +"\\"+ f, header=0)
    data_list.append(data)
    
dust = pd.concat(data_list, axis = 0, ignore_index = True)

dust_dat = dust.sort_values(by = "측정소명",
                 ascending=False)   # 내림차순 정렬
dust_dat = dust_dat.sort_values(by = ["측정일", "측정시간"]) # 오름차순정렬

# 1-2번
dust_dat.loc[dust_dat["PM10"].isna(), "PM10"] = 0  # 결측치 0으로 대체
dust_dat

# 1-3번
dust_dat["구"] = [s.split(" ")[1] for s in dust_dat["주소"]] # 주소를 띄어쓰기로 나누어준 후 두번째 요소를 구 칼럼으로 만들어준다.
group_dat = dust_dat.groupby("구")

for group, dat in group_dat:
    plt.plot(dat["PM10"], label = group)
plt.xlabel("Date")
plt.ylabel("Maximum of PM10")
plt.legend()



group_dat = orange_dat.groupby("Tree")
for group, dat in group_dat:
    plt.hist(dat["circumference"],
             label=group)
plt.legend(loc="center right",
           bbox_to_anchor=(0.5,0.5,1.5,1.5))



# 문제2번
# 2-1
data2 = pd.read_csv(r".\midterm exam datasets\data2.csv")

group_dat = data2.groupby(by=[data2.columns])


data2 = data.groupby(["month", "user_id"]).\
    agg(log_month = ("log_date", lambda x: x.shape[0]),
        pay_month = ("payment", "mean"))



# 문제3번
# 3-1
data3 = pd.read_csv(r"C:\Users\user\Desktop\sc\data_visualization\midterm exam datasets\data4.csv")
# dteday를 날짜형식으로 포맷팅 한다.
data3["dteday"] = pd.to_datetime(data3.dteday,
                                 format = "%Y-%m-%d")
#year데이터 값만 뽑아 새로운 칼럼으로 만들어준다.
data3["year"] = data3.dteday.dt.year

#숫자로 되어있는 날짜 형식을 str형태로 바꾸어준다.
weather = []
for i in data3["weathersit"]:
    if i == 1:
        w = "sunny"
    elif i == 2:
        w = "cloudy"
    elif i == 3:
        w = "drizzly"
    else:
        w = rainy
    weather.append(w)
#바뀐 데이터들을 새로운 칼럼으로 만들어준다.
data3["weather"] = weather

# 연도별 그룹핑
group_dat = data3.groupby(by="year")
# 1개도화지에 2개 차트를 그린다
fig, axes = plt.subplots(1,2)

i = 0
for year, group in group_dat:
    counts = group.weather.value_counts()
    axes[i].pie(counts,
                  labels = counts.index, # label은 날씨로 부여한다
                  autopct = "%.1f%%") # 소수첫째자리 까지 출력한다.
    axes[i].set_title(year) # 연도를 title로 부여한다.
    i+=1



#3-2
data3["month"] = data3.dteday.dt.month
data3.cnt = pd.to_numeric(data3.cnt)
count = data3.groupby(by="month").value_counts()


i = 0
fig, axes = plt.subplots(1,2)
for month, group in count:
    axes[i].bar(count.index, height = count.values)
    axes[i].xlabel = "Month"
    i+=1















