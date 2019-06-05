# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Topic(scrapy.Item):
    type = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()


class Reply(scrapy.Item):
    # define the fields for your item here like:
    content = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()

