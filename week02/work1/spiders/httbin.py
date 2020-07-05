# -*- coding: utf-8 -*-
import scrapy
from httpbin.items import HttpbinItem

class HttbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        pipeline_items = []
        item = HttpbinItem()
        item['ip_origin'] = response.text
        pipeline_items.append(item)
        return pipeline_items
