import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.api as sm

mtcars = sm.datasets.get_rdataset("mtcars", "datasets").data.copy()

fig = plt.figure()
axes = fig.add_subplot(111, projection = "3d")
# fig, axes = plt.subplots(1,1,
#                     subplot_kw = dict(projection = "3d"))

axes.scatter(mtcars.wt, 
             mtcars.disp, 
             mtcars.mpg,
             depthshade = False)

axes.scatter(mtcars.wt, 
             mtcars.disp, 
             zs =  mtcars.mpg.min(), # 특정축 고정
             zdir = "z",
             depthshade = False,
             alpha = 0.3)


axes.scatter(mtcars.wt, 
             mtcars.mpg, 
             zs =  mtcars.disp.max(), # 특정축 고정
             zdir = "y",
             depthshade = False,
             alpha = 0.3)

axes.scatter(mtcars.disp, 
             mtcars.mpg, 
             zs =  mtcars.wt.min(), # 특정축 고정
             zdir = "x",
             depthshade = False,
             alpha = 0.3)

axes.set_xlim([mtcars.wt.min(), 
               mtcars.wt.max()])
axes.set_ylim([mtcars.disp.min(),
               mtcars.disp.max()])
axes.set_zlim([mtcars.mpg.min(),
               mtcars.mpg.max()])

axes.set_xlabel("wt")
axes.set_ylabel("disp")
axes.set_zlabel("mpg")

axes.view_init(0, 45) # 각도조절


x = y = np.linspace(-4*np.pi, 4*np.pi, 50)
z = x**2 + y**2    
fig = plt.figure()
axes = fig.add_subplot(111, projection = "3d")
axes.plot(x, y, z)

volcano = sm.datasets.get_rdataset("volcano", 
                          "datasets").data.copy()

x = np.arange(1, volcano.shape[0] + 1)
y = np.arange(1, volcano.shape[0] + 1)
xx, yy = np.meshgrid(x, y)

fig = plt.figure()
axes = fig.add_subplot(111, projection = "3d")
axes.plot_surface(xx.T, yy.T, volcano.values)



import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"

mtcars.cyl = pd.Categorical(mtcars.cyl)
fig = px.scatter(data_frame = mtcars,
           x = "wt", y = "mpg",
           color = "cyl", symbol="cyl")
fig.show()


