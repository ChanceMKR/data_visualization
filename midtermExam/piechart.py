# t-test 
# 1. 정규붙포를 따라야한다.
# 2. 비모수검정

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

usa = sm.datasets.get_rdataset("usa_states",
                               "stevedata")

usa_states = usa.data.copy()

counts = usa_states.region.value_counts()
pie = plt.pie(counts,
        labels = counts.index,
        autopct = "%.1f%%",
        shadow = True,
        explode = [0.2, 0, 0, 0])
pie[0][0].set_color("#FFFFFF")
pie[0][0].set_edgecolor("#000000")

counts.plot.pie(autopct = "%.1f%%",
                shadow = True,
                explode = [0.2]*4)
