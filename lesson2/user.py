"""
Напишите класс User, имеющий следующие свойства и методы:

- __init__(self, name, password): конструктор, принимающий имя пользователя и пароль
- name: свойство, которое возвращает имя пользователя
- password: свойство, позволяет установить или изменить пароль пользователя
- is_admin: свойство возвращает, является ли пользователь администратором или нет
- _is_admin: свойство-помощник определяет, является ли пользователь администратором или нет
- login(self, password): метод проверяет, соответствует ли введенный пароль паролю пользователя
- logout(self): метод, выходит из аккаунта пользователя
(устанавливает значение свойства _is_logged_in в False при условии, что пользователь залогинен)

Для свойств name и password используйте декораторы @property и @password.setter.
"""


class User:

    def __init__(self, first, password):
        self.first = first
        self.pwd = password
        self.is_admin = False
        self._admin = False
        self._is_logged_in = False

    @property
    def name(self):
        return f'{self.first}'

    @property
    def password(self):
        return f'{self.pwd}'

    @property
    def _is_admin(self):
        return f'{self.is_admin}'

    @_is_admin.setter
    def _is_admin(self, booly):
        self.is_admin = booly

    @password.setter
    def password(self, password):
        self.pwd = password

    def login(self, password):
        if password == self.password:
            print('True')
        else:
            print('False')

    def logout(self):
        if self._is_logged_in:
            self._is_logged_in = False
        return self._is_logged_in


# код для проверки 
user1 = User("Alice", "qwerty")
print(user1.name)  # Alice
print(user1.password)  # qwerty
print(user1.is_admin)  # False

user1.password = "newpassword"
print(user1.password)  # newpassword

user1._is_admin = True
print(user1.is_admin)  # True

user1.login("newpassword")  # True
user1.logout()
