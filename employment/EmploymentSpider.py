import scrapy
from items import EmploymentItem

class EmploymentSpider(scrapy.Spider):
    name = 'employment'
    allowed_domains = ["jobs.zhaopin.com","sou.zhaopin.com"]
    start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%90%88%E8%82%A5&kw=%E5%89%8D%E7%AB%AF&sm=0&p=1']
    def parse(self, response):
        salary = response.xpath('//td[@class="gsmc"]/a/text()').extract()
        item = EmploymentItem()
        item['salary'] = salary
        print(salary)
        yield item
