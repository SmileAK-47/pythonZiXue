'''
from electric_car import ElecatricCar
my_tesla = ElecatricCar('tssla','model',2016)
print(my_tesla.get_desccripive_name())
my_tesla.battery.descaribe_battery()
my_tesla.battery.get_range()
'''

from  electric_car import  Car,ElecatricCar

my_beetle = Car('volkswagen','beetel',2016)
print(my_beetle.get_desccripive_name())

my_tesla = ElecatricCar('tesla','roadster',2018)
print(my_tesla.get_desccripive_name())