class Animal(object):
    def __init__(self,animal_type):
        print('Animal Type:', animal_type)
    def p(self):
        print("PAnimal")
class Mammal(Animal):
    def p(self):
        print("PMammal")
    def __init__(self):
        # call super class
        super().__init__('Mammal')
        print('Mammal give birth directly')
dog=Mammal()
dog.p()

# Method overriding



