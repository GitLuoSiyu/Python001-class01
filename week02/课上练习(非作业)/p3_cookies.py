import requests

# 在同一个 Session 实例发出的所有请求之间保持 cookie

# requests 默认使用了 session 功能

s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')

print('返回值:',r.text)

# '{"cookies": {"sessioncookie": "1223456789"}}'

# 会话可以使用上下文管理器
with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')










