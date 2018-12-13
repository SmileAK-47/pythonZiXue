'''
# 7-1  汽车租赁：编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，
# 如“Let me see if I can find you a Subaru”。
a = input("Let me see if I can find you a Subaru!"+"\n：")
print(" wo yao nini:" +a)


# 7-2  餐馆订位：编写一个程序，询问用户有多少人用餐。如果超过 8人，就打印一
# 条消息，指出没有空桌；否则指出有空桌。
people = input("How many people"+"\n:")
if type(people) == int:
    people = int(people)
else:
    exit(10086)
if people >8 :
    print("not zuowei")
else:
    print("hai you zuowei ")

# 7-3   10  的整数倍：让用户输入一个数字，并指出这个数字是否是 10的整数倍。
number = input("place input:")
number = int(number)
if number % 10 ==0:
    print("shi 10 de beishu")
else:
    print("bu shi")


# 7-4  比萨配料：编写一个循环，提示用户输入一系列的比萨配料，并在用户输入
# 'quit' 时结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添
# 加这种配料。

add = "place input:"
message = ""
while add !='good':
    message = input(add)
    print("ok add :"+message)

# 7-5  电影票：有家电影院根据观众的年龄收取不同的票价：不到 3岁的观众免费；
# 3~12岁的观众为 10美元；超过 12岁的观众为 15美元。请编写一个循环，在其中询问
# 用户的年龄，并指出其票价。
age = "piao jia wei :"
# piao = ""
while True:
    piao = input(age)
    piao = int(piao)
    # print(piao)
    if piao < 3:
        print("不要钱")
    elif  12< piao <= 3:
        print("10美元")
    elif  piao >= 12 :
        # print("15刀")
        continue


# 7-6  三个出口：以另一种方式完成练习 7-4或练习 7-5，在程序中采取如下所有做法。
#  在 while 循环中使用条件测试来结束循环。
add = "place input:"
while True:
    message = input(add)
    print("ok add :"+ message)
    if message == "ok":
        break

#  使用变量 active 来控制循环结束的时机。
add = "place input:"
active = True
while active:
    message = input(add)
    if message == 'quit':
        break
    # print("ok add :"+ message)
    else:
        print("ok add :" + message)

#  使用 break 语句在用户输入 'quit' 时退出循环。
add = "place input:"
while True:
    message = input(add)
    print("ok add :"+ message)
    if message == "quit":
        break



# 7-7  无限循环：编写一个没完没了的循环，并运行它（要结束该循环，可按 Ctrl +C，
# 也可关闭显示输出的窗口）。
x = 1
while x < 10:
    # x += 1
    print(x)


# 7-8  熟食店：创建一个名为 sandwich_orders 的列表，在其中包含各种三明治的名
# 字；再创建一个名为 finished_sandwiches 的空列表。遍历列表 sandwich_orders ，对于
# 其中的每种三明治，都打印一条消息，如 I made your tuna sandwich ，并将其移到列表
# finished_sandwiches 。所有三明治都制作好后，打印一条消息，将这些三明治列出来。
sandwich_orders = ['rede','liangde','tangde']
finished_sandwiches = []
while sandwich_orders:
    sandwiches = sandwich_orders.pop()
    print("i made your tuna sandwich:"+sandwiches.title())
    finished_sandwiches.append(sandwiches)
print("\n yijng zuohao le:")
for sandwiches in finished_sandwiches:
    print(sandwiches.title())


# 7-9  五香烟熏牛肉（pastrami ）卖完了：使用为完成练习 7-8 而创建的列表
# sandwich_orders ，并确保 'pastrami' 在其中至少出现了三次。在程序开头附近添加这样
# 的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；再使用一个 while 循环将
# 列表 sandwich_orders 中的 'pastrami' 都删除。确认最终的列表 finished_sandwiches 中
# 不包含 'pastrami' 。
sandwich_orders = ['rede','pastrami','liangde','pastrami','tangde','pastrami']
print("pastrami 已经卖完了")
while 'pastrami' in sandwich_orders :
    sandwich_orders.remove('pastrami')
print(sandwich_orders)


# 7-10  梦想的度假胜地：编写一个程序，调查用户梦想的度假胜地。使用类似于“If
# you could visit one place in the world, where would you go?”的提示，并编写一个打印调
# 查结果的代码块。
city = {}
dream_active = True
while dream_active:
    name = input("if you could visit one place in the world where would you go ?")
    response = input("city:")
    city[name] = response

    repeat = input("would you like to lit another person respond?(yes / no)")
    if  repeat == 'no':
        dream_active = False
print("-----")
for name,response in city.items():
    print(name + 'would like to climb '+ response)



# 8-1  消息：编写一个名为 display_message() 的函数，它打印一个句子，指出你在本
# 章学的是什么。调用这个函数，确认显示的消息正确无误。
def study(name):
    print("haohaoxuexi:"+ name +"!")
study('hanshu')


# 8-2  喜欢的图书：编写一个名为 favorite_book() 的函数，其中包含一个名为 title
# 的形参。这个函数打印一条消息，如 One of my favorite books is Alice in Wonderland 。
# 调用这个函数，并将一本图书的名称作为实参传递给它。
def favorite_book(title):
    print("One of my favorite books is : "+title+"!")
favorite_book('钢铁是怎样炼成的')


# 8-3 T  恤：编写一个名为 make_shirt() 的函数，它接受一个尺码以及要印到 T恤上
# 的字样。这个函数应打印一个句子，概要地说明 T恤的尺码和字样。
# 使用位置实参调用这个函数来制作一件 T恤；再使用关键字实参来调用这个函数。
def make_shirt(size,typeface):
    print("T style size "+ size + ' typeface : '+typeface + ' .')

make_shirt('66','woaini')


# 8-4  大号 T  恤：修改函数 make_shirt() ，使其在默认情况下制作一件印有字样“I love
# Python”的大号 T恤。调用这个函数来制作如下 T恤：一件印有默认字样的大号 T恤、
# 一件印有默认字样的中号 T恤和一件印有其他字样的 T恤（尺码无关紧要）。
def make_shirt(size,typeface= "I love python"):
    print("T style size "+ size + ' typeface : '+typeface + ' .')

make_shirt('66')

# 8-5  城市：编写一个名为 describe_city() 的函数，它接受一座城市的名字以及该城
# 市所属的国家。这个函数应打印一个简单的句子，如 Reykjavik is in Iceland 。给用
# 于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城
# 市不属于默认国家。
def describe_city(city,country= '中国'):
    print(city + " is  in " + country)
describe_city('beijing')
describe_city('hangzhou')
describe_city('dongjing',country = 'jpan')


# 8-6  城市名：编写一个名为 city_country() 的函数，它接受城市的名称及其所属的
# 国家。这个函数应返回一个格式类似于下面这样的字符串：
# "Santiago, Chile"
# 至少使用三个城市国家对调用这个函数，并打印它返回的值。
def country(capital,city):
    fall = capital + ' ' + city
    return  fall.title()
fall =  country('beijing','zhongguo')
print(fall)
fall1 = country('dongjing','japan')
print(fall1)
fall_2 = country('newyek','america')
print(fall_2)

# 8-7  专辑：编写一个名为 make_album() 的函数，它创建一个描述音乐专辑的字典。
# 这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。使用这个函
# 数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑
# 的信息。
# 给函数 make_album() 添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调
# 用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个函数，并
# 至少在一次调用中指定专辑包含的歌曲数。
def make_album(music_name,artist_naem,number= ''):
    person = {'music':music_name.title(),'people':artist_naem.title()}

    if number :
        person['number']= number
    return person
musician = make_album('jiaoxiangqu','beiduofe',25)
print(musician)
musician = make_album('guangxianqu','bahe')
print(musician)
musician = make_album('ddd','sss',12)
print(musician)


# 8-8  用户的专辑：在为完成练习 8-7 编写的程序中，编写一个 while 循环，让用户
# 输入一个专辑的歌手和名称。获取这些信息后，使用它们来调用函数 make_album() ，并
# 将创建的字典打印出来。在这个 while 循环中，务必要提供退出途径。

def make_album(music_name,artist_naem,number= ''):
    person = {'music':music_name.title(),'people':artist_naem.title()}
    if number:
        person['number'] = number
    return person
while True:
    print("\n place tell me  your like  who:")
    m_name = input("music_name:")
    if m_name =='q':
        break
    a_name = input("artist_naem:")
    if a_name =='q':
        break
    b_nmuber = input("nmuber:")
    if b_nmuber =='q':
        break
    print(make_album(m_name,a_name,b_nmuber))


# 8-9  魔术师：创建一个包含魔术师名字的列表，并将其传递给一个名为
# show_magicians() 的函数，这个函数打印列表中每个魔术师的名字。
magicians_names = ['dava','baoluo','ganggnag','qiuchuji','qiaofeng']

def show_magicians(magicians_names):
    for name in magicians_names:
        print(name)
show_magicians(magicians_names)

print('---------------------------------------')

# 8-10  了不起的魔术师：在你为完成练习 8-9 而编写的程序中，编写一个名为
# make_great() 的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the
# Great”。调用函数 show_magicians() ，确认魔术师列表确实变了。

magicians_names = ['dava','baoluo','ganggnag','qiuchuji','qiaofeng']
alter_magical = []
def make_great(magicians_names,alter_magical):
    while magicians_names:
        magic = magicians_names.pop()
        print(magic + " is great ！")
        alter_magical.append(magicians_names)

def show_magicians(alter_magical):
    for name in alter_magical:
        print(name)
make_great(magicians_names,alter_magical)
show_magicians(magicians_names)

# 8-11  不变的魔术师：修改你为完成练习 8-10 而编写的程序，在调用函数
# make_great() 时，向它传递魔术师列表的副本。由于不想修改原始列表，请返回修改后
# 的列表，并将其存储到另一个列表中。分别使用这两个列表来调用 show_magicians() ，
# 确认一个列表包含的是原来的魔术师名字，而另一个列表包含的是添加了字样“the
# Great”的魔术师名字。
magicians_names = ['dava','baoluo','ganggnag','qiuchuji','qiaofeng']
alter_magical = []
def make_great(magicians_names,alter_magical):
    while magicians_names:
        magic = magicians_names.pop()
        print(magic + " is great ！")
        alter_magical.append(magicians_names)

def show_magicians(alter_magical):
    for name in alter_magical:
        print(name)

make_great(magicians_names[:],alter_magical)
show_magicians(alter_magical)
show_magicians(magicians_names)



# 8-12  三明治：编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个
# 函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点
# 的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。
def make_pizz(*toppings):
    print(toppings)
make_pizz('dd')
make_pizz('dd','aa','aa','gg')
make_pizz('ae','rt','r','t')


# 8-13  用户简介：复制前面的程序 user_profile.py ，在其中调用 build_profile() 来
# 创建有关你的简介；调用这个函数时，指定你的名和姓，以及三个描述你的键-值对。
def build_profile(first,last,**user_info):
    profile = { }
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
# user_profile = build_profile('albert','enter',
#                           location = 'sss',
#                           field  = 'aaa')



me_gang= build_profile('wang','gang',
                               school='yizhong',
                               worker= 'hagnzhou')
print(me_gang)

# 8-14  汽车：编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接
# 受制造商和型号，还接受任意数量的关键字实参。这样调用这个函数：提供必不可少的
# 信息，以及两个名称 — 值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# 打印返回的字典，确认正确地处理了所有的信息
def make_car(pinpai,chandi,**car_parts):
    car_tuple = {}
    car_tuple['pinpai'] = pinpai
    car_tuple['chadi'] = chandi
    for key,value in car_parts.items():
        car_tuple[key] = value
    return car_tuple
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

# 8-15  打印模型：将示例 print_models.py 中的函数放在另一个名为 printing_
# functions.py 的文件中；在 print_models.py 的开头编写一条 import 语句，并修改这个文
# 件以使用导入的函数。

        #--print_models.py文件中的代码-----
# def print_models(unprinted_desions,conmpleted_models):
#     while unprinted_desions:
#         current_design = unprinted_desions.pop()
#         print("moder:"+current_design)
#         conmpleted_models.append(current_design)
#
# def show_completed(completed_models):
#     print("The followingmodels have been printd:")
#     for i in completed_models:
#         print(i)

import printing_models  as spam
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []


spam.print_models(unprinted_designs,completed_models)
spam.show_completed(completed_models)



# 8-16  导入：选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一
# 个文件中。在主程序文件中，使用下述各种方法导入这个函数，再调用它：
# import  module_name
# from  module_name import  function_name
# from  module_name import  function_name as fn
# import  module_name as mn
# from  module_name import *

        #-------pets代码如下----
# def describe_pet(animal_type,pet_name):
#     print("\nI have a "+animal_type + "." )
#     print("my "+ animal_type + ' name is '+ pet_name + "!")

import pets
pets.describe_pet('aa','bb')

from pets import describe_pet
describe_pet('dd','bb')

from pets  import describe_pet as dp
dp('dd','bb')

import pets as pp
pp.describe_pet('aaa','aaa')

from pets import *
describe_pet('hh','nn')

# 8-17  函数编写指南：选择你在本章中编写的三个程序，确保它们遵循了本节介绍
# 的函数编写指南。

# 略


# 9-1  餐馆：创建一个名为 Restaurant 的类，其方法 __init__() 设置两个属性：
# restaurant_name 和 cuisine_type 。创建一个名为 describe_restaurant() 的方法和一个
# 名为 open_restaurant() 的方法，其中前者打印前述两项信息，而后者打印一条消息，
# 指出餐馆正在营业。
# 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述
# 两个方法。
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("naem: "+ self.restaurant_name)
        print("tpye: "+self.cuisine_type)
    def oper_restaurant(self):
        print("open ok")

restaurant_1 = Restaurant('wanggang','haha')
print(restaurant_1.restaurant_name,restaurant_1.cuisine_type)
restaurant_1.describe_restaurant()
restaurant_1.oper_restaurant()

# 9-2  三家餐馆：根据你为完成练习 9-1而编写的类创建三个实例，并对每个实例调
# 用方法 describe_restaurant() 。
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("naem: "+ self.restaurant_name)
        print("tpye: "+self.cuisine_type)
    def oper_restaurant(self):
        print("open ok")
restaurant_1 = Restaurant('xiao ming' ,'malatang')
restaurant_1.describe_restaurant()
restaurant_2 = Restaurant('da gang', 'shaokao')
restaurant_2.describe_restaurant()
restaurant_3 = Restaurant('little zhao','egg and tomato')
restaurant_1.describe_restaurant()


# 9-3  用户：创建一个名为 User 的类，其中包含属性 first_name 和 last_name ，还有
# 用户简介通常会存储的其他几个属性。在类 User 中定义一个名为 describe_user() 的方
# 法，它打印用户信息摘要；再定义一个名为 greet_user() 的方法，它向用户发出个性化
# 的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def desceribe_user(self):
        print("first_name : "+ self.first_name)
        print("last_name : "+ self.last_name)
    def gereet_user(self):
        print("hello:"+ self.first_name+" "+ self.last_name)

User_1 = User('wagn','gang')
User_1.desceribe_user()
User_1.gereet_user()
User_2 = User('little','zhao')
User_2.desceribe_user()
User_2.gereet_user()



# 9-4  就餐人数：在为完成练习 9-1 而编写的程序中，添加一个名为 number_served
# 的属性，并将其默认值设置为 0。根据这个类创建一个名为 restaurant 的实例；打印有
# 多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为 set_number_served() 的方法，它让你能够设置就餐人数。调用这个
# 方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为 increment_number_served() 的方法，它让你能够将就餐人数递增。
# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served =0
    def describe_restaurant(self):
        print("naem: "+ self.restaurant_name)
        print("tpye: "+self.cuisine_type)
        print('the number of meals : ' + str(self.number_served))
    def oper_restaurant(self):
        print("open ok")

    def set_number_served(self,nubmer):
        self.number_served = nubmer

    def increment_number_seved(self,number):
        self.number_served += number

restaurant= Restaurant('ganggang','roudian')
restaurant.describe_restaurant()
restaurant.oper_restaurant()
print('-----')
restaurant.set_number_served(10)
restaurant.describe_restaurant()
print('-----')
restaurant.increment_number_seved(3)
restaurant.describe_restaurant()

# 9-5  尝试登录次数：在为完成练习 9-3 而编写的 User 类中，添加一个名为
# login_attempts  的属性。编写一个名为 increment_login_attempts() 的方法，它将属性
# login_attempts 的值加 1。再编写一个名为 reset_login_attempts() 的方法，它将属性
# login_attempts 的值重置为 0。
# 根据 User 类创建一个实例，再调用方法 increment_login_attempts() 多次。打印属
# 性 login_attempts 的值，确认它被正确地递增；然后，调用方法 reset_login_attempts() ，
# 并再次打印属性 login_attempts 的值，确认它被重置为 0。
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def desceribe_user(self):
        print("first_name : "+ self.first_name)
        print("last_name : "+ self.last_name)
        print("login_attempst : "+ str(self.login_attempts))
    def gereet_user(self):
        print("hello:"+ self.first_name+" "+ self.last_name)
    def increment_login_attrempst(self):
        self.login_attempts +=1
        return self.login_attempts
    def reste_login_attemts(self):
        self.login_attempts = 0
        return self.login_attempts

nwe_user =User('wang','gang')
# nwe_user.increment_login_attrempst()
nwe_user.desceribe_user()
nwe_user.increment_login_attrempst()
nwe_user.gereet_user()
nwe_user.increment_login_attrempst()
nwe_user.increment_login_attrempst()
print(nwe_user.increment_login_attrempst())
nwe_user.reste_login_attemts()
print(nwe_user.login_attempts)
#-------------------------------------------------------------------------
# 9-6  冰淇淋小店：冰淇淋小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的
# 类，让它继承你为完成练习 9-1 或练习 9-4 而编写的 Restaurant 类。这两个版本的
# Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为 flavors 的属性，用于
# 存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个
# IceCreamStand 实例，并调用这个方法。
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served =0
    def describe_restaurant(self):
        print("naem: "+ self.restaurant_name)
        print("tpye: "+self.cuisine_type)
        # print('the number of meals : ' + str(self.number_served))
    def oper_restaurant(self):
        print("open ok")

    def set_number_served(self,nubmer):
        self.number_served = nubmer

    def increment_number_seved(self,number):
        self.number_served += number

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        # self.name = name
        # self.type = type
    def flavors(self):
        print("Ths is a "+ self.restaurant_name + ' and cuisine is '+ self.cuisine_type)

IceCreamStand = IceCreamStand('ganggang','liangliang')
# print(IceCreamStand.describe_restaurant())
IceCreamStand.flavors()

#-------------------------------------------------------------------------
# 9-7  管理员：管理员是一种特殊的用户。编写一个名为 Admin 的类，让它继承你为
# 完成练习 9-3 或练习 9-5 而编写的 User 类。添加一个名为 privileges 的属性，用于存
# 储一个由字符串（如 "can add post" 、 "can delete post" 、 "can ban user" 等）组成的
# 列表。编写一个名为 show_privileges() 的方法，它显示管理员的权限。创建一个 Admin
# 实例，并调用这个方法。

class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def desceribe_user(self):
        print("first_name : "+ self.first_name)
        print("last_name : "+ self.last_name)
        print("login_attempst : "+ str(self.login_attempts))
    def gereet_user(self):
        print("hello:"+ self.first_name+" "+ self.last_name)
    def increment_login_attrempst(self):
        self.login_attempts +=1
        return self.login_attempts
    def reste_login_attemts(self):
        self.login_attempts = 0
        return self.login_attempts

class Adimin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privigese = ["can add post", "can delete post", "can ban user"]
    def shew_privilease(self):
        print(self.privigese)
Admin = Adimin('wangwang','ganggang')
Admin.shew_privilease()

#-------------------------------------------------------------------------
# 9-8  权限：编写一个名为 Privileges 的类，它只有一个属性—— privileges ，其中
# 存储了练习 9-7所说的字符串列表。将方法 show_privileges() 移到这个类中。在 Admin
# 类中，将一个 Privileges 实例用作其属性。创建一个 Admin 实例，并使用方法
# show_privileges() 来显示其权限。

class Privieges():
    def __init__(self,):
        # self.privileges = privileges
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        print(self.privileges)
        for privileges in self.privileges:
            print(privileges)
admin = Privieges()
admin.show_privileges()

#-------------------------------------------------------------------------

# 9-9  电瓶升级：在本节最后一个 electric_car.py 版本中，给 Battery 类添加一个名为
# upgrade_battery() 的方法。这个方法检查电瓶容量，如果它不是 85，就将它设置为 85。
# 创建一辆电瓶容量为默认值的电动汽车，调用方法 get_range() ，然后对电瓶进行升级，
# 并再次调用 get_range() 。你会看到这辆汽车的续航里程增加了
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometeer_reading = 0
    def get_desccripive_name(self):
        long_name = str(self.year)+ ' '+ self.model +' '+self.make
        return long_name

    def read_odmoter(self):
        print('the is car '+ str(self.odometeer_reading) + ' miles on it')

    def updata_odometer(self,mileage):
        # self.odometeer_reading = mileage
        # 将里程表读数设置为指定的值
        # 禁止将里程表读数往回
        if mileage >= self.odometeer_reading:
            self.odometeer_reading = mileage
        else:
            print("you cat't roo back an odometer!")

    def incrment_odometer(self,miles):
        #将里程表读数增加指定的量
        self.odometeer_reading += miles

class Bettery():
    #一次模拟电动汽车电瓶车的简单完成
    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def descaribe_battery(self):
        print("The CAR has a "+ str(self.battery_size)+ "-kwh battery")

    def get_range(self):
        if self.battery_size ==70 :
            range = 240
        elif self.battery_size ==85:
            range = 270

        message = "This car can go apporximaterly "+  str(range)
        message += " miles on a full charge"
        print(message)

    def upgrade_battery(self):
            if self.battery_size != 85:
                self.battery_size = 85

class ElecatricCar(Car):
    def __init__(self,make ,model,year):
        super().__init__(make,model,year)
        self.battery = Bettery()

my_tesla =  ElecatricCar('tesla','model' ,2018)
my_tesla.battery.get_range()
my_tesla.battery.get_range()
#----------------------------------------------------------

# 9-13  使用 OrderedDict ： 在练习 6-4中，你使用了一个标准字典来表示词汇表。请
# 使用 OrderedDict 类来重写这个程序，并确认输出的顺序与你在字典中添加键 — 值对的
# 顺序一致。
from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['ken']= 'c'
favorite_languages['li'] = 'python'
favorite_languages['gang'] = 'c++'
favorite_languages['wang'] = 'java'

for k,v in favorite_languages.items():
    print(k +" " + v)

#--------------------------------------------------------------------------
# 9-14  骰子：模块 random 包含以各种方式生成随机数的函数，其中的 randint() 返回
# 一个位于指定范围内的整数，例如，下面的代码返回一个 1~6内的整数：
# from random import randint
# x = randint(1, 6)
# 请创建一个 Die 类，它包含一个名为 sides 的属性，该属性的默认值为 6。编写一
# 个名为 roll_die() 的方法，它打印位于 1和骰子面数之间的随机数。创建一个 6面的骰
# 子，再掷 10次。
# 创建一个 10面的骰子和一个 20面的骰子，并将它们都掷 10次。
from random import randint
class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        x = randint(1,6)
        self.sides = x
        print(self.sides)

    def roll_die10(self):
        x = randint(1,10)
        self.sides = x
        print(self.sides)
    def roll_die20(self):
        x = randint(1,20)
        self.sides = x
        print(self.sides)

    # def roll_die(self):
    #     for i in range(10):
    #         print(randint(1,self.sides))

doo = Die()

print('-----6---')
for i in range(10):
    doo.roll_die()
print('---10---')
for i in range(10):
    doo.roll_die10()
print('---20----')
for i  in range(20):
    doo.roll_die20()


#-------------------------------------------------------------------------
# 10-1 Python  学习笔记：在文本编辑器中新建一个文件，写几句话来总结一下你至
# 此学到的 Python知识，其中每一行都以“In Python you can”打头。将这个文件命名为
# learning_python.txt，并将其存储到为完成本章练习而编写的程序所在的目录中。编写一
# 个程序，它读取这个文件，并将你所写的内容打印三次：第一次打印时读取整个文件；
# 第二次打印时遍历文件对象；第三次打印时将各行存储在一个列表中，再在 with 代码
# 块外打印它们。
filename = 'G:\\webderiver\\python_rumendaoshijian\\diliuzhang\\file_operation\\learning_python.txt'
with open(filename) as file_object:
    read = file_object.read()
    print(read)
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip())

#-----------------------------------------------
# 10-2 C  语言学习笔记：可使用方法 replace() 将字符串中的特定单词都替换为另一
# 个单词。下面是一个简单的示例，演示了如何将句子中的 'dog' 替换为 'cat' ：
# >>>  message = "I really like dogs."
# >>>  message.replace('dog', 'cat')
# 'I really like cats.'
# 读取你刚创建的文件 learning_python.txt中的每一行，将其中的 Python都替换为另
# 一门语言的名称，如 C。将修改后的各行都打印到屏幕上。
filname = 'learning.txt'
with open(filname,'a') as file_object:
    file_object.write("One=In C you can 1\n")
    file_object.write("Two=In C you can 2\n")
    file_object.write("there=In C you can 3\n")

with open(filname)as file_object:
    lens = file_object.readlines()
    for line in lens:
        print(line.rstrip().replace('C','python'))
------------------------------------------------------------------



# 10-3  访客：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写
# 入到文件 guest.txt中。
filename = 'guest.txt'
with open(filename,'w') as file_object:
    name = input("place enter name:")
    file_object.write(name)

#-----------------------------------------------------------------------------
# 10-4  访客名单：编写一个 while 循环，提示用户输入其名字。用户输入其名字后，
# 在屏幕上打印一句问候语，并将一条访问记录添加到文件 guest_book.txt 中。确保这个
# 文件中的每条记录都独占一行。
filename = 'guest_book.txt'
while True:
    with open(filename,'a')as file_object:
        naem = input("place enter name:")
        thought = input("place gan yan:")
        if name == 'quit'
            break
        file_object.write('name:'+naem+"\n")
        file_object.write('gan yan ：'+thought+'\n')
        print('thanks')

'''
# 10-5  关于编程的调查：编写一个 while 循环，询问用户为何喜欢编程。每当用户输
# 入一个原因后，都将其添加到一个存储所有原因的文件中。
filename = 'question.txt'
while True:
    your_reason = input('why you like :')
    if your_reason == 'q':
        break
    else:
        with open(filename,'a') as file_object:
            file_object.write('your:'+your_reason+'\n')