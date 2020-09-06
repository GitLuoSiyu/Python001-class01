import os
import time

if __name__ == '__main__':
    while True:
        os.system("scrapy crawl smzd")
        # 每7200轮询一次
        time.sleep(7200)

