#coding: utf-8

import  urllib.error,urllib.request,urllib.parse
import http.cookiejar

login_ur1 = "https://passport.cnblogs.com/user/signin"

get_url = "https://home.cnblogs.com/u/smileAK47/"

valuse = {
    "input1":"p92zv+PMrC0wkP8l/8fl7E2sUxaxKZ+awUh+NkEsn+OhSKEt8kBSIDahnsHqE1S8ewrl3F580DB7rEhimy6hHlp/NEIorJKeMx7YHz3CgcJWpoe384OoB4Z+UV7/tCcJU1ykVI7RwsYLh3dlwAspSI6K5VnTHChfSk1ILWObAXE=",
    "input2":"LE5Jfw3CQAjJ50OYsioNkHCLF0rx5LUoSJ49rBgbZnu/Z2Qz7aeV81MFB0pBVaJv/7u4mO3ZXXLw1mO4QfKl1OhHjyMxGKpNUViUWaAJln1hSIgAQVCkoHKuyRhn/kB8pmT8+kXEyGSqBiaTWcgIhMl9V4I+S6fpNR7DH69ur14=",
    "remember": False
    }
postdata = urllib.parse.urlencode(valuse).encode()
user_agen = {
    "User-Agent":
        " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
headers = {
        'User-Agent':user_agen, 'Connection':'keep-alive'
    }

cookie_filename= 'cookie.txt'

cookie_aff = http.cookiejar.MozillaCookieJar(cookie_filename)

handler = urllib.request.HTTPCookieProcessor(cookie_aff)

opener = urllib.request.build_opener(headers)
request = urllib.request.Request(login_ur1)

try :
    response = opener.open(request)
except urllib.error.URLError as e:
    print(e.reason)

cookie_aff.save(ignore_discard= True,ignore_expires = True)

for item in cookie_aff:
    print('Name='+ item.name)
    print('Value='+ item.value)

#使用cookie登录get_uel
get_request = urllib.request.Request(get_url,headers = headers)
get_response = opener.open(get_request)
print(get_response.read().decode())