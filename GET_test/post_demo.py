# coding:utf-8

import requests
# 先打开登录首页，获取部分 cookie
url = "http://localhost:8080/jenkins/j_acegi_security_check"
headers = {
"User-Agent":
"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    # "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0)Gecko/20100101 Firefox/44.0"
} # get 方法其它加个 ser-Agent 就可以了
d = {"from": "",
"j_password": "f7bcd85ebab14e2fbb6d76cc99bc5c6a",
"j_username": "admin",
"Jenkins-Crumb": "e677c237181756818cbbccd4296d44f1",
"json": {"j_username": "admin",
"j_password": "f7bcd85ebab14e2fbb6d76cc99bc5c6a",
"remember_me": True,
"from": "",
"Jenkins-Crumb": "e677c237181756818cbbccd4296d44f1"
},
"remember_me": "on",
"Submit": u"登录"
}
s = requests.session()
r = s.post(url, headers=headers, data=d)
print (r.content.decode())


# import  re
# t = re.findall(r'<b>(.+?)</b>',r.content)
# print(t[0])
# print(t[1])