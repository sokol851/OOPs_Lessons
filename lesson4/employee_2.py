"""
Для класса Employee и Client, опишите магический метод сложения таким образом, чтобы результатом сложения
было число, а прибавлять можно было только числа или другие объекты дочерних классов Employee

"""


class Employee:
    def __init__(self, pay):
        self.pay = pay

    def __add__(self, other):
        # if isinstance(other, int):
        if isinstance(other, int):
            return self.pay + other
        if isinstance(other, Employee):
            return self.pay + other.pay
        return self.pay


class Client:
    def __init__(self, pay):
        self.pay = pay

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.pay + other.pay
        return other


class Developer(Employee):
    pass


class Manager(Employee):
    pass


# код для проверки
users = [Employee(50000), Client(100000), Developer(50000), Manager(50000)]

total_salary = 0
for user in users:
    total_salary = user + total_salary

print(total_salary)
# Вывод: 150000
