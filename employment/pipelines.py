# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from . import database

class EmploymentPipeline(object):
    def __init__(self):
        # self.file = codecs.open(
        #     'zhilian.json', 'w', encoding='utf-8')
        self.db = database.initDB()
    def process_item(self, item, spider):
        # print('aaa:', item)
        # line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # self.file.write(line)
        database.insert(self, item)
        return item
    def spider_closed(self, spider):
        # self.file.close()
        self.db.close()
