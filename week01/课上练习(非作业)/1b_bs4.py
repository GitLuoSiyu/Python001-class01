# 使用BeautifulSoup解析网页
import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'

headers = {'user-agent': user_agent}

url = 'https://movie.douban.com/top250'

response = requests.get(url, headers = headers)

bs_info = bs(response.text, 'html.parser')

# python 中使用 for in 形式的循环,Python使用缩进来进行代码分割
for tags in bs_info.find_all('div', attrs = {'class': 'hd'}):
    for atag in tags.find_all('a',):
        print(atag.get('href'))
        # 获取所有链接
        print(atag.find('span',).text)
        # 获取电影名称




# 运行结果
# https://movie.douban.com/subject/1292052/
# 肖申克的救赎
# https://movie.douban.com/subject/1291546/
# 霸王别姬
# https://movie.douban.com/subject/1292720/
# 阿甘正传
# https://movie.douban.com/subject/1295644/
# 这个杀手不太冷
# https://movie.douban.com/subject/1292063/
# 美丽人生
# https://movie.douban.com/subject/1292722/
# 泰坦尼克号
# https://movie.douban.com/subject/1291561/
# 千与千寻
# https://movie.douban.com/subject/1295124/
# 辛德勒的名单
# https://movie.douban.com/subject/3541415/
# 盗梦空间
# https://movie.douban.com/subject/3011091/
# 忠犬八公的故事
# https://movie.douban.com/subject/1292001/
# 海上钢琴师
# https://movie.douban.com/subject/1292064/
# 楚门的世界
# https://movie.douban.com/subject/3793023/
# 三傻大闹宝莱坞
# https://movie.douban.com/subject/2131459/
# 机器人总动员
# https://movie.douban.com/subject/1291549/
# 放牛班的春天
# https://movie.douban.com/subject/1889243/
# 星际穿越
# https://movie.douban.com/subject/1292213/
# 大话西游之大圣娶亲
# https://movie.douban.com/subject/5912992/
# 熔炉
# https://movie.douban.com/subject/25662329/
# 疯狂动物城
# https://movie.douban.com/subject/1307914/
# 无间道
# https://movie.douban.com/subject/1291560/
# 龙猫
# https://movie.douban.com/subject/1291841/
# 教父
# https://movie.douban.com/subject/1849031/
# 当幸福来敲门
# https://movie.douban.com/subject/3319755/
# 怦然心动
# https://movie.douban.com/subject/6786002/
# 触不可及




