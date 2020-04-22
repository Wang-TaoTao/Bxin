# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql

# class DoubanPipeline(object):
#
#     def __init__(self):
#         self.file = open('Douban3.json','w')
#
#
#
#
#     def process_item(self, item, spider):
#
#
#         item = dict(item)
#         json_data = json.dumps(item, ensure_ascii=False) + ',\n'
#         self.file.write(json_data)
#
#
#         return item
#
#     def __del__(self):
#         self.file.close()
from Douban.items import DoubanDetailItem, DoubanItem


class DoubanPipeline(object):

    def process_item(self, item ,spider):

        # obj1 = DoubanItem()
        # print(obj1.direct)

        # DoubanItem.save()
        # DoubanDetailItem.save()
        # DoubanItem.save()
        item.save()


        return item
