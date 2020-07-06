import requests
import lxml.etree

# 爬取页面详细信息
# 电影详细页面
url = 'https://movie.douban.com/subject/1292052/'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'

# 生目为字典使用字典的语法赋值
header = {}
header['user-agent'] = user_agent
response = requests.get(url, headers = header)

# xml化处理
selector = lxml.etree.HTML(response.text)

# 电影名称
file_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称:{file_name}')

# 上映日期
plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'评分:{plan_date}')

# 上映日期
mylist = [file_name, plan_date]

# 保存
import pandas as pd
movie1 = pd.DataFrame(data = mylist)

# windows需要使用gbk字符集
movie1.to_csv('./movie1.csv', encoding = 'gbk', index = False, header = False)














