import pandas as pd
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
os.getcwd()

raccoon = mpimg.imread(r"./image data analysis data/Raccoon image.jpg")
plt.imshow(raccoon)
plt.axis("off")

img = Image.open("./image data analysis data/Raccoon image.jpg")
img.show()
logo = Image.open(r"./image data analysis data/python_logo.png")

img.paste(logo)
img.show()

kernels = np.array([[0,-1,0],
                   [-1,4,-1],
                   [0,-1,0]])