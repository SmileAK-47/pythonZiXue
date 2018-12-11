#ending = utf -8

class  Dalao():
    def __init__(self,name ,year,work):
        self.name = name
        self.year = year
        self.work = work

    def aut_test(self):
        print("大佬什么都可以")

    def aut_app_test(self):
        print("大佬会web")

dl = Dalao('adsf','15','IT')

print("大佬的名字：",dl.name )
print("大佬年龄:",dl.year )

dl.aut_app_test()
dl.aut_test()
