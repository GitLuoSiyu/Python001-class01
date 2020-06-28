import requests
from bs4 import BeautifulSoup as bs
import csv
with open('data.csv','w',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
cookie = '__mta=145079819.1560786771466.1593172387616.1593173075229.37; _lxsdk_cuid=16b66241d56ad-012b83434b8298-f373567-100200-16b66241d57c8; mojo-uuid=8c3c5b6c38e5c467401eef443e9718dc; uuid_n_v=v1; uuid=2A2FE020ADE811EA8C8DE3118EB8AC1A4DAE102ED95D4042AF5F9D0C6E45B927; _lxsdk=2A2FE020ADE811EA8C8DE3118EB8AC1A4DAE102ED95D4042AF5F9D0C6E45B927; recentCis=1; _csrf=9fd658cc88861a15f4cb93f2bead7ab32931b559b70ff89908098ef4ef6f8e80; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592102325,1593017843,1593166930; __mta=145079819.1560786771466.1593018689733.1593166946145.20; mojo-session-id={"id":"805ca80a211a56f2dfdcfeced469be39","time":1593169247977}; mojo-trace-id=47; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593173075; _lxsdk_s=172f0497ed7-95e-acb-641%7C%7C79'
header = {'user-agent':user_agent,'Cookie':cookie}
url = 'https://maoyan.com/board/4'
type_url = ''
response = requests.get(url,headers=header)
bs_info = bs(response.text,'html.parser')
for tags in bs_info.find_all('div',attrs={'class':'movie-item-info'}):
    for atag in tags.find_all('a'):
        print (atag.text)
        writer.writerow(atag.text)
        type_url = 'https://maoyan.com' + atag.get('href')
        print(type_url)
    for ptag in tags.find_all('p', attrs={'class': 'releasetime'}):
        print(ptag.text)
        writer.writerow(ptag.text)

response1 = requests.get(type_url,headers=header)
bs_info2 = bs(response1.text,'html.parser')
for tag in bs_info2.find_all('div',attrs={'class':'movie-brief-container'}):
    for atag1 in tag.find_all('a'):
        print (atag1.text)
        writer.writerow(atag1.text)

