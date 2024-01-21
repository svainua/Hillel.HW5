# Cтворити функцію генератор (yield) простих чисел у диапазоні заданих двома аргументами чисел.
# Вивести у консоль результат роботи функції-генератора у диапазоні від n до z в один рядок через прогалину.
# n і z- числа діапазону які можна вибирати випадковим чином.

import random


def simple_numbers(start, stop):
    for i in range(start, stop + 1):
        is_prime = True
        for num in range(2, int(i**0.5) + 1):
            if i % num == 0:
                is_prime = False
                break
        if is_prime:
            yield i


n = random.randint(1, 20)
z = random.randint(20, 100)

for n in simple_numbers(n, z):
    print(n, end=" ")
