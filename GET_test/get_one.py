#conding:utf-8
import requests
#
# r = requests.get('https://baidu.com/')
#
# print(r.url)
# print(r.encoding)
# print(r.cookies)
# print(r.headers)
# print(r.content)
# print(r.text)

payload = {"youyou": "hello world",
           "pythonqq群":"ddd"}
r = requests.post('http://httpbin.org/post',data=payload)
print(r.text)