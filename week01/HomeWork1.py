import requests
from bs4 import BeautifulSoup
import pandas as pd

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'uuid_n_v=v1; uuid=F97222B0B76811EA9736CB82F1E06989920248FF2A224C3CBF94A7A34351517D; mojo-uuid=2b4fed65a835e681e1fdb005bddb1e46; _lxsdk_cuid=172eef93ae8c8-0eeb2f133b8fa6-4353760-144000-172eef93ae8c8; _lxsdk=F97222B0B76811EA9736CB82F1E06989920248FF2A224C3CBF94A7A34351517D; _csrf=8c54da97c327305eb0b03d703906e01ed4ce97171f3fef05b4da8c7dfc918800; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593147210,1593223737; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593225630; __mta=121412407.1593147210586.1593225614673.1593225630337.5; _lxsdk_s=172f3cff427-05e-d5e-ef5%7C%7C1',
    'Host': 'maoyan.com',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

myurl = 'https://maoyan.com/films?showType=3'
response = requests.get(myurl, headers=header)
bs_info = BeautifulSoup(response.text, 'html.parser')
dic_info = {
    '电影名称': [],
    '电影类型': [],
    '上映时间': []
}

num_limit = 10
n = 0
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    if n >= 10:
        break

    for tags_2nd in tags.find_all('div', ):
        if tags_2nd.find('span', attrs={'class': 'name'}) is not None:
            name = tags_2nd.find('span', attrs={'class': 'name'}).text
            dic_info['电影名称'].append(name)

        elif tags_2nd.find('span', ).text[:-1] == '类型':
            genra = tags_2nd.text.split('\n')[2].strip()
            dic_info['电影类型'].append(genra)

        elif tags_2nd.find('span', ).text[:-1] == '上映时间':
            release_date = tags_2nd.text.split('\n')[2].strip()
            dic_info['上映时间'].append(release_date)

    n += 1

pd.DataFrame(dic_info).to_csv('requests_bs4_猫眼电影前10.csv', encoding='utf-8-sig')
