# 小文件下载
import requests
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

r = requests.get(image_url)
with open("python_logo.png", 'wb') as f:
    f.write(r.content)

# 大文件下载
import requests
file_url = "http://python.xxx.yyy.pdf"
r = requests.get(file_url, stream = True)
with open("python.pdf", "wb") as pdf:
    for thunk in r.iter_content(chunk_size = 1024):
        if chunk:
            pdf.write(chunk)







