"""
Напишите класс Student, представляющий студента, имеющий следующие атрибуты:

- __slots__ = ('name', 'age', 'grades'): список атрибутов, доступных объекту.

Напишите класс Course, представляющий курс, имеющий следующие атрибуты:

- __slots__ = ('name', 'students'): список атрибутов, доступных объекту.
"""


class Student:
    __slots__ = ('name', 'age', 'grades')


class Course:
    __slots__ = ('name', 'students')


# код для проверки
student1 = Student()
student1.name = "John"
student1.age = 20
student1.grades = [90, 80, 85]
print(student1.name, student1.age, student1.grades)

student2 = Student()
student2.name = "Jane"
student2.age = 21
student2.grades = [95, 85, 90]
print(student2.name, student2.age, student2.grades)

course = Course()
course.name = "Math"
course.students = [student1, student2]
print(f'{course.name} - [{course.students[0].name}, {course.students[1].name}]')
