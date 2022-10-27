#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:09:30 2022

@author: chance
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

x = np.linspace(0, 2*np.pi, 30)
y = np.cos(x)
plt.plot(x, y)
plt.axhline(y=0, xmin=0.5, xmax=1,
            linestyle="dotted")
plt.axvline(x=3, linestyle="solid")


mtcars = sm.datasets.get_rdataset("mtcars",
                                  "datasets")

mtcars_dat = mtcars.data.copy()

plt.scatter(mtcars_dat.mpg, mtcars_dat.disp)

x = mtcars_dat["mpg"]
y = mtcars_dat["disp"]
X = sm.add_constant(x)
linear_model = sm.OLS(y, X)

res = linear_model.fit()
res.summary()

plt.scatter(mtcars_dat.mpg, mtcars_dat.disp)
plt.axline((0, res.params[0]),
           slope = res.params[1],
           c = "red")
# 회귀직선은 조건부기대값을 예측한 것이다.
#res.params.round(1)
plt.title("intercept:{}, slope:{}".format(res.params[0], res.params[1]))

state_region = sm.datasets.get_rdataset('usa_states', 'stevedata')
state = state_region.data.copy()

state.head()

state.region.value_counts()
count = state.region.value_counts()
plt.bar(x = count.index,
        height = count.values,
        color = ["black", "red", "green", "blue"])
plt.ylabel("Freq")

count.plot.bar(y="region",
               color=["black", "red", "green", "blue"])

mtcars_dat[["cyl", "wt"]]
mtcars_dat["company"] = [s.split(" ")[0] for s in mtcars_dat.index]
mtcars_dat.company

mtcars_dat.groupby("company")[["cyl", "wt"]].mean().plot.bar()
