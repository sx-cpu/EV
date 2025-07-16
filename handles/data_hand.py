# -------------------------------------------------- ML 28/11/2019 ----------------------------------------------------#
#
# File used to import data from preprocess to modeling module
# here we also add a column for weekday type
# two type of arguments 'granular' and 'counts'
# counts is from ts data
# granular is from each all clustered data
# force is used when we want to repull data from preprocessing even though its already present
# This file is used in the following manner.
#     importing data from preprocess
#     import data is used to import data from preprocessing folder to modeling folder
#     returns the location of the saved data file
#     loc = import_data(year=Year,slot=slot_mins,type='granular',force=True)
#     loc = import_data(year=Year,slot=slot_mins,type='counts')

#
# -------------------------------------------------------------------------------------------------------------------- #
import pandas as pd
import os

# load the config file
import json

# 获取当前脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 构建 config.json 的绝对路径
config_path = os.path.join(script_dir, '..', 'config.json')

try:
    with open(config_path, 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    print(f"Configuration file not found at {config_path}. Please ensure it exists.")
    # 可根据实际需求选择退出程序或进行其他处理
    raise

# config = json.load(open('config.json'))

def get_slotted_data(data, slot_secs):
    # created slots are in form of ceilings.
    factor = slot_secs / 3600
    # columns_to_divide = ['Start_time_slot', 'ChargeTime', 'ConnectedTime']
    data = ((data // factor) + 1).astype(int)
    return data

def get_csv_data(filename, filepath):
    # This function returns the data. data format should be in csv
    # read the raw data and prepare print out the first five rows of the data

    raw_data = pd.read_csv(os.path.join(filepath, filename))
    if config['verbose'] > 2:
        print(" ------------------- File:",filename," -------------------")
        print(raw_data.head(1))
    return raw_data

def create_factor_arr(year,month,daytype):
    # we can use this function to create a factor array for AM modeling
    # it is done using the year, month and daytype.

    factor_arr = year.apply(str) + "_" \
                 + month.apply(str) + "_" \
                 + daytype.apply(str)

    return factor_arr


