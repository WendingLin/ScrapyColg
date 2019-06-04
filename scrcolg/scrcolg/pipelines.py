# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .items import Topic, Reply
import jieba


class ScrcolgPipeline(object):
    counthours = [0] * 24

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, Topic):
            line = "帖子："+item['content'] + "\n"
        if isinstance(item, Reply):
            line = "回复:"+ item['content']+'\n'
        self.file.write(line)
        return item


