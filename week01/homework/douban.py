# 使用requests库获取豆瓣影评
# -*- coding: utf-8 -*-
import requests

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
cookie = 'bid=I4f-2S4Hw7M; gr_user_id=0bea42be-eb0f-4105-a24f-851b2aa6a2fb; _vwo_uuid_v2=DCD0B565CB6F9157AA1B5A5377BC5BDB9|0c5eb874c09393334309cbe33251b8c8; __gads=ID=4029d9123bb60610:T=1586704189:S=ALNI_MZb5BF_-JOLXLGFDHaDDmmRUCCgIg; viewed="1138768_1885761"; douban-fav-remind=1; ll="108296"; __utma=30149280.479131430.1586704071.1591256151.1593916687.5; __utmc=30149280; __utmz=30149280.1593916687.5.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1593916687; ap_v=0,6.0; __utma=223695111.967053518.1593916690.1593916690.1593916690.1; __utmb=223695111.0.10.1593916690; __utmc=223695111; __utmz=223695111.1593916690.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1593916690%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DMvmzox62zRsNF87fu-JEKPUoeyiOAFuPmEhwDWJK65JOEW45JGdGKftj9QDFDj5k%26wd%3D%26eqid%3De052bd6a002a13c2000000045f013d2c%22%5D; _pk_id.100001.4cf6=0d0e0a0d096e4984.1593916690.1.1593916690.1593916690.; _pk_ses.100001.4cf6=*; __yadk_uid=jDQTNaAhLsJVUlr1mp2RjLEBRb4nyyOj'

header = {'user-agent':user_agent,'Cookie':cookie}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl,headers=header)
print(response.text)
print(f'状态码:{response.status_code}')

