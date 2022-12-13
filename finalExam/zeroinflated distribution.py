# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:04:49 2022

@author: user
"""

import os
import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\user\Downloads\dau_dpu.csv")


pay_count = data.groupby(["user_id", "month"]).\
        payment.apply(lambda x: np.sum(x>0)).reset_index(drop = False)

pay_count.head()
data.payment

pay_count.groupby("month").payment.mean()
#100달에 두 번 결제

pay_count
np.sum(pay_count.payment !=0) / len(pay_count.payment) #결제를 한 비율
np.sum(pay_count.payment ==0) / len(pay_count.payment) #결제를 아예 안하는 사람의 비율

#결제를 절대 안하는 사람과 어떤 요인(그 달에 돈이 없어서?) 때문에 결제를 안하는 사람들에 차이를 둬야 함.

#zero inflated distribution 두 가지 분포가 혼합됨.

from scipy.stats import poisson

pay5 = pay_count.loc[pay_count.month == 5, "payment"]
#5월달의 결제 횟수
#포아송
poi_x = np.arange(0, pay5.max())
hist = pay5.plot.hist(bins = poi_x, density = True)  #데이터 프레임에서 히스토그램 그리기 / bins : 구간 / density :확률,비율로)
#이론적인 분포
poi_y = poisson.pmf(poi_x, pay5.mean()) #포아송 할 때 표본평균
hist.plot(poi_x + 0.5, poi_y) #+0.5하는 이유는 0~1 사이 막대의 중간에 그리기 위해서


import statsmodels.api as sm

zeroinf = sm.ZeroInflatedPoisson(pay5.values, 
                       np.ones([pay5.shape[0],1]),
                       exog_inf1=np.ones([pay5.shape[0],1])).fit()    #회귀모형에서 절편값으로 기댓값구하면 와이바

zeroinf.summary()
#inflate_const 파이에 대한 계수, const : 람다에 대한 계수

np.exp(zeroinf.params[0] / (1+np.exp(zeroinf.params[0])))
np.exp(zeroinf.params[1]) #포아송 분포에서의 평균
# => 전체 데이터에서는 100달에 2번 결제하지만, 결제를 하는 사람만 놓고 봤을 때 1달에 3~4번 결제함

def zeroinf_poi(x, mu, prob) :
    y = prob * (x==0) + (1 - prob) * poisson.pmf(x, mu = mu)
    #x가 0인 애들중에 zerostate에 들어갈 확률 + (zerostate에 들어가지 않은 사람 확률) * 포아송 모수
    return(y)

poi_y = map(lambda x: zeroinf_poi(x = x, mu = np.exp(zeroinf.params[1]), prob = np.exp(zeroinf.params[0]) / (1 + np.exp(zeroinf.params[0]))), poi_x)
poi_yy = list(poi_y)
hist = pay5.plot.hist(bins = poi_x, density = True)
hist.plot(poi_x + 0.5, poi_yy)

