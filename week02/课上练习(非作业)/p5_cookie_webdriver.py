from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver,和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html

    browser.get('https://www.douban.com')
    time.sleep(1)

    browser.switch_to_frame(browser.find_elements_bt_tag_name('iframe')[0])
    btm1 = browser.find_element_bt_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    btm1.click()

    browser.find_element_by_xpath('//*[@id="username"]').send_keys('15055495@qq.com')
    browser.find_element_by_id('password').send_keys('test123test456')
    time.sleep(1)

    browser.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()

    # 获取cookies
    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)

except Exception as e:
    # 捕获异常
    print(e)
finally:
    browser.close()





