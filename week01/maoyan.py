# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from spider.items import SpiderItem
from spider.pipelines import SpiderPipeline

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4']

    def start_requests(self):
        url = 'https://maoyan.com/board/4'
        yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        items = []
        movies = Selector(response=response).xpath('//*[@id="app"]/div/div/div[1]/dl/dd[2]/div/div/div[1]')
        for movie in movies:
            item = SpiderItem()
            link = movie.xpath('./a/@href')
            title = movie.xpath('./a/text()')
            time = movie.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[2]/div/div/div[1]/p[3]')
            item['title'] = title
            item['link'] = link
            item['time'] = time
            items.append(item)
            yield scrapy.Request(url=link,meta={'item':item},callback=self.parse2)
    def parse2(self,response):
        item = response.meta['item']
        m_type = Selector(response=response).xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[1]')
        item['type'] = m_type
        yield item