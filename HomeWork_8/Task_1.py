# Напишіть програму, Яка генерує список із 15 випадкових чисел. (використовуйте генератори списків чи генератори виразів)
# Виведіть:
# Так - якщо сумма непарних чисел у списку більша за суму парних чисел
# Ні - у всіх інших випадках

import random

my_list = [random.randint(0, 10) for i in range(15)]
print(my_list)

if sum(i for i in my_list if i % 2 != 0) > sum(i for i in my_list if i % 2 == 0):
    print("Yes")
else:
    print("No")



