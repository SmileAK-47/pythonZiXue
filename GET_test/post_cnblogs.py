#coding :tuf -8
import urllib.error,urllib.request, urllib.parse
import  requests
import  http.cookies

login_ur1 = "https://passport.cnblogs.com/user/signin"

headers = {
"User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }

# payload = {
# #     "input1":"hnvPeczMqgCCsdMSqW2E5LSO/6DCiCGhCdACb/mb03LAfzERkjfbT6QegLtn2i/rXh5/WLdt2x4h/Z1Jyd7U2iJBfp6SrJ56Km2AnxqN5mzob+WBG6v6dNUDZDn8NP7RwAgmzefVnh3lXxzr/0kR8r83OSdU5apbv0lr0/jt4lc=",
# #      "input2":"DD55F1pTbAjMx0Xs9rlsciT5IE+pzCIxnqiJSznv6Oe2An4jjANUcZv+4wi+cJDcGr7VCr0RgUjkdDvaYnZ0//McDDofCYfU72DLwmZGXz6qz0DRkE+K1ba8XRUyOAfAHHIPH6sHWwUbZtesHwbmjcte+Ff4JvpFMNXhs+RgX+A=",
# #      "remember":True,
# #      }

s = requests.session()
r = s.get(login_ur1,  headers= headers, verify = False)
print(s.cookies)

c = requests.cookies.RequestsCookieJar()
c.set('.CNBlogsCookie', '2B255051085E41C1F9D68AD3373AD6D25D142810816DD76A03D049161CAB7F76A056936608FEABA76ADCF768DCAEB257EA6BAB66F40F7053B9C7EEC811849E482BF95F1A857A4CC14F76C9591CDBD608A1704F0D6334F4396F35895B543CFA87C03E9173') # 填上面抓包内容
c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8J0rgDI0eRtJkfTEZKR_e81NAzoHX1Eprt36_LidrtrkxDTQeLGkDumhdUC3kEL8giJsfFfuP3g4lGL65rFAzAzcae5gBJise2fymJRFJI93G4siIl1kLtGvJb6KqJaamrfTsg3f710LHjxdbbU4KUTrmJ_k9ffhaIGe-bkuFWK5z2tgaEuh4UMlzvLWYGJ9j6j1RqnrvwuUBzgN4NgK8szZBRKnlto70Z_6ZnO02oQOPfCtALtnzkD91vx716VZdEKtJDYjVqpY7hyFE9oTnF9RohFcdpgSrgv75WP_S236') # 填上面抓包内容
c.set('AlwaysCreateItemsAsActive',"True")
c.set('AdminCookieAlwaysExpandAdvanced',"True")
s.cookies.update(c)
print (s.cookies)



url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"

body = {
    "__VIEWSTATE":"",
    "__VIEWSTATEGENERATOR	":"FE27D343",
    "Editor$Edit$txbTitle	post_2018.11.22":" 哈哈",
    "Editor$Edit$EditorBody":	"<p>阿斯蒂芬</p>",
    "Editor$Edit$Advanced$ckbPublished":	"on",
    "Editor$Edit$Advanced$chkDisplayHomePage":"on"	,
    "Editor$Edit$Advanced$chkComments":	"on",
    "Editor$Edit$Advanced$chkMainSyndication"	:"on",
    "Editor$Edit$kbDraft"	:"存为草稿"
    }

r2 = s.post(url2 , data = body, verify = False)

print(r.content.decode('utf-8'))
