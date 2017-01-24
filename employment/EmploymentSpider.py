import scrapy
from items import EmploymentItem

class EmploymentSpider(scrapy.Spider):
    name = 'employment'
    allowed_domains = ["jobs.zhaopin.com","sou.zhaopin.com"]
    p = 1
    cities = ('上海', '北京', '杭州', '深圳', '广州', '合肥')
    initCityIndex = 0
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx'
    start_urls = [url + '?kw=前端' + '&jl=' + cities[initCityIndex] + '&p=' + str(p)]

    def __init__(self):
        self.p = 1

    def getValue(self,arr):
        return len(arr) != 0 and arr[0] or ''

    def getTitle(self, arr):
        if len(arr) == 0:
            return ''
        str = ''
        for i in arr:
            i = i.replace('<b>', '').replace('</b>', '')
            str += i
        return str

    def parse(self, response):
        nextPage = response.xpath('//li[@class="pagesDown-pos"]')
        if len(nextPage) == 0:
            return
        contents = response.xpath('//table[@class="newlist"][position()>1]')
        # xpath解析table需去掉tbody
        item = EmploymentItem()
        for content in contents:
            salary = content.xpath('.//tr/td[@class="zwyx"]/text()').extract()
            salary = self.getValue(salary)
            if (salary and salary.find('-') > -1):
                salary = salary.split('-')
                item['min_salary'] = salary[0]
                item['max_salary'] = salary[1]
                title = content.xpath('.//tr/td[@class="zwmc"]/div/a/node()').extract()
                item['title'] = self.getTitle(title)
                feedback = content.xpath('.//tr/td[@class="fk_lv"]/span/text()').extract()
                item['feedback'] = self.getValue(feedback)
                company = content.xpath('.//tr/td[@class="gsmc"]/a/text()').extract()
                item['company'] = self.getValue(company)
                location = content.xpath('.//tr/td[@class="gzdd"]/text()').extract()
                item['location'] = self.getValue(location)
                date = content.xpath('.//tr/td[@class="gxsj"]/span/text()').extract()
                item['date'] = self.getValue(date)
                yield item
        url = response.url.replace('&p=' + str(self.p), '&p=' + str(self.p + 1))
        self.p = self.p + 1
        yield scrapy.Request(url, callback=self.parse)
