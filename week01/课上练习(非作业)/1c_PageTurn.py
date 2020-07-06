import requests
from bs4 import BeautifulSoup as bs 

def get_url_name(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'

    header = {'user-agent': user_agent}
    response = requests.get(url, headers = header)
    bs_info = bs(response.text, 'html.parser')

    # 
    for tags in bs_info.find_all('div', attrs = {'class': 'hd'}):
        for atag in tags.find_all('a',):
            # 获取所有链接
            print(atag.get('href'))
            # 获取电影名称
            print(atag.find('span',).text)

# 生成包含所有页面的元组
urls = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))

print(urls)

# 控制请求的频率，引入time模块，类似异步延迟
from time import sleep

sleep(10)

for page in urls:
    get_url_name(page)
    sleep(5)


# 运行结果:
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
# https://movie.douban.com/subject/1296141/
# 控方证人
# https://movie.douban.com/subject/1851857/
# 蝙蝠侠：黑暗骑士
# https://movie.douban.com/subject/1292365/
# 活着
# https://movie.douban.com/subject/20495023/
# 寻梦环游记
# https://movie.douban.com/subject/1300267/
# 乱世佳人
# https://movie.douban.com/subject/1293172/
# 末代皇帝
# https://movie.douban.com/subject/26387939/
# 摔跤吧！爸爸
# https://movie.douban.com/subject/1291552/
# 指环王3：王者无敌
# https://movie.douban.com/subject/30170448/
# 何以为家
# https://movie.douban.com/subject/1929463/
# 少年派的奇幻漂流
# https://movie.douban.com/subject/2129039/
# 飞屋环游记
# https://movie.douban.com/subject/1293182/
# 十二怒汉
# https://movie.douban.com/subject/1291858/
# 鬼子来了
# https://movie.douban.com/subject/21937452/
# 素媛
# https://movie.douban.com/subject/1291583/
# 天空之城
# https://movie.douban.com/subject/1308807/
# 哈尔的移动城堡
# https://movie.douban.com/subject/1299398/
# 大话西游之月光宝盒
# https://movie.douban.com/subject/1291828/
# 天堂电影院
# https://movie.douban.com/subject/1293839/
# 罗马假日
# https://movie.douban.com/subject/1298624/
# 闻香识女人
# https://movie.douban.com/subject/1295038/
# 哈利·波特与魔法石
# https://movie.douban.com/subject/21937445/
# 辩护人
# https://movie.douban.com/subject/26752088/
# 我不是药神
# https://movie.douban.com/subject/1292000/
# 搏击俱乐部
# https://movie.douban.com/subject/1291548/
# 死亡诗社
# https://movie.douban.com/subject/1299131/
# 教父2
# https://movie.douban.com/subject/1301753/
# 狮子王
# https://movie.douban.com/subject/1291572/
# 指环王2：双塔奇兵
# https://movie.douban.com/subject/1418019/
# 大闹天宫
# https://movie.douban.com/subject/1900841/
# 窃听风暴
# https://movie.douban.com/subject/1305487/
# 猫鼠游戏
# https://movie.douban.com/subject/1291571/
# 指环王1：魔戒再现
# https://movie.douban.com/subject/1293350/
# 两杆大烟枪
# https://movie.douban.com/subject/1296736/
# 钢琴家
# https://movie.douban.com/subject/1306029/
# 美丽心灵
# https://movie.douban.com/subject/1291818/
# 饮食男女
# https://movie.douban.com/subject/1291843/
# 黑客帝国
# https://movie.douban.com/subject/1292224/
# 飞越疯人院
# https://movie.douban.com/subject/1485260/
# 本杰明·巴顿奇事
# https://movie.douban.com/subject/1309046/
# V字仇杀队
# https://movie.douban.com/subject/3742360/
# 让子弹飞
# https://movie.douban.com/subject/26580232/
# 看不见的客人
# https://movie.douban.com/subject/1292402/
# 西西里的美丽传说
# https://movie.douban.com/subject/1303021/
# 小鞋子
# https://movie.douban.com/subject/1292849/
# 拯救大兵瑞恩
# https://movie.douban.com/subject/27060077/
# 绿皮书
# https://movie.douban.com/subject/3442220/
# 海豚湾
# https://movie.douban.com/subject/1292220/
# 情书
# https://movie.douban.com/subject/3008247/
# 穿条纹睡衣的男孩
# https://movie.douban.com/subject/25958717/
# 海蒂和爷爷
# https://movie.douban.com/subject/1294408/
# 音乐之声
# https://movie.douban.com/subject/1292262/
# 美国往事
# https://movie.douban.com/subject/1780330/
# 致命魔术
# https://movie.douban.com/subject/1291832/
# 低俗小说
# https://movie.douban.com/subject/1292223/
# 七宗罪
# https://movie.douban.com/subject/1293544/
# 沉默的羔羊
# https://movie.douban.com/subject/1292343/
# 蝴蝶效应
# https://movie.douban.com/subject/2334904/
# 禁闭岛
# https://movie.douban.com/subject/1292679/
# 春光乍泄
# https://movie.douban.com/subject/1292656/
# 心灵捕手
# https://movie.douban.com/subject/11525673/
# 布达佩斯大饭店
# https://movie.douban.com/subject/1787291/
# 被嫌弃的松子的一生
# https://movie.douban.com/subject/1652587/
# 阿凡达
# https://movie.douban.com/subject/1294371/
# 摩登时代
# https://movie.douban.com/subject/1292370/
# 剪刀手爱德华
# https://movie.douban.com/subject/1294639/
# 勇敢的心
# https://movie.douban.com/subject/1292215/
# 天使爱美丽
# https://movie.douban.com/subject/1302425/
# 喜剧之王
# https://movie.douban.com/subject/1297192/
# 致命ID
# https://movie.douban.com/subject/1298070/
# 加勒比海盗
# https://movie.douban.com/subject/1418834/
# 断背山
# https://movie.douban.com/subject/3011235/
# 哈利·波特与死亡圣器(下)
# https://movie.douban.com/subject/1300299/
# 杀人回忆
# https://movie.douban.com/subject/6985810/
# 狩猎
# https://movie.douban.com/subject/26799731/
# 请以你的名字呼唤我
# https://movie.douban.com/subject/1297359/
# 幽灵公主
# https://movie.douban.com/subject/1291875/
# 阳光灿烂的日子
# https://movie.douban.com/subject/25814705/
# 小森林 夏秋篇
# https://movie.douban.com/subject/1291999/
# 重庆森林
# https://movie.douban.com/subject/2149806/
# 入殓师
# https://movie.douban.com/subject/1297630/
# 第六感
# https://movie.douban.com/subject/10777687/
# 7号房的礼物
# https://movie.douban.com/subject/1865703/
# 红辣椒
# https://movie.douban.com/subject/21318488/
# 消失的爱人
# https://movie.douban.com/subject/25814707/
# 小森林 冬春篇
# https://movie.douban.com/subject/1296339/
# 爱在黎明破晓前
# https://movie.douban.com/subject/1292434/
# 一一
# https://movie.douban.com/subject/1297052/
# 侧耳倾听
# https://movie.douban.com/subject/1306249/
# 唐伯虎点秋香
# https://movie.douban.com/subject/5322596/
# 超脱
# https://movie.douban.com/subject/3072124/
# 玛丽和马克思
# https://movie.douban.com/subject/1297447/
# 倩女幽魂
# https://movie.douban.com/subject/3395373/
# 蝙蝠侠：黑暗骑士崛起
# https://movie.douban.com/subject/4268598/
# 告白
# https://movie.douban.com/subject/1305164/
# 甜蜜蜜
# https://movie.douban.com/subject/1291545/
# 大鱼
# https://movie.douban.com/subject/4917726/
# 阳光姐妹淘
# https://movie.douban.com/subject/1292337/
# 无人知晓
# https://movie.douban.com/subject/5989818/
# 萤火之森
# https://movie.douban.com/subject/1316510/
# 射雕英雄传之东成西就
# https://movie.douban.com/subject/2353023/
# 驯龙高手
# https://movie.douban.com/subject/11026735/
# 超能陆战队
# https://movie.douban.com/subject/4202302/
# 借东西的小人阿莉埃蒂
# https://movie.douban.com/subject/1292274/



