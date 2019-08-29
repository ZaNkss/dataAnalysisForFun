# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         data_spider
# Description:  
# Author:       Za_Nks
# Date:         2019/8/28
# -------------------------------------------------------------------------------
import random
import time

import pandas as pd
import requests
import db_client


class DataSpider(object):
    def __init__(self):
        self.cites = list(pd.read_csv('city_data.csv')['city'])
        self.db_collcetion = db_client.get_collection()

    def get_data(self):
        for city in self.cites:
            page_num = 1
            print("正在抓取%s的数据" % city)
            url = "https://travelsearch.fliggy.com/async/queryItemResult.do?" \
                  "searchType=product&keyword=%(city)s&category=SCENIC&pagenum=%(page_num)d" \
                  % {"city": city, "page_num": page_num}
            # proxy = random.choice(config.PROXY_POOL)
            # print(proxy)
            with requests.session() as s:
                res = s.get(url=url)
            data = res.json()
            page_message = data['data']['data'].get('itemPagenum')
            if page_message is not None:
                # 获取总页码数
                total_page_num = page_message['data']['count']
                data_list = data['data']['data']['itemProducts']['data']['list'][0]['auctions']
                self.store_data_to_db(city, data_list)
                print("成功抓取%s第%d页的数据" % (city, page_num))
                if total_page_num > 1:
                    # 对剩余页进行查询
                    for i in range(1, total_page_num):
                        page_num += 1
                        with requests.session() as s:
                            res = s.get(url=url)
                        data = res.json()
                        data_list = data['data']['data']['itemProducts']['data']['list'][0]['auctions']
                        self.store_data_to_db(city, data_list)
                        print("成功抓取%s第%d页的数据" % (city, page_num))
                        time.sleep(random.uniform(10, 20))

    def store_data_to_db(self, city, data_list):
        for data in data_list:
            data['city'] = city
            self.db_collcetion.insert_one(data)


if __name__ == '__main__':
    spider = DataSpider()
    spider.get_data()