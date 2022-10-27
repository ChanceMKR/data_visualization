import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
import os
pio.renderers.default = "browser"
now = os.getcwd()
os.chdir(now)
passengers = pd.read_csv("./data/AirPassengers.csv",
                         header = 0)
passengers.head()
passengers.tail()
passengers["cumsum"] = passengers.Passengers.cumsum()/50 #cumsum : 누적합
passengers.Month = pd.to_datetime(passengers.Month,
                                  format = "%Y-%m")
# format
# %Y%m%d -> 20221013 Y:4자리년도
# %Y-%m-%d
# %Y/%m/%d -> 2022-10-13

passengers.Month.dt.weekday
passengers.Month.dt.month


passengers_melt = passengers.melt(id_vars = "Month") #wide form -> long form
fig = px.line(passengers_melt,
              x = "Month",
              y = "value",
              color = "variable")
fig.show()


import statsmodels.api as sm
mtcars = sm.datasets.get_rdataset("mtcars",
                                  "datasets").data.copy()
mtcars.cyl = pd.Categorical(mtcars.cyl)
fig = px.scatter_3d(mtcars,
                    x = "wt",
                    y = "disp",
                    z = "mpg",
                    color = "cyl",
                    symbol = "cyl")
fig.show()


volcano = sm.datasets.get_rdataset("volcano",
                                   "datasets").data.copy()
import plotly.graph_objects as go
x = np.arange(1, volcano.shape[0] + 1)
y = np.arange(1, volcano.shape[0] + 1)
y1 = np.arange(2, volcano.shape[0] + 2)

obj = go.Surface(x = x, y = y, z = volcano.values)
fig = go.Figure(data = obj)
fig.show()

px.scatter()

obj1 = go.Scatter(x=x, y=y, mode = "markers")
obj2 = go.Scatter(x=x, y=y1, mode = "markers")
fig = go.Figure(data = [obj1, obj2])
fig.show()

simulation = pd.read_csv("./data/Simulation data.csv")
simulation.head()

scatter = go.Scatter3d(x = simulation.x1,
                       y = simulation.x2,
                       z = simulation.y,
                       mode = "markers", size = 1)
fig = go.Figure(data = scatter)
fig.show()

X1 = sm.add_constant(simulation["x1"])
lm1 = sm.OLS(simulation.y, X1)
lm1.fit().summary()

X2 = sm.add_constant(simulation["x2"])
lm2 = sm.OLS(simulation.y, X2)
lm2.fit().summary()

X = sm.add_constant(simulation[["x1", "x2"]])
lm = sm.OLS(simulation.y, X)
lm.fit().summary()




