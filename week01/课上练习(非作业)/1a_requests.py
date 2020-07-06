import requests

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'

header = {'user-agent': user_agent}

url = 'https://movie.douban.com/top250'

response = requests.get(url, headers = header)
print(response.text)
print(f'返回状态码:{response.status_code}')