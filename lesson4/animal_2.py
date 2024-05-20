"""
Допишите код под условия в цикле так, чтобы вывод был корректным
"""


class Animal:
    def __init__(self, name):
        pass

    def walk(self):
        if isinstance(self, Dog):
            return Dog.bark(self)
        elif isinstance(self, Cat):
            return Cat.meow(self)


class Dog(Animal):
    @staticmethod
    def bark(self):
        print('Bark!')


class Cat(Animal):
    @staticmethod
    def meow(self):
        print('Meow!')


animals = [Dog('Dog1'), Dog('Dog2'), Cat('Cat1'), Dog('Dog3')]

for animal in animals:
    # Должно выводиться Bark или Meow в зависимости от того какой класс
    animal.walk()
