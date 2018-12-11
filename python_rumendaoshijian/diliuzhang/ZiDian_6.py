
'''
#6-7在为完成练习 6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为 people 的列表中。
# 遍历这个列表，将其中每个人的所有信息都打印出来。
alien_0 = {'color':'green','points':'5'}
alien_1 = {'color':'yellow','points':'5'}
alien_2 = {'color':'blue','points':'5'}
people = [alien_0, alien_1,alien_2]
for alien_info in people:
    print(alien_info)

#6_8宠物：创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在
#每个字典中，包含宠物的类型及其主人的名字。将这些字典存储在一个名为 pets 的列
#表中，再遍历该列表，并将宠物的所有信息都打印出来。

dd = {'name':'dd','host':'gnaggang'}
mm = {'name':'mm','host':'wangwang'}
tt = {'name':'mm','host':'xiaozhao'}

pest = [dd,mm,tt]
for pest_info in pest:
    print(pest_info)

# 6-9  喜欢的地方：创建一个名为 favorite_places 的字典。在这个字典中，将三个
# 人的名字用作键；对于其中的每个人，都存储他喜欢的 1~3个地方。为让这个练习更有
# 趣些，可让一些朋友指出他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字
# 及其喜欢的地方打印出来。
favorite_places= {'wang':['dali','beijing'],
                'xiaoming':['shandong','xinjinag'],
                  'xiaozhao':['tianjing','bejing']}
for y,k in favorite_places.items():
    print("\n"+ y +":")
    for info  in k :
        print(info)

# 6-10  喜欢的数字：修改为完成练习 6-2而编写的程序，让每个人都可以有多个喜欢
# 的数字，然后将每个人的名字及其喜欢的数字打印出来。

friends_numbers = {
    'jack' :[ '6','7','10'],
    'tom' : ['7','10','11'],
    'angel' : ['30','10','12'],
    'kitty' : ['1','2','34']
    }
for k ,y in friends_numbers.items():
    print("\n"+ k +':')
    for nmumber in y:
        print("lucky"+str(nmumber))
'''

# 6-11  城市 ：创建一个名为 cities 的字典，其中将三个城市名用作键；对于每座城市，都创建一个字典，
# 并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。在表示每座城市的字典中，
# 应包含 country 、 population 和 fact 等键。将每座城市的名字以及有关它们的信息都打印出来。

cities  = {
    'beijing':{
        "country":'china',
        "pupulation":'thertinYi',
        "fact":'people happya'
        },
    'nanjing':{
        "country": 'china_01',
        "pupulation": 'how mach',
        "fact": 'hen leng'
    },
    'dongbei':{
        "country": 'beifang',
        "pupulation":'four',
        "fact": 'geng leng'
    }
}
for k ,v in cities.items():
    print('\ncity'+ k)
    for key, value  in v.items():
        print(key +":"+ value)