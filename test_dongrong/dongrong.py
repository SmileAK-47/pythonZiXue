from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
import time
import logging
import os

class GloryRoad(unittest.TestCase):
    def setUp(self):
        #启动
        self.driver = webdriver.Chrome("G:\\webderiver\\chromedriver.exe")

    def testDongRong(self):
        self.driver.get('http://admin.idongrong.com/index.php/login')
        self.driver.find_element_by_name("user_id").send_keys("10000")
        self.driver.find_element_by_name("user_pass").send_keys("123456")
        self.driver.find_element_by_class_name("Btn_b").click()
        time.sleep(5)

        assert u"wangg" in self.driver.page_source,"页面中不存在的元素"
    def tearDown(self):
        self.driver.quit()



if __name__  == "__main__":
    suite2 = unittest.TestLoader().loadTestsFromTestCase(GloryRoad)
    file = open('test_demo02.txt', 'w+')
    runner = unittest.TextTestRunner(stream=file, verbosity=2)
    runner.run(suite2)




'''
browser = webdriver.Chrome('G:\webderiver\chromedriver.exe')
browser.get('http://admin.idongrong.com/index.php/login')

#页面最大化
browser.maximize_window()
#等待2秒
time.sleep(2)
#智能等待
# browser.implicitly_wait(30)
#登录动容后台
browser.find_element_by_name("user_id").send_keys("10000")
browser.find_element_by_name("user_pass").send_keys("123456")
time.sleep(2)
browser.find_element_by_class_name("Btn_b").click()

browser.find_element_by_id("12").click()

browser.find_element_by_id("12-1201")
browser.find_element_by_id("12-1201-120102").click()

time.sleep(3)
browser.quit()
'''