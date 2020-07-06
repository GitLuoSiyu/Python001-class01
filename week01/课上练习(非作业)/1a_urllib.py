from urllib import request
import urllib.request

# GET
response = request.urlopen('http://httpbin.org/get')
print(response.read().decode())

# POST
response = request.urlopen('http://httpbin.org/post', data=b'key=value', timeout = 10)
print(response.read().decode())

# cookie
from http import cookiejar
# 创建一个cookiejar对象
cookie = cookiejar.CookieJar()

# 创建cookie处理器
handler = request.HTTPCookieJar()

# 创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)

# 创建Opener对象
opener = request.build_opener(handler)











