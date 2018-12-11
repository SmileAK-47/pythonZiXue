'''
classmates= ['wnag ','xiao','zhao']

for i in classmates:
    print( i)

print(len(classmates))

classmates.append('gang')
print(classmates)

classmates.insert(1,'mingming')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(1)
print(classmates)
'''

# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

for red in L:
    for w in red:

        print(w)
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
