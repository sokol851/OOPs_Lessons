"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число
- Оценки - список из целых чисел, может быть пустым

Опишите класс Student и метод avg_rate так, чтобы считалась средняя оценка, а при пустом списке оценок возвращался 0

"""


class Student:
    name: str
    course: str
    rate: list

    def __init__(self, name, course, rate=None):
        self.name = name
        self.course = course
        if rate is None:
            rate = []
        self.rate = rate

    def avg_rate(self):
        try:
            return print(sum(self.rate) / len(self.rate))
        except ZeroDivisionError:
            return print(0.0)


# код для проверки
student = Student('Ivan', 'Python', [5, 4, 5, 5])
student.avg_rate()  # 4.75

student = Student('Ivan', 'Python', [])
student.avg_rate()  # 0.0
