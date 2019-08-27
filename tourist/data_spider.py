# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         data_spider
# Description:  
# Author:       Za_Nks
# Date:         2019/8/28
# -------------------------------------------------------------------------------


import pandas as pd


def build_db_connect():
    pass


class DataSpider(object):
    def __init__(self):
        self.cites = list(pd.read_csv('city_data.csv')['city'])



