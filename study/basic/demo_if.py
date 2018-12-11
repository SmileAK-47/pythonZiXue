'''
age = 17
if age >= 18:
    print('you are is ', age)
    print('adult')
else:
    print('you are is',age)
    print('teenger')

s = input('birth:')
birth = int(s)
if birth < 2000:
    print("00前")
else:
    print("00后")


# 练习
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）
# 帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：

# -*- coding: utf-8 -*-

# height = 15
# weight = 30
weight = float (input("请输入体重："))
height = float (input("请输入身高："))

bim  =  weight/(height*2)
if bim <18.5:
    print("过轻")
elif 18.5<= bim <25:
    print("正常")
elif 25<= bim <28:
    print("过重")
elif 28<= bim <32:
    print("肥胖")
elif 32 <= bim :
    print("严重肥胖")
print(bim)

'''
age = int(input('Input your age: '))

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
