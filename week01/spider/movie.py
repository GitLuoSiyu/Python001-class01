# -*-coding: utf-8 -*-

class MovieSpider(scrapy.Spider):
    # 运行时传递的爬虫名字
    name = 'movies'

    # 允许访问的域名
    allowed_domains = ['douban.com']

    # 
    start_urls = ['http://douban.com/']

    def parse(self, response):
        pass