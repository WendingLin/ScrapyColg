import scrapy
from scrapy.spiders import Spider
from .tools import time_compare, get_page_url, clean_string
from ..items import Topic, Reply


class DjSpider(Spider):
    name = 'colg'
    start_urls = [
        'https://bbs.colg.cn/forum-171-1.html',
    ]
    base_url = 'https://bbs.colg.cn/'
    page_counter = 1

    # first page
    def parse(self, response):
        for each in response.xpath("//table[@id='threadlisttableid']/tbody[contains(@id,'normal')]"):
            topic = Topic()
            #Check time
            topic['date'] = each.xpath("tr/td[2]/em/span/text()").extract_first()
            if(time_compare(topic['date'])==False):
                continue
            link = get_page_url(each.xpath("tr/th/a[1]/@href").extract_first(), self.base_url)
            yield scrapy.Request(link, self.parsecontent)
            topic['type'] = each.xpath("tr/th/em/a/text()").extract_first()
            topic['content'] = each.xpath("tr/th/a[1]/text()").extract_first()
            topic['author'] = each.xpath("tr/td[2]/cite/a/text()").extract_first()
            yield topic

        # parse the page and yield items
        if self.page_counter == 1:
            return
        self.page_counter += 1
        next_page = response.xpath("//a[@class='nxt']/@href").extract_first()
        url_next_page = get_page_url(next_page, self.base_url)
        yield scrapy.Request(url_next_page, self.parse)



    def parsecontent(self, response):
        # parse the page and yield items

        # for each in response.xpath("//table[@class='plhin']/tr[1]"):
        #     content = each.xpath("//td[@class='t_f']")[0].xpath("string(.)").extract_first()
        #     #for info in each.xpath("//td[@class='t_f']/*[not(@class='pstatus') and not(@class='quote')]"):
        #         #content += info.xpath("string(.)").extract_first()
        for path in response.xpath("//td[@class='t_f']"):
            content = path.xpath("string(.)").extract_first()
            reply = Reply()
            reply['content'] = clean_string(content)
            yield reply

        next_page = response.xpath("//a[@class='nxt']/@href")
        if next_page.extract_first() is not None:
            url_next_page = get_page_url(next_page.extract_first(), self.base_url)
            yield scrapy.Request(url_next_page, self.parsecontent)
