import scrapy
from items import EmploymentItem

class EmploymentSpider(scrapy.Spider):
    name = 'employment'
    allowed_domains = ["jobs.zhaopin.com","sou.zhaopin.com"]
    p = 1
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%90%88%E8%82%A5&kw=%E5%89%8D%E7%AB%AF&sm=0&p='
    start_urls = [url + str(p)]

    def __init__(self):
        self.p = 1
        self.url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%90%88%E8%82%A5&kw=%E5%89%8D%E7%AB%AF&sm=0&p='

    def parse(self, response):
        contents = response.xpath('//table[@class="newlist"][position()>1]')

        if len(contents) == 0:
            return
        # xpath解析table需去掉tbody
        item = EmploymentItem()
        for content in contents:
            item['title'] = content.xpath('.//tr/td[@class="zwmc"]/div/a/text()').extract()[0]
            feedback = content.xpath('.//tr/td[@class="fk_lv"]/span/text()').extract()
            item['feedback'] = len(feedback) != 0 and feedback[0] or ''
            item['company'] = content.xpath('.//tr/td[@class="gsmc"]/a/text()').extract()[0]
            item['salary'] = content.xpath('.//tr/td[@class="zwyx"]/text()').extract()[0]
            item['location'] = content.xpath('.//tr/td[@class="gzdd"]/text()').extract()[0]
            item['date'] = content.xpath('.//tr/td[@class="gxsj"]/span/text()').extract()[0]
            yield item
        self.p = self.p + 1
        yield scrapy.Request(self.url + str(self.p), callback=self.parse)
