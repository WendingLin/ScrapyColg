# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .items import Topic, Reply

from .spiders.tools import get_hour, map_add, sortmap, write_map_to_csv


class ScrcolgPipeline(object):
    hours = {}
    topictypes = {}
    replyauthors = {}
    topicauthors = {}
    counttopics = 0
    countreplies = 0


    def open_spider(self, spider):
        self.file1 = open('counttopic', 'w')
        self.file2 = open('countreply', 'w')
        return

    def close_spider(self, spider):
        print("总共统计帖子数："+str(self.counttopics))
        print("总共统计回复数：" + str(self.countreplies))
        write_map_to_csv(sortmap(self.hours), 'hours.csv')
        write_map_to_csv(sortmap(self.topictypes), 'topictypes.csv')
        write_map_to_csv(sortmap(self.replyauthors), 'replyauthors.csv')
        write_map_to_csv(sortmap(self.topicauthors), 'topicauthors.csv')
        self.file1.close()
        self.file2.close()
        return

    def process_item(self, item, spider):
        map_add(get_hour(item['date']), self.hours)
        author = item['author']
        line =item['content'] + "\n"
        if isinstance(item, Topic):
            self.counttopics+=1
            type = item['type']
            map_add(type, self.topictypes)
            map_add(author, self.topicauthors)
            self.file1.write(line)
        if isinstance(item, Reply):
            self.countreplies+=1
            map_add(author, self.replyauthors)
            self.file2.write(line)

        return item


