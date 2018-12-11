#print(r'''hello
#,word''')
'''
a = 123
a = 'hello,world'
print(a)

#布尔型
b = True
print(b)

age  = 18
if age >=18:
    print('wo')
else:
    print('ni')

c = 'tom ,\"jery\" ,\"rosi\" '
print(c)

print("my name is %s , age %.2f " % ("asd",10.121))

'''
class message:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'my name {self.name},age {self.age}'.format(self=self)

print(str(message('Li',10)))

s1 = 72
s2 = 85

r = ((85-72)/72)*100
print('%.1f'% r)
print(r)