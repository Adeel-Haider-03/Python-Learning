#Polymorphism in classes refer to having methods in different classes that have the same name but possibly different implementations.

class Animal:
    def __init__(self, name):
        self.name = name
       
    def movement(self):
        return 'walk'
    

class Dog(Animal):
    pass  # Inherits movement method from Animal, we write pass when we want to skip writing code and also avoid errors

class Fish(Animal):
    def movement(self):
        return 'swim'

class Bird(Animal):
    def movement(self):
        return 'fly'


dog = Dog('Buddy')
fish = Fish('Goldie')
bird = Bird('Tweety')

for x in (dog, fish, bird):
    print(f'{x.name} can {x.movement()}')