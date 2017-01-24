# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EmploymentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    feedback = scrapy.Field()
    company = scrapy.Field()
    min_salary = scrapy.Field()
    max_salary = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
