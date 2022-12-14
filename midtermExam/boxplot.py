import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


usa = sm.datasets.get_rdataset("usa_states",
                               "stevedata")

usa_states = usa.data.copy()

counts = usa_states.region.value_counts()

x = np.random.randn(100)
plt.boxplot(x)

# 이상치는 모델링을 한 이후에 이상치를 제거해야한다.

iris = sm.datasets.get_rdataset("iris",
                                "datasets")
iris_dat = iris.data.copy()
plt.boxplot(iris_dat.drop(columns = "Species"))
# 박스가 높으면 데이터가 많이 퍼져있는 것이다.(분산)
# boxplot에서 box 높이가 겹치면 연관성이 있을 수 있다.

box = plt.boxplot(iris_dat.drop(columns = "Species"),
            vert = False)

box
# whiskers : 수염
# caps : 최대치
# boxex : 박스
# median : 주황선
# fliers : 이상치

box = iris_dat.boxplot(column = ["Sepal.Length",
                           "Petal.Length"],
                 by = "Species",
                 patch_artist = True,
                 return_type = "dict")
color = ["red", "blue", "green"]

list(box.iteritems())

for var, dic in box.iteritems():
    for b, color in zip(dic["boxes"], color):
        b.set_facecolor(color)
        
iris_dat.head()
iris_melt = iris_dat.melt(id_vars = "Species") # wide 폼을 long폼으로 바꾸어준다.
sns.boxplot(data = iris_melt,
            x = "variable",
            y = "value",
            hue = "Species")
