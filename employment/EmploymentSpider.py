import scrapy
from items import EmploymentItem

class EmploymentSpider(scrapy.Spider):
    name = 'employment'
    allowed_domains = ["jobs.zhaopin.com","sou.zhaopin.com"]

    def __init__(self):
        self.p = 1
        self.initCityIndex = 0
        self.cities = ('上海', '北京', '杭州', '深圳', '广州', '合肥')
        self.start_urls = [self.getUrl()]

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

    def getUrl(self):
        url = 'http://sou.zhaopin.com/jobs/searchresult.ashx'
        return url + '?kw=前端' + '&jl=' + self.cities[self.initCityIndex] + '&p=' + str(self.p)

    def parse(self, response):
        nextPage = response.xpath('//li[@class="pagesDown-pos"]')
        if len(nextPage) > 0:
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
        else:
            self.initCityIndex = self.initCityIndex + 1
            if (self.initCityIndex == len(self.cities)):
                return
            self.p = 1
            yield scrapy.Request(self.getUrl(), callback=self.parse)
