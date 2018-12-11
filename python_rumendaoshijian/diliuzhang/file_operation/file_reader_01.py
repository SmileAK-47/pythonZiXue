'''

filename = 'G:\\webderiver\\python_rumendaoshijian\\diliuzhang\\file_operation\\pi_digits.txt'

#逐行读取
with open(filename) as file_object:
    for line in file_object:
        print(line)

#输出没有多余空行
filename = 'G:\\webderiver\\python_rumendaoshijian\\diliuzhang\\file_operation\\pi_digits.txt'
with open(filename)as file_object:
    for line in file_object:
        print(line.rstrip())
'''
#创建一个包换文件各行内容的列表
filename = 'G:\\webderiver\\python_rumendaoshijian\\diliuzhang\\file_operation\\pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())