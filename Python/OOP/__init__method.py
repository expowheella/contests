import re


class Person:
    ''' May have its own attributes '''
    name = "Bulat"
    surname = "Iakhin"


''' And could be accessed if an object is created '''
me = Person()       # create example of Person called 'me'
print(
    me.name,        # Bulat
    me.surname      # Iakhin
)

''' But, these attributes are not inherited into the subclass '''
print(
    me.__dict__ # will return {}
)

''' You also cannot inherit the attributes from Person'''
# you = Person("Alsu", "Iakhina") # TypeError: Person() takes no arguments


''' If you need the attributes to be inherited from parent class, you should transform them into constructor fields'''
''' In this case, we should use constructor __init__'''

class Car:
    def __init__(self, name, year):
        self.type = 'light_vehicle'
        self.name = name
        self.year = year

    def show_speed(self, speed):
        self.speed = speed
        return f'the {self.name} of the year {self.year} has average speed of {self.speed}'

mersedes = Car(name="Mersedes", year=2022)
print(
    mersedes.name,'\n',
    mersedes.type,'\n',
    mersedes.year    
)

print (mersedes.show_speed(100))

bmw = Car("BMW", 2000)
print(bmw.show_speed(200))

""" You can also create methods of objects in order to make additional operations on the objects
    by inheriting from its parent class Car with its attributes """

class Speedometer(Car):
    
    def get_name(self):
        self.name = super().__dict__
        return self.name
        


mersedes_speedometer = Speedometer("BMW", 2022)
print(mersedes_speedometer.get_name)
