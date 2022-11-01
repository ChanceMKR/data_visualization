import numpy as np
import pandas as pd
import os

def read_fun(path, folder, subfolder = "game-01"):
    data_folder_path = path + "/" + folder + "/" + subfolder
    folder_list = os.listdir(data_folder_path)
    data_list = []
    for name in folder_list:
        data_path = data_folder_path + "/" + name + "/" + "data.tsv"
        data = pd.read_table(data_path, sep = "\t", header = 0)
        data_list.append(data)
    
    res_data = pd.concat(data_list, axis = 0, ignore_index = True)
    return(res_data)
