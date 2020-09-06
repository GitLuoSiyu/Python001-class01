# -*- coding: utf-8 -*-
import re
import datetime
import ast
import scrapy
from scrapy.selector import Selector
from smzd.items import ProductItem, CommentItem
from snownlp import SnowNLP

class SmzdSpider(scrapy.Spider):
    # 爬虫名称
    name = 'smzd'
    allowed_domains = ['smzdm.com']
    # 起始URL列表
    start_urls = ['https://smzdm.com']
    base_url = 'https://www.smzdm.com'
#   注释默认的parse函数
#   def parse(self, response):
#        pass

    def __init__(self):
        self.category = 'diannaoyouxi'
        self.count = 0
        self.limit = 10
        self._datetime = datetime.datetime
        self._timedelta = datetime.timedelta
        self.minutes_ago_pattern = re.compile(r"(\d+)分钟前")
        self.hours_ago_pattern = re.compile(r"(\d+)小时前")
        self.tag_pattern = re.compile(r"<[^>]*>")
        self.emotion_space_pattern = re.compile(r"(?<=])\ +(?=\[)")

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        url = f"https://www.smzdm.com/fenlei/{self.category}/"
        yield scrapy.Request(url=url, meta={'count': 0})

    # 解析函数
    def parse(self, response):
        # print('text',response.text)
        count = response.meta['count']
        # print('获取整体页面：',count)
        for div in response.css("#feed-main-list li > div"):
            # print('获取整体页面：',div)
            count += 1
            if count > self.limit:
                break
            title_tag = div.css("h5 a")
            article_url = title_tag.xpath("@href").get()
            article_id = title_tag.xpath("@href").re_first(r"/p/(\d+)")
            article_data = title_tag.xpath(
                "@onclick").re_first(r"push\((.*)\)")
            article_data = ast.literal_eval(article_data)
            article_title = article_data['pagetitle']

            yield ProductItem(**{
                'p_id': article_id,
                'p_name': article_title,
                'p_type': '电脑',
                'add_time': datetime.datetime.now()
            })
            yield scrapy.Request(article_url, callback=self.parse_comments, meta={'article_id': article_id})

        next_url = response.css(
            ".feed-pagenation .next-page a::attr(href)").get()
        if count <= self.limit and next_url:
            yield scrapy.Request(next_url, meta={'count': count})

    def parse_comments(self, response):
        article_id = response.meta['article_id']
        goods_type = response.css("div.crumbs a > span::text").getall()[-1]
        for li in response.css("#commentTabBlockNew li.comment_list"):
            pub_time = self._parse_time(li)
            comment_tag = li.css(
                ".comment_conBox > .comment_conWrap .comment_con")
            comment_id = comment_tag.css("input::attr(comment-id)").get()
            comment_info = self._parse_comments(comment_tag.css("p").get())

            yield CommentItem(**{
                'p_id': article_id,
                'p_name':goods_type,
                'c_id': comment_id, 
                'short': comment_info,
                'sentiment': SnowNLP(comment_info).sentiments,
                'c_time': pub_time,
                'add_time': datetime.datetime.now()
            })
        next_url = response.css("#commentTabBlockNew .pagination .pagedown a::attr(href)").get()
        if next_url:
            yield scrapy.Request(next_url, callback=self.parse_comments, meta={'article_id': article_id})

    def _parse_comments(self, html):
        html = self.tag_pattern.sub("", html)
        html = self.emotion_space_pattern.sub("", html)
        if html:
            html = html.strip()
        return html

    def _parse_time(self, sel):
        def _outtime(ptime):
            return ptime.strftime("%Y-%m-%d %H:%M")

        pub_time1 = sel.css(".time meta::attr(content)").get()
        pub_time2 = sel.css(".time::text").get()
        pub_time = self._datetime.strptime(pub_time1, "%Y-%m-%d")

        try:
            tmp = self._datetime.strptime(pub_time2, "%m-%d %H:%M")
            pub_time = pub_time.replace(month=tmp.month, day=tmp.day, hour=tmp.hour, minute=tmp.minute)
            return _outtime(pub_time)
        except ValueError:
            if pub_time2 == pub_time1 or not pub_time2:
                return _outtime(pub_time)
            elif self.hours_ago_pattern.search(pub_time2):
                hour = int(self.hours_ago_pattern.search(pub_time2).group(1))
                pub_time = self._datetime.now() - self._timedelta(seconds=hour * 3600)
                return _outtime(pub_time)
            elif self.minutes_ago_pattern.search(pub_time2):
                minutes = int(self.minutes_ago_pattern.search(pub_time2).group(1))
                pub_time = self._datetime.now() - self._timedelta(seconds=minutes * 60)
                return _outtime(pub_time)
        return _outtime(pub_time)


