"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""
import datetime


class Car:
    brand: str
    model: str
    year: int

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        try:
            if year <= datetime.datetime.now().year:
                self.year = year
            else:
                raise Exception
        except Exception:
            print('Эта машина еще не была выпущена')
        else:
            print(f'Год выпуска: {self.year}')


# код для проверки
car = Car('Toyota', 'Corolla', 2022)

car = Car('Toyota', 'Corolla', 3000)
# raises Exception('Эта машина еще не была выпущена')
