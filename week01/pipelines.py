# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SpiderPipeline:
    def process_item(self, item, spider):
       title = item['title']
       link = item['link']
       time = item['time']
       type1 = item['type']
       output = '{title}|\t{link}|\t{time}|\t{type1}|\t'.format(title,link,time,type1)
       with open('movie.csv','a+',encoding='utf-8') as movie:
           movie.write(output)
       return item
