# -*- coding: utf-8 -*-

import requests
from PIL import Image
from bs4 import BeautifulSoup
import re
from io import BytesIO
import numpy as np

url = r"https://www.sciencekids.co.nz/pictures/flags.html"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
countries = soup.select("tr > td.style54")
flags_url = [country.select("img")[0] for country in countries if len(country.select("img")) != 0]

countries_list = [country.select("a")[1].text for country in countries if len(country.select("a")) != 0]

flags_list = list()
for u in flags_url:
    flag_url = u.attrs["src"]
    image_url = r"https://www.sciencekids.co.nz" + re.sub("^[.]{2,}", "", flag_url)

    image_r = requests.get(image_url)
    flag_image = Image.open(BytesIO(image_r.content))
    flags_list.append(np.array(flag_image))

import pickle
with open(r"C:\Users\Beom\OneDrive - UOS\22년도 강의자료\22년도 데이터 시각화 강의자료\dashboard\countries_flags.pkl", "wb") as f:
    pickle.dump([countries_list, flags_list], f)
    f.close()
    