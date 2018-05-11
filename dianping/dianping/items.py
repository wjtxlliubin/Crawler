# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DianpingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # define the fields for your item here like:
    _id = scrapy.Field()
    
    name = scrapy.Field()

    description = scrapy.Field()

    effection = scrapy.Field()

    teachers = scrapy.Field()

    environment = scrapy.Field()

    phone = scrapy.Field()

    address = scrapy.Field()

    class_des = scrapy.Field()

    star = scrapy.Field()

    characteristic = scrapy.Field()

    









