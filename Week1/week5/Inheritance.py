# Inheritance

class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

class Dog(Animal):
    def __init__(self,breed,name):
        super().__init__(name)
        self.breed = breed


    def bark(self):
        super().eat()
        print(f'{self.name} is barking')

bruno = Dog('pug','bruno')
print(bruno.bark())