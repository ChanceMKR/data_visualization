import pandas as pd
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
import cv2
from sklearn.cluster import KMeans

import os

os.getcwd()

raccoon = mpimg.imread(r"./image data analysis data/Raccoon image.jpg")

plt.imshow(raccoon)
# plt.plot([1000, 1500], [1000, 1200])
plt.axis("off")

raccoon.shape
fig, axes = plt.subplots(1 ,3)
for i in range(raccoon.shape[2]):
    temp = np.zeros_like(raccoon) # raccoon과 같은 크기지만 값이 모두 0인 행렬을 만들어준다.
    temp[:, :, i] = raccoon[:,:,i]
    axes[i].imshow(temp)
    axes[i].axis("off")


img = Image.open(r"./image data analysis data/Raccoon image.jpg")
img.show()
img.format
img.mode
img.size
img.save("new_image.png")

img.resize((100, 400)).show()
img.thumbnail((100,400)) # 가로세로 비율이 유지된다.
img.show()
img.size
img.rotate(45).show()


img = Image.open(r"./image data analysis data/Raccoon image.jpg")
logo = Image.open(r"./image data analysis data/python_logo.png")
logo_x, logo_y = (img.width - logo.width), (img.height - logo.height)
img.paste(logo, (logo_x, logo_y))
img.show()

# a = Image.FLIP_TOP_BOTTOM
# a = Image.ROTATE_90
# a = Image.ROTATE_180
# a = Image.TRANSPOSE
a = Image.TRANSVERSE
img_flip = img.transpose(a)
img_flip.show()


img = Image.open(r"./image data analysis data/Raccoon image.jpg")
img.convert("L").show() # 흑백
r, g, b = img.split()
new_image = Image.merge("RGB", (g, b ,r))
new_image.show()


from PIL import ImageEnhance
contrast = ImageEnhance.Contrast(img)
contrast.enhance(1.5).show()

color = ImageEnhance.Color(img)
color.enhance(1.5).show()


brightness = ImageEnhance.Brightness(img)
brightness.enhance(1.5).show()


sharpness = ImageEnhance.Sharpness(img)
sharpness.enhance(1.5).show()


#kernel은 가운데 원소가 0,0으로 인덱싱 되어있다.
raccoon = Image.open(r"./image data analysis data/Raccoon image.jpg")
kernel = np.ones((3,3)) / 9
#kernel = np.ones((10,10)) / 100


kernel = np.array([[0,-1,0],
                   [-1,4,-1],
                   [0,-1,0]])

kernel = np.array([[-1,-1,-1],
                   [-1,8,-1],
                   [-1,-1,-1]])

kernel = np.array([[-1,0,-1],
                   [0,4,0],
                   [-1,0,-1]])

kernel = np.array([[-1, -1, -1],
                   [-1,9,-1],
                   [-1,-1,-1]])

kernel = np.array([[-1, 0, 1],
                   [-1, 0, 1],
                   [-1, 0, 1]])  # -> 세로선이 밝아진다 일단 합이 0이기때문에 대부분의 사진이 어두워지게 된다.

kernel = np.array([[1,1,1],
                   [0,0,0],
                   [-1,-1,-1]])

#1,1,1
#1,1,1
#1,1,1


raccoon_data = np.array(raccoon)
raccoon_data.shape

out = cv2.filter2D(raccoon_data, -1, kernel)
out_img = Image.fromarray(out)
out_img.show()
out_img.size
raccoon.show()



cat = Image.open(r"./image data analysis data/cat.png")
cat.show()

cat_data = np.array(cat)
w, h, d = cat_data.shape
X = cat_data.reshape((w * h, d)) / 255


kmeans = KMeans(n_clusters = 10, # 클러스터가 커질수록 원본이미지와 비슷해진다.
                max_iter=10, n_init=1)

res = kmeans.fit(X)
centroids = res.cluster_centers_
compressed_X = (255 * centroids[res.labels_, :]).astype(np.uint8).reshape((w, h, d))
compressed_image = Image.fromarray(compressed_X)
compressed_image.show()
compressed_image.save(r"./image data analysis data/comp_Cat.png")



