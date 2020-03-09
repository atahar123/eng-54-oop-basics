from animal_class import *

class Reptile(Animal):

    def __init__(self, name, age, colour, scales,blood_temp):
        super().__init__(name, age, colour)
        self.scales = scales
        self.blood_temp = blood_temp

    def make_sound(self):
        return 'BLAAAAAA'


animal1 = Animal('Nacho', 20, 'Yellowish')
reptile1 = Reptile('Ringo', 30, 'Yellow', 'Lots', 'Super cold')

print(animal1)
print(reptile1)

# Reptile has all the attributes and methods of Animal
print(reptile1.name) # This is an attribute of reptile not a method
print(reptile1.eat())
print(reptile1.potty())
print(reptile1.sleep())
print(reptile1.reproduce())
print(reptile1.make_sound())

print(animal1.make_sound())
print(animal1.reproduce())


