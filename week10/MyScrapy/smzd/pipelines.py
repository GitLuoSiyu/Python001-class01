# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# python 一期 毕业作业
import pymysql

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'lxp123456',
    'db' : 'test'
}

from .items import ProductItem, CommentItem

class SmzdPipeline:
     def process_item(self, item, spider):
        if type(item) == ProductItem:
            table = 'product'
        elif type(item) == CommentItem:
            table = 'comment'
        keys = ', '.join(item.keys())
        values = ', '.join([f'%({i})s' for i in item])
        add_sql = ("INSERT IGNORE INTO %s (%s) VALUES (%s)" % (table, keys, values))
        conn = pymysql.connect(
            host = dbInfo['host'],
            port = dbInfo['port'],
            user = dbInfo['user'],
            password = dbInfo['password'],
            db = dbInfo['db']
         )
        cur = conn.cursor()
         
        try:
            cur.execute(add_sql, dict(item))
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()

        return item
