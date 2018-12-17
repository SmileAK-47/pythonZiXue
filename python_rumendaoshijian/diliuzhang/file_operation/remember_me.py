# import  json
# filename = 'username.json'
#
# username = input("Whis your name ?")
# with open(filename,'w')as f_obj:
#     json.dump(username,f_obj)
#     print("Well remember you when you come back "+username + " !")
#


# import json
# def greet_uesr():
#     filename = "username.json"
#     try :
#         with open(filename)as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         username = input("what is your name?")
# #         with open(filename,'w') as f_obj:
# #             json.dump(username,f_obj)
# #             print("well remember you when you come back " + username + "!")
# #     else:
# #         print("welcome to back"+username +"!")
# #
# # greet_uesr()

import  json
def get_stored_usernmae():
    #如果存储了用户名，就获取他
    filename = 'username.json'
    try:
        with open(filename) as f_ojb:
            username = json.load(f_ojb)
            print(username)
    except FileNotFoundError:
        return  None
    else:
        return username
def greet_user():
    #问候用户支出名字
    username = get_stored_usernmae()
    if username:
        print('welcome back'+ username+ "!")
    else:
        username = input("what is you name:")
        filename = 'username.json'
        with open(filename,'w')as f_obj:
            json.dump(username,f_obj)
            print("wel  remember you when come bake "+ username+"!")

greet_user()
