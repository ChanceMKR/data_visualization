import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
import os
os.chdir("/Users/chance/Desktop/Coding/data_visualization")
os.getcwd()
state_region = sm.datasets.get_rdataset("usa_states",
                                        "stevedata")
state = state_region.data.copy()
count = state.region.value_counts()
plt.bar(x = count.index,
        height = count.values,
        color = ["black", "red", "green", "blue"])
plt.ylabel("Freq")
#plt.xticks(ticks = range(0, 4),
#           labels = [s.lower() for s in count.index])
count.plot.bar(y = "region",
               color = ["black", "red", "green", "blue"])

mtcars = sm.datasets.get_rdataset("mtcars",
                                  "datasets",
                                  cache = False)
mtcars_dat = mtcars.data.copy()
mtcars_dat.head()
mtcars_dat["company"] = [s.split()[0] for s in mtcars_dat.index]
mtcars_dat.groupby("company")[["cyl", "wt"]].mean().plot.bar(subplots=True, rot=45)
mtcars_dat.groupby("company")["cyl"].median().plot.bar(rot = 45)


sns.barplot(x = "index", y = "region", data = count.reset_index(drop = False))

count.reset_index(drop=False)
group_dat = mtcars_dat.groupby("company")[["cyl", "wt"]].mean()
sns.barplot(data = group_dat, ci = None)

barplot_dat = group_dat.reset_index(drop=False).melt(id_vars = "company")
sns.barplot()(x = "company", 
              y = "value",
              hue = "variable",
              data = barplot_dat)


iris = sm.datasets.get_rdataset("iris", "datasets", cache = False)
iris_dat = iris.data.copy()
iris_melt = iris_dat.melt(id_vars = "Species")
sns.barplot(x = "variable",
            y = "value",
            hue = "Species",
            data = iris_melt)

sns.barplot(x = "variable",
            y = "value",
            hue = "Species",
            ci = 95,
            data = iris_melt)