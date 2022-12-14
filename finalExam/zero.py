import pandas as pd
import numpy as np
import os
os.getcwd()

#과금 안한 유져들 payment = 0으로 처리까지 한 데이터
data = pd.read_csv(r"./data/dau_dpu.csv")
data.head()

#유져별 월별 payment > 0보다 큰 사람들
pay_count = data.groupby(["user_id", "month"]).payment.apply(lambda x: np.sum(x > 0)).reset_index(drop = False)

# user : 독립 / 월별(단위시간당) 분포 : 포아송분포를 따름
pay_count.groupby("month").payment.mean()

#확률적으로 0이 나오는 분포 : 포아송분포
#절대적으로 payment가 0 과 가끔 payment != 0 을 구분하는 분포 : zero-inflated
# >> mixture distribution

np.sum(pay_count.payment != 0)

from scipy.stats import poisson

#5월달만
pay5 = pay_count.loc[pay_count.month == 5, "payment"]

#x축 생성 : poisson은 무한대까지이나, 필요한 값은 pay5.max()까지
poi_x = np.arange(0, pay5.max())

#bins = 갯수지만, density = True를 주면 비율로 나타남
hist = pay5.plot.hist(bins = poi_x, density = True)
#0이 너무 많아서 다른분포가 잘 보이지도 않음

#각 0, 1, 2, 3,,,들의 확률들
poi_y = poisson.pmf(poi_x, pay5.mean())

#막대의 중간에 점을 찍고 선을 긋기 위해 +0.5
#같이 그림 : 선과 막대가 약간 안맞음
hist = pay5.plot.hist(bins = poi_x, density = True)
hist.plot(poi_x + 0.5, poi_y)

import statsmodels.api as sm

#원래 Regression에 쓰나, Regression에 절편만 있으면 평균 추정
#np.ones = 설명변수 / 
zeroinf = sm.ZeroInflatedPoisson(pay5.values,
                       np.ones([pay5.shape[0], 1]),
                       exog_infl = np.ones([pay5.shape[0], 1])).fit()

zeroinf.summary()
#inflate = pie의 추정 (0 ~ 1 범위인데도 5가 넘음)
#const = 1-pie * P(x)의 추정

#pie의 값
np.exp(zeroinf.params[0]) / (1 + np.exp(zeroinf.params[0]))

#절대적인 0을 제외한 값
np.exp(zeroinf.params[1])


#y = zeroState에 들어갈 확률:prob*(x==0) + 약간의 확률이 있는:(1-prob)* ,,,
def zeroinf_poi(x, mu, prob):
    y = prob * (x == 0) + (1 - prob) * poisson.pmf(x, mu = mu)
    return(y)

#x에 0, 1, 2, 3 ,,, 넣어야함 > for문사용 가능
#더 쉽게 map(for문 같은것)
poi_y = map(lambda x: zeroinf_poi(x = x,
                                  mu = np.exp(zeroinf.params[1]),
                                  prob = np.exp(zeroinf.params[0]) / (1 + np.exp(zeroinf.params[0]))),
            poi_x)

#원소들 보고싶으면 list
poi_yy = list(poi_y)

hist = pay5.plot.hist(bins = poi_x, density = True)
hist.plot(poi_x + 0.5, poi_yy)

#############################################################################

skill = pd.read_csv(r"C:\Users\user\Desktop\Data\SkillCraft1_Dataset.csv")
skill.head()

#생략된 부분을 더 많이 보여줌
pd.set_option("display.max_columns", 18)
skill.head()

#데이터가 없는 부분을 ?처리 해놨음
#행별로 ?가 하나라도 있으면 삭제
skill_c = skill.loc[~(skill == "?").any(axis = 1)]

skill_c["age_g"] = 10
#이상한 Warning message가 뜸

df = pd.DataFrame(np.array([[5, 0, 3, 3, 7],
                            [9, 3, 5, 2, 4],
                            [7, 6, 8, 8, 1]]),
                  columns = ["A", "B", "C", "D", "E"])

# df.A의 > 5 변수들의 A를 뽑아 1000으로 변경시킬 것임
df[df.A > 5]["A"] = 1000
# Warning message만 뜨고, 실행은 됐으나 값이 변하지 않음

df.loc[df.A > 5]["A"] = 1000
#안됨

#chain indexing 먼저 df.A > 5를 뽑고, A부분을 할당
#다음 명령과 같음
df.__getitem__(df.A > 5).__setitem__("A", 1000)

#df.loc[df.A > 5] == __getitem__ / ["A"] = 1000 == __setitem__
df.loc.__getitem__(df.A > 5).__setitem__("A", 1000)

#view와 copy의 문제
#view = 보여주고 값을 변경 >> 반영시킴
#copy = 복제품을 만들고 수정 >> 코드끝나면 복제품을 날려버림
#무엇이 copy고 무엇이 view인지 개발자도 모름

#chain indexing을 안하면 됨
df.loc[df.A > 5, "A"] = 1000

#또는, copy()를 통해 메모리에 똑같은 녀석을 복제 후 사용
df_temp = df[df.A > 5].copy()
df_temp["A"] = 1000
df_temp

##########################################################################












