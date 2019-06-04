import scrapy
from scrapy.spiders import Spider

from ..items import topic, reply

class DjSpider(Spider):
    name = 'colg'
    start_urls = [
        'https://bbs.colg.cn/forum-171-1.html',
    ]

    starter_url = 'https://bbs.colg.cn/'

    # first page
    def parse(self, response):
        # parse the page and yield items
        next_page = response.xpath("//a[@class='nxt']/@href").extract()[0]
        url_next_page = self.starter_url+next_page
        print(url_next_page)
        yield scrapy.Request(url_next_page, self.parse)
        #
        # for each in response.xpath("//a[@class='s xst']/@href"):
        #     header = each.extract()
        #     print(header)


    # def parsecontent(self, response):
    #     # parse the page and yield items
    #     ____next_page = response.xpath("some link element for the next page")
    #     ____if
    #     next_page is not None:
    #     ________url_next_page = next_page.get_url()
    #     ________yield
    #     scrapy.Request(url_next_page, self.parse)

