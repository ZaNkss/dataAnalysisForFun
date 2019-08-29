# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         db_client
# Description:  
# Author:       Za_Nks
# Date:         2019/8/28
# -------------------------------------------------------------------------------

import pymongo
import config


def get_collection():
    uri = 'mongodb://%(user)s:%(pwd)s@%(host)s:%(port)d/%(database)s?authMechanism=SCRAM-SHA-1' % \
        {
            "user": config.DB['user'],
            "pwd": config.DB['password'],
            "host": config.DB['host'],
            "port": config.DB['port'],
            "database": config.DB['database']
        }
    client = pymongo.MongoClient(uri)
    return client.get_database(config.DB['database'])[config.DB['collection']]