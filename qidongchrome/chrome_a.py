from selenium import webdriver
import time
import os
browser = webdriver.Chrome('G:\webderiver\chromedriver.exe')
browser.get('http://www.baidu.com')

#页面最大化
browser.maximize_window()
#等待2秒
time.sleep(2)
#智能等待
# browser.implicitly_wait(30)
browser.find_element_by_id("kw").send_keys("wanggang")
time.sleep(2)
# browser.find_element_by_class_name("t c-gap-bottom-small").click()


# browser.back()


time.sleep(2)
#browser.find_element_by_naem("王刚").clike()
browser.quit()