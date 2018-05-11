# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log



class DianpingPipeline(object):
    def __init__(self):
        connection=pymongo.MongoClient(
            settings['MONGO_HOST'],
            settings['MONGO_PORT']
        )
        db=connection[settings['MONGO_DB']]
        self.collection=db[settings['MONGO_COLL']]
    def process_item(self,item,spider):
        value = self.collection.find_one(item['_id'])
        if value:
            log.msg('The item has in mongo',
                        level=log.DEBUG,spider=spider)
        else:
            valid=True
            for data in item:
                if not data:
                    valid=False
                    raise DropItem('Missing{0}!'.format(data))
            if valid:
                self.collection.insert(dict(item))
                log.msg('question added to mongodb database!',
                        level=log.DEBUG,spider=spider)
            return item