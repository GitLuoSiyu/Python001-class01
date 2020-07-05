# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class HttpbinPipeline:
    def __init__(self):
        # 本地mq
        self.client = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = '123456',
            database = 'myweb',
            charset = 'utf8mb4'
        )
        self.cur = self.client.cursor()
    def process_item(self, item, spider):
        ip = item['ip_origin']
        ip1= ip.split(':')[1]
        print (ip1)
        sql = 'insert into learn_author(ip) VALUES (%s)'
        try:
            self.cur.execute(sql,ip1)
            self.cur.close()
            self.client.commit()
        except Exception as e:
            print (e)
            self.client.rollback()
        self.client.close()

