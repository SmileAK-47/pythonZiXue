# def describe_pet(animal_type,pet_name):
#     print("\nI have a "+animal_type + "." )
#     print("my "+ animal_type + ' name is '+ pet_name + "!")

# describe_pet('wolf','dog')
#
# describe_pet('dog','haha')


class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name + "siting ")
    def roll_over(self):
        print(self.age +'old')

my_dog = Dog('xiao',25)
print(my_dog.name+" xiaoxao"+ str(my_dog.age)+'old')
print("hh "+ str(my_dog.age)+"years old")