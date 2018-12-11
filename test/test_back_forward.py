from selenium import webdriver

driver = webdriver.Chrome('G:\webderiver\chromedriver.exe')

#访问百度首页
first_url = "http://baidu.com"
print("now caaess %s" %(first_url))
driver.get(first_url)

#访问新网网页
second_url = 'http://news.baidu.com'
print("now access %s" %(second_url))
driver.get(second_url)

#返回（后退）到百度首页
print("back to %s" %(first_url))
driver.back()

#前进到新网页
print("forward to %s "%(second_url))
driver.forward()