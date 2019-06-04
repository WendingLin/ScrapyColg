import scrapy
from scrapy.spiders import Spider
from .tools import time_compare
from ..items import Topic, Reply


class DjSpider(Spider):
    name = 'colg'
    start_urls = [
        'https://bbs.colg.cn/forum-171-1.html',
    ]


    starter_url = 'https://bbs.colg.cn/'
    page_counter = 1

    # first page
    def parse(self, response):
        for each in response.xpath("//table[@id='threadlisttableid']/tbody[contains(@id,'normal')]"):
            topic = Topic()
            topic['date'] = each.xpath("tr/td[2]/em/span/text()").extract_first()
            if(time_compare(topic['date'])==False):
                continue
            topic['type'] = each.xpath("tr/th/em/a/text()").extract_first()
            topic['content'] = each.xpath("tr/th/a[1]/text()").extract_first()
            topic['author'] = each.xpath("tr/td[2]/cite/a/text()").extract_first()
            yield topic

        # parse the page and yield items
        if self.page_counter == 1:
            return
        next_page = response.xpath("//a[@class='nxt']/@href").extract()[0]
        url_next_page = self.starter_url + next_page
        print(url_next_page)
        self.page_counter += 1
        yield scrapy.Request(url_next_page, self.parse)



    # def parsecontent(self, response):
    #     # parse the page and yield items
    #     ____next_page = response.xpath("some link element for the next page")
    #     ____if
    #     next_page is not None:
    #     ________url_next_page = next_page.get_url()
    #     ________yield
    #     scrapy.Request(url_next_page, self.parse)
