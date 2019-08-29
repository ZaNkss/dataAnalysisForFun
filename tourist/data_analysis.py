# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         data_analysis
# Description:  
# Author:       Za_Nks
# Date:         2019/8/29
# -------------------------------------------------------------------------------
from os import path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.json import json_normalize

import db_client


def save_data_to_file(filename):
    collction = db_client.get_collection()
    data = collction.find()
    data = json_normalize([i for i in data])
    data.to_csv(filename)
    return data


def get_data_from_file(filename):
    return pd.read_csv(filename)


if __name__ == '__main__':
    filename = "data.csv"
    if not path.exists(filename):
        data = save_data_to_file(filename)
    else:
        data = get_data_from_file(filename)

    print(data.columns)