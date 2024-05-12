"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""

import time


class Timer:
    def __init__(self):
        self.elapsed_time = 0

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.time()
        self.elapsed_time = self.stop - self.start
        return self.elapsed_time


with Timer() as timer:
    a = sum(range(1, 200))
    print(a)

    print("Execution time:", timer.elapsed_time)
