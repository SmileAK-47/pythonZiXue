'''
names = ['hah','lilei','xiaoming']
for name in names :
    print(name)

sum = 0
number = [1,2,3,4,5,6,6,7,8,9,10]
for x in number:
    sum = sum + x
print(sum)

sum1 = 0
a = range(101)
for x in a :
    sum1 = sum1 + x
print(sum1)

sum2 = 0
n = 99
while n >0:
    sum2 = sum2 + n
    n = n - 2
print("奇数和为: ",sum2)


n = 0
while n <10 :
    n = n +1
    if n % 2 ==0:
        continue
    print("jieguo:",n)

# w= tuple(range(1,101,2))
# for  i in  w:
#     print(i)

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

#打印列表
names = [' me ',' bob ',' you ']
print(names)

#打印数字0-9
for i in range(10):
    print(i)
'''
#计算1-100的和
sum = 0
n  = 1
while n <=100:
    sum = sum + n
    n  = n + 1
print(sum)

acc = 1
n = 1
while n <= 100:
    acc = acc * n
    n = n + 1
print(acc)