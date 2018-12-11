# coding:utf-8
import requests
url ="http://www.kuaidi.com/index-ajaxselectcourierinfo-9894058703354-youzhengguonei.html"

headers = {
'Host': 'www.kuaidi.com',
'Connection': 'keep-alive',
'Content-Length': '31',
'Accept': '*/*',
'Origin': 'http://www.kuaidi.com',
'X-Requested-With':' XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Referer': 'http://www.kuaidi.com/',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language':' zh-CN,zh;q=0.9',
'Cookie': 'lang=zh-cn; theme=default; sid=i4jglbduth9tcnp2grp1aj7tr2; UM_distinctid=1673ebd7c1d802-05a63bf81983e6-9393265-1fa400-1673ebd7c1f2; CNZZDATA1254194234=1530576628-1542943437-%7C1543212726'


} # get 方法加个 ser-Agent 就可以了

s = requests.session()
r = s.post(url, headers=headers)
result = r.json()
print(result)

# data = result["data"] # 获取 data 里面内容
# print (data)
# print (data[0]) # 获取 data 里最上面有个
# get_result = data[0]['context'] # 获取已签收状态
# print (get_result)
# if  u"已签收" in  get_result:
#     print("快递单已经签收成功"
# else:
#     print("未签收")