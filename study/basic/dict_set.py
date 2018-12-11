# a = dict(1,2,3)
# b= set(1,2,3)
# c= dict((1, [2, 3]))
# w = set([2, 3])
# e = set ([1,1,1,5,5,6,7,8])
# f = set([1,2,3])
# g = dict(1,2,3,)
# h = dict((1, [2, 3]))
# i = dict([3,1,4])

# j = set([2,1,4])
# print(f)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)


l1  = set([5,6,3,7,1])
print(l1)
l2 =  set([3,4,5,7])
print(l1&l2)
print(l2 | l1)