#coding:utf-8
import requests

#先打开首页获取cookie

url = "http://localhost:8080/j_acegi_security_check "
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"

}   # get 方法其它加个 ser-Agent 就可以了

d = {"from":"",
     "j_password":"wg0051",
     "j_username":"wanggang",
     "Submit":"登录"}

s = requests.session()
r = s.post(url, headers=headers,data= d)
print(r.content).decode('utf-8')