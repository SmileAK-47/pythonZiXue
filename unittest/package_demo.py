#coding  :utf-8
import unittest
import requests
class Test_kuaidi(unittest.TestCase):
    def setUp(self):
        self.headers = {"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        self.s = requests.session()
    def test_yunda(self):
        danhao = '1202247993797'
        kd = 'yunda'
        #这里对url的单号参数了
        self.url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html"
        print(self.url)
        #第一步发送请求
        r = self.s.get(self.url, headers = self.headers, verify = False)
        result = r.json()
        # #第二步获取结果
        print(result['company'])#获取公司名称
        data = result["data"]#获取data里面内容
        print(data[0])
        get_result = data[0]['context']
        print(get_result)
        #断言：测试结果与期望结果对比
        self.assertEqual('韵达' ,result['company'])
        self.assertIn('已签收',get_result)
if __name__ =="main":
    unittest.main()
