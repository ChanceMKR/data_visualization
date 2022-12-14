# t-test 
# 1. 정규붙포를 따라야한다.
# 2. 비모수검정

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import searborn as sns
import statsmodels.api as sm

usa = sm.datasets.get_rdataset("usa_states",
                               "stevedata")

usa_states = usa.data.copy()

counts = usa_states.region.value_counts()
plt.pie(counts,
        labels = counts.index,
        autopct = "%.1f%%",
        shadow = True,
        explode = [0.2, 0, 0, 0])

