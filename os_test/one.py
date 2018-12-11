import os
'''
#获取当前路径
os.getcwd()  

#更改当前目录
#os.chdir()
os.chdir('G:\\webderiver\\os_tes')

#创建新的文件夹
# os.makedirs('G:\\webderiver\\os_tes')

#os.path 模块提供了一些函数，返回一个相对路径的绝对路径，以及检查给定的路径是否为绝对路径
a= os.path.abspath('.\\webdriver\\os_one')
print(a)
#os.path.isabs 如果参数是一个绝对路径，就返回 True，如果参数是一个相对路径，就返回 False
b = os.path.isabs('.\\webdriver\\os_one')
print(b)

d = os.path.isabs('G:\webderiver\os_test\webdriver\os_one')
print(d)
#调用 os.path.relpath(path, start)将返回从 start 路径到 path 的相对路径的字符串
c= os.path.isabs(os.path.abspath('.\\webdriver\\os_one'))
print(c)

# open()函数打开文件
helloFile = open("G:\\webderiver\\test_one\\.idea\\001.txt","w")
# helloFile.write('hellasdf!\n')
# helloFile.close()

# print(helloFile)

# abc = helloFile.read()
print(helloFile)
'''
baconFile = open('G:\\webderiver\\test_one\\.idea\\001.txt','w')
baconFile.write("hello world!\n")
# baconFile.close()
# baconFile.write("bacon is ont a veaetable.")
# baconFile.close()

# baconFile = open('G:\\webderiver\\test_one\\.idea\\bacon.txt''a')
contert = baconFile.read()
# baconFile.close()
print(contert)
