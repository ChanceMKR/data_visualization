import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

iris = sm.datasets.get_rdataset("iris",
                                "datasets")

iris_dat = iris.data.copy()
iris_dat.head()

n, bins, patches = plt.hist(iris_dat["Sepal.Width"])
n
bins # 구간
patches

n, bins, patches = plt.hist(iris_dat["Sepal.Width"],
                            bins = 31)
# (iris_dat["Sepal.Width"].max() - iris_dat["sepal.Width"].min() / 31

breaks = np.linspace(iris_dat["Sepal.Width"].min(),
                     iris_dat["Sepal.Width"].max(),
                     50)
plt.hist(iris_dat["Sepal.Width"], bins = breaks)

plt.hist(iris_dat["Sepal.Width"],
         density = True) # 넓이의 합이 1이 된다.

grouped_dat = iris_dat.groupby("Species")
list(grouped_dat)

for group, data in grouped_dat:
    plt.hist(data["Sepal.Width"],
             label = group,
             alpha = 0.5)
plt.legend()

iris_dat.hist(column = "Sepal.Width",
              by = "Species")

sns.histplot(data = iris_dat,
             x = "Sepal.Width",
             hue = "Species",
             stat = "probability") # 높이가 확률

sns.histplot(data = iris_dat,
             x = "Sepal.Width",
             hue = "Species",
             stat = "density") # 넓이가 확률



fig = plt.figure()  # 도화지 만들기
# fig.add_subplot(1,1,1)
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
ax1.boxplot(iris_dat["Sepal.Length"])
ax2.hist(iris_dat["Sepal.Width"])
ax3.hist(iris_dat["Petal.Length"])
ax4.plot(iris_dat["Petal.Width"])



fig, axes = plt.subplots(2,2,figsize = (5,5))
axes[0,0].hist(iris_dat["Sepal.Width"])
axes[0,0].legend(["Hi"])
axes[1,1].hist(iris_dat["Petal.Width"])
fig.legend(["Bye"])



fig, axes = plt.subplots(1,2)
axes[0].hist(iris_dat["Sepal.Length"], alpha = 0.5)
axes[0].hist(iris_dat["Sepal.Width"], alpha = 0.5)
axes[1].hist(iris_dat["Petal.Length"], alpha = 0.5)
axes[1].hist(iris_dat["Petal.Width"], alpha = 0.5)
axes[0].legend(["Sepal Length", "Sepal Width"])
axes[1].legend(["Petal Length", "Petal Width"])
fig.legend(["plot1_1", "plot1_2", "plot2_1", "plot2_2"])




fig, axes = plt.subplots(1,1)
axes.hist(iris_dat["Sepal.Length"],
          alpha = 0.5, label = "Sepal.Length")
axes.hist(iris_dat["Sepal.Width"],
          alpha = 0.5, label = "Sepal.Width")
axes.legend(title="IRIS", loc="upper left", fontsize=20, title_fontsize=25)

axes.set_xlabel("Sepal")
axes.set_ylabel("Freq")
axes.set_xlim(0, 10)
axes.set_ylim(0, 100)
axes.set_xticks(ticks = [3, 6], labels = ["a","b"])
axes.tick_params(axis="x", color="red",
                 direction="inout", # in, out
                 length=20, width=3,
                 labelcolor="blue")


