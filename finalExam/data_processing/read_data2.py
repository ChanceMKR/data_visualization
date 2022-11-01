import os
import pandas as pd

os.getcwd()
path1 = "./data/game_user_data/"
path2 = "dau"
path3 = "/game-01"
path = path1 + path2 + path3

os.listdir(path)

data_list = []

def read_fun2(path2):
    path = path1 + path2 + path3
    for i in os.listdir(path):
        folder = path + "/" + i + "/data.tsv"
        data = pd.read_table(folder, sep="\t")
        data_list.append(data)
    
    return pd.concat(data_list, axis=0)