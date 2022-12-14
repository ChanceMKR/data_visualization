import pandas as pd
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
import os
os.getcwd()


raccoon = mpimg.imread(r"./image data analysis data/Raccoon image.jpg")
plt.imshow(raccoon)
plt.axis("off")

img = Image.open("./image data analysis data/Raccoon image.jpg")
img.show()
img.mode
img.size
img.format


logo = Image.open(r"./image data analysis data/python_logo.png")
img.paste(logo)
img.show()

img.convert("L").show()