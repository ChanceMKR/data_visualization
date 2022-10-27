import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import random
os.getcwd()

mtcars = sm.datasets.get_rdataset("mtcars", "datasets")
mtcars_dat = mtcars.data.copy()
mtcars_dat["company"] = [s.split(" ")[0] for s in mtcars_dat.index]


orange = sm.datasets.get_rdataset("Orange")
orange_dat = orange.data.copy()
orange_dat.head()


plt.hist(x=orange_dat["circumference"], bins=10)
plt.hist(orange_dat["circumference"])

group_dat = orange_dat.groupby("Tree")
for group, dat in group_dat:
    plt.hist(dat["circumference"],
             label=group)
plt.legend(loc="center right",
           bbox_to_anchor=(0.5,0.5,1.5,1.5))

mtcars_dat
sns.barplot(x = "company", y = "cyl", hue = "variable", data = mtcars_dat)
sns.barplot(x = "Tree", y = "circumference", hue = "age", data = orange_dat)
sns.barplot(x = "age", y = "circumference", hue = "Tree", data = orange_dat)



plt.plot(orange_dat["age"],
         orange_dat["circumference"], "o")

plt.scatter(orange_dat["age"],
            orange_dat["circumference"], 
            c=orange_dat["Tree"], 
            cmap="plasma")

orange_dat.plot.scatter(x="age",
                        y="circumference",
                        c=orange_dat["Tree"],
                        cmap="viridis")

sns.scatterplot(data = orange_dat,
                x = "age",
                y = "circumference",
                hue = "Tree",
                s = orange_dat.circumference*0.5)

fig, ax = plt.subplots()
orange_dat.plot.scatter(x = "age",
                        y = "circumference", ax = ax)

sns.pairplot(data = orange_dat[["age", "circumference", "Tree"]])

sns.pairplot(data = orange_dat,
             vars = ["age", "circumference", "Tree"],
             hue = "Tree",
             # 대각원소 교체
             diag_kind = "kde",
             # 상삼각제거
             corner = True)


mtcars = sm.datasets.get_rdataset("mtcars", "datasets").data.copy()

fig = plt.figure()
axes = fig.add_subplot(111, projection = "3d")


axes.scatter(mtcars.wt, 
             mtcars.disp, 
             mtcars.mpg,
             depthshade = False)


plt.scatter(orange_dat.age, orange_dat.circumference)
x = orange_dat.age
y = orange_dat.circumference
X = sm.add_constant(x)
linear_model = sm.OLS(y, X)
res = linear_model.fit()
res.summary()
