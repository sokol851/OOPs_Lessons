"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""

import time


class Timer:
    def __init__(self):
        self.elapsed_time = time.perf_counter()

    def __enter__(self):
        self.elapsed_time = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time = time.perf_counter() - self.elapsed_time


timer = Timer()
with timer:
    time.sleep(3)

print("Execution time:", timer.elapsed_time)
