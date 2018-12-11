#dncoding = uff- 8

from selenium import webdriver
import unittest
import time

class VisitSoGou(unittest.TestCase):

    def setUp(self):
        #启动浏览器
        self.driver = webdriver.Chrome(executable_path= "G:\webderiver\chromedriver.exe")
#获取页面Title属性值
    # def test_visitSogou(self):
    #     #访问搜索搜索首页
    #     self.driver.get("http://www.baidu.com")
    #     #打印当前网页的地址
    #     # print (self.driver.current_url)
    #     title = self.driver.title
    #     print("当前页面的title属性title的属性值:",title)
    #     self.assertEqual(title,"百度一下，你就知道","页面title属性值错误")

#获取页面HTML源代码
#     def test_getPageSource(self):
#         url = "http://www.sogou.com"
#         self.driver.get(self)
#         pageSource= self.driver.page_source
#         print(pageSource)
#         self.assertTrue(u"新闻"in pageSource,"页面源码中未找到'新闻'关键字")

#获取当前页面URL地址
    # def test_getCurrentPageUrl(self):
    #     url = "http://www.sogou.com"
    #     self.driver.get(url)
    #     currentPageUrl = self.driver.current_url
    #     print( currentPageUrl)
    #     self.assertEqual(currentPageUrl,"https://www.sogou.com/","当前页面网站非预期")


#获取页面元素的文本内容
    # def test_getWebElementText(self):
    #     url = "http://www.baidu.com"
    #     #访问百度首页
    #     self.driver.get(url)
    #     import time
    #     time.sleep(4)
    #     #通过xpah定位方式找到ID属性值为“u1”的元素下的第一个链接元素
    #     aElement = self.driver.find_element_by_xpath("//*[@class = 'mnav'][1]")
    #     #通过找到的链接元素对象的text属性获取到链接元素的问文本内容
    #     a_text = aElement.text
    #     self.assertEqual(a_text,u"新闻")

#获取页面元素的属性
    # def test_getWebElementAttrivute(self):
    #     url = "http://www.sougo.com"
    #     #访问搜狗首页
    #     self.driver.get(url)
    #     #找到搜索输入框元素
    #     searchBox = self.driver.find_element_by_id("query")
    #     #获取搜索输入框页面元素的name属性值
    #     print(searchBox.get_attribute("naem"))
    #     #向搜索输入框中输入“测试工程师指定的输入内容”
    #     searchBox.send_keys("测试工程师指定的输入内容")
    #     #获取页面搜索框的value属性值（既搜索框中的文字内容）
    #     print(searchBox.get_attribute("value"))

#获取页面元素CSS属性值
    # def test_getWebElementCSSvalue(self):
    #     url ="http://baidu.com"
    #     self.driver.get(url)
    #     #找到搜索输入框元素
    #     searchaBox = self.driver.find_element_by_id("kw")
    #     #使用页面元素对象的value_of_css_property()方法获取元素的css属性值
    #     print("搜索输入框的高度是：",searchaBox.value_of_css_property("height"))
    #     print("搜索输入框的宽度是：",searchaBox.value_of_css_property("width"))
    #     font = searchaBox.value_of_css_property("font-family")
    #     #断言搜索漱口的字符是否是arial 字体
    #     self.assertEqual(font,"arial")

#清空输入空中的内容
    # def test_clearInputBoxText(self):
    #     url = "http://baidu.com"
    #     #访问百度页面
    #     self.driver.get(url)
    #     #获取输入框页面对象
    #     input = self.driver.find_element_by_id("kw")
    #     input.send_keys("光荣子路自动化测试")
    #     import time
    #     time.sleep(4)
    #     #清空输入框中默认内容
    #     input.clear()
    #     time.sleep(5)

    # def test_printSelectText(self):
    #     url = "G:\\webderiver\\frouit.html"
    #     #访问自定义的HTML
    #     self.driver.get(url)
    #     #使用name属性找到页面上name属性为“fruit”的下拉列表元素
    #     # Select =self.driver.find_element_by_class_name("fruit")
    #     # all_option = self.driver.find_element_by_class_name("option")
    #     #
    #     # for option in all_option:
    #     #     print("选项显示的文本：",option.text)
    #     #     print("选项值为：",option.get_attribute("value"))
    #     #     option.click()
    #     #     import time
    #     #     time.sleep(5)



    #选择下拉列表元素的三种方法
    def test_opertaDroplIST(self):
        url =" G:\\webderiver\\frouit.html"
        #访问自定义的HTML 网页
        self.driver.get(url)
        #导入Select 模块
        from selenium.webdriver.support.ui import  Select
        #使用Xpath定位方式获取select页面元素对象
        select_element = Select(self.driver.find_element_by_xpath("//select"))
        #打印默认选中的文本
        print(select_element.first_selected_option.text)
        #获取所有选择的页面元素对象
        all_options = select_element.options
        #打印选项总个数
        print (len(all_options))

        # is_enabled(): 判断元素是否可操作
        # is_selected():判断元素是否被选中

        if all_options[1].is_enabled()and not all_options[1].is_selected():
        #     #方法一：通过序号选择第二个元素，序号从0开始
        #     select_element.select_by_index(1)
        #     #打印已选中项文本
        #     print(select_element.all_selected_options[0].text)
        #     #assertEqual()方法断言当前选中的选项文本是否是西瓜
        #     self.assertEqual(select_element.all_selected_options[0].text,"西瓜")
        # import time
        # time.sleep(5)

              #方法二“通过选项的显示文本选择文本为“猕猴桃”选项
        #     select_element.select_by_visible_text("泥猴桃")
        #    #断言已经选中的文本是否是"猕猴桃"
        #     self.assertEqual(select_element.all_selected_options[0].text,"泥猴桃")
        #     time.sleep(2)

            #方法三：通过选项的value属性值选择value= “shanzha”选项
            select_element.select_by_value("shanzha")
            print(select_element.all_selected_options[0].text)
            self.assertEqual(select_element.all_selected_options[0].text,"山楂")



    def tearDown(self):
        #退出浏览器
        self.driver.quit()

if __name__ == '__main__':
        unittest.main()
