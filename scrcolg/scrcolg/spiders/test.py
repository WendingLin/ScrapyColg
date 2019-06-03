from scrapy.spiders import Spider
from ..items import ScrcolgItem

class DjSpider(Spider):
    name = 'colg'
    start_urls = [
        'https://bbs.colg.cn/forum-171-1.html',
    ]



    def parse(self, response):
        items = []
        for each in response.xpath("//a[@class='s xst']/@href"):
            item = ScrcolgItem()
            header = each.extract()
            print(header)

        print(items)
        print(len(items))

