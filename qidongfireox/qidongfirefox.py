#coding=utf-8

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://baidu.comg")
driver.find_element_by_id("kw").send_keys("gnag")
driver.find_element_by_id("su").click()
driver.quit()