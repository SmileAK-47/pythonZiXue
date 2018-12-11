'''
# coding =   utf -8
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


#案例一
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
my_tesla = ElectricCar('testla','model',2018)
print(my_tesla.get_desccripive_name())


#案例二
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 70
    def descripbe_battery(self):
        print("this car has a "+ str(self.battery_size)+ "-kwh battery")
my_tesla = ElectricCar('testla','model',2018)
print(my_tesla.get_desccripive_name())
my_tesla.descripbe_battery()
'''


#将实例用作属性
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

class ElecatricCar(Car):
    def __init__(self,make ,model,year):
        super().__init__(make,model,year)
        self.battery = Bettery()

# my_tesla  =ElecatricCar('tesla','model',2018)
# print(my_tesla.get_desccripive_name())
# my_tesla.battery.descaribe_battery()
# my_tesla.battery.get_range()