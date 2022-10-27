import os 
import numpy as np
os.chdir("/Users/chance/Desktop/Coding/data_visualization")

from data_processing.read_data import read_fun

dau = read_fun(path = "./data/game_user_data",
               folder = "dau",
               subfolder = "game-01")


dpu = read_fun(path = "./data/game_user_data",
               folder = "dpu",
               subfolder = "game-01")

dau.head()
dau.tail()
dpu.head()


import pandas as pd
data = pd.merge(dau, dpu, 
      on = ["log_date", "app_name", "user_id"],
      how = "left")
data.loc[data.payment.isna(), "payment"] = 0 # 구매 NAN을 0으로 대체
data.log_date
len(data.user_id.unique()) # 한번이라도 접속한 유저수

data["log_date"] = pd.to_datetime(data.log_date,
                                  format = "%Y-%m-%d")
data["month"] = data.log_date.dt.month 

#월별 접속 유저수
data.groupby("month").apply( # groupby 한 애들을 apply를 통해서 x에 집어넣는다.
    lambda x: len(x.user_id.unique())
    )
data.groupby("month").payment.mean() # 월별 구매액 평균
data.groupby("month").payment.max() # 월별 구매액 최대치 
data.groupby("month").payment.agg(avg = "mean",
                                  maximum = "max") # 한번에 보기

# 유저별로 각 달마다 결제한 금액
# agg 집계함수
data2 = data.groupby(["month", "user_id"]).\
    agg(log_month = ("log_date", lambda x: x.shape[0]),
        pay_month = ("payment", "mean"))
    
data2.reset_index(drop = False, inplace = True)    

log_vs_pay = data2.groupby("user_id").\
    agg({"log_month" : 
             lambda x : str(np.where((x > 15).all(), "high", np.where((x > 10).all(), "mid", "low"))),
         "pay_month":
             lambda x : str(np.where((x > 100).any(), "high", np.where((x > 50).any(), "mid", "low")))})
        
pd.crosstab(log_vs_pay.log_month,
            log_vs_pay.log_month)
