import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import pi


x = np.linspace(0, 2*pi , 30)
y = np.sin(x)
y2 = np.cos(x)


# 산점도
plt.plot(x, y, "o")
plt.plot(x, y2, "o")
plt.plot(x,y,"o", x, y2, "o")
plt.plot(x,y,"-", x, y2, "x")
plt.plot(x,y,"or", x, y2, ".")
plt.plot(x,y,",", x, y2, "--")
plt.plot(x,y,"|", x, y2, "o-")
#plt.plot(x, y, "o-o")


plt.scatter(x,y)

plt.scatter(x,y,c = "#DAF7A6")
plt.scatter(x,y,s = 100)

dat = pd.DataFrame({"x" : x,
                    "y1" : y,
                    "y2" : y2})

# fig 도화지,  ax 축
fig, ax = plt.subplots()

dat.plot.scatter(x = "x",
                 y = "y1", ax = ax)
dat.plot.scatter(x = "x",
                 y = "y2", ax = ax)

import statsmodels.api as sm
mtcars = sm.datasets.get_rdataset("mtcars",
                                  "datasets",
                                  cache = True)

print(mtcars.__doc__)
mtcars_data = mtcars.data.copy()
mtcars_data.head()
mtcars_data.tail()

plt.plot(mtcars_data["mpg"],
         mtcars_data["disp"],
         "o")

plt.scatter(mtcars_data["mpg"],
            mtcars_data["disp"])

plt.scatter(mtcars_data["mpg"],
            mtcars_data["disp"])
plt.xlabel("mpg")
plt.ylabel("disp")
plt.title("Scatter Plot")

mtcars_data.plot.scatter(x = "mpg",
                         y = "disp",
                         title = "Scatter plot")

mtcars_data.head()
mtcars_data.Index

mtcars_data["company"] = [s.split(" ")[0] for s in mtcars_data.index]
mtcars_data.head()

group_data = mtcars_data.groupby("company")

for name, group in group_data:
    plt.plot(group.mpg, group.disp, "o",
             label = name)
    plt.xlabel("mpg")
    plt.ylabel("disp")
plt.legend(loc = "upper right",
           #bbox_to_anchor x위치, y위치, 넓이, 높이 -> 시험
           bbox_to_anchor = (0, 1, 10, 12))

mtcars_data.plot.scatter(x = "mpg", 
                         y = "disp",
                         # c 색깔 -> categorical 변수로 처리를 해주어야 한다.
                         c = "company" )

mtcars_data2 = mtcars_data.copy()
mtcars_data2["company"] = pd.Categorical(mtcars_data2["company"])

mtcars_data2.plot.scatter(x = "mpg", 
                          y = "disp",
                          # c 색깔 -> categorical 변수로 처리를 해주어야 한다.
                          c = "company",
                          cmap = "viridis")

viridis = plt.get_cmap("viridis")
viridis(0)
len(viridis.colors)


sns.scatterplot(data = mtcars_data2,
                x = "mpg",
                y = "disp",
                # hue 색상부여
                hue = "company",
                # s 크기
                s=400)

sns.scatterplot(data = mtcars_data2,
                x = "mpg",
                y = "disp",
                # hue 색상부여
                hue = "company",
                # s 크기
                s=mtcars_data2.wt*100)

mtcars_data2.iloc[0, :]

# pairplot 변수별 산점도 출력
sns.pairplot(mtcars_data2[["mpg", "cyl", "disp", "hp", "drat"]])
sns.pairplot(data = mtcars_data,
             vars = ["mpg", "cyl", "disp"],
             hue = "company",
             # 대각원소 교체
             diag_kind = "kde",
             # 상삼각제거
             corner = True)




