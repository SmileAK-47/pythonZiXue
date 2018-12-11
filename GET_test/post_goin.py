#coding :utf -8

import  requests

url = "https://passport.cnblogs.com/user/signin"

headers = {
"User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"

}

payload = {
    "input1":"hnvPeczMqgCCsdMSqW2E5LSO/6DCiCGhCdACb/mb03LAfzERkjfbT6QegLtn2i/rXh5/WLdt2x4h/Z1Jyd7U2iJBfp6SrJ56Km2AnxqN5mzob+WBG6v6dNUDZDn8NP7RwAgmzefVnh3lXxzr/0kR8r83OSdU5apbv0lr0/jt4lc=",
     "input2":"DD55F1pTbAjMx0Xs9rlsciT5IE+pzCIxnqiJSznv6Oe2An4jjANUcZv+4wi+cJDcGr7VCr0RgUjkdDvaYnZ0//McDDofCYfU72DLwmZGXz6qz0DRkE+K1ba8XRUyOAfAHHIPH6sHWwUbZtesHwbmjcte+Ff4JvpFMNXhs+RgX+A=",
     "remember":True,
     # "geetest_challenge":"05489fa7888ff74430cc6328ed6005d3ih",
     # "geetest_validate":"f7e8f7699c5e084aa3b822eedb464b39",
     # "geetest_seccode":"f7e8f7699c5e084aa3b822eedb464b39|jordan"

}
s = requests.session()
r = s.post(url, json=payload, headers= headers, verify = False)
print(r.json)
