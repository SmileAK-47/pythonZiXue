'''
class Car():
        def __init__(self,make,model,year):
            self.make = make
            self.model = model
            self.year = year
        def get_descriptive_name(self):
            long_name = str(self.year)+ ' '+ self.make +' '+ self.model
            return  long_name.title()
my_new_car = Car('audi','as',2016)
print(my_new_car.get_descriptive_name())


class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reding = 0
    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make +' '+self.model
        return long_name
    def read_odometer(self):
        print('the is car '+ str(self.odometer_reding)+' miles on it')
my_name_car = Car('audi','a4',2018)
print(my_name_car.get_descriptive_name())
# 使用句点方法 访问汽车属性odometer_reding
# 下面这行代码让python 在实例中找到odometer_redaing 并将值给为54
my_name_car.odometer_reding = 54
my_name_car.read_odometer()


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
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_desccripive_name())
my_new_car.updata_odometer(51)
my_new_car.read_odmoter()
'''



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
'''
my_new_car = Car('audi','a4',2018)
print(my_new_car.get_desccripive_name())

my_new_car.updata_odometer(23500)
my_new_car.read_odmoter()

# my_new_car.incrment_odometer(100)
# my_new_car.read_odmoter()

my_new_car.updata_odometer(100)
my_new_car.read_odmoter()

# my_new_car.updata_odometer(30000)
# my_new_car.read_odmoter()
'''