# Створіть словник із випадковими числовими значеннями довжиною в 20 елементів.
# Необхідно їх (числові значення) перемножити і вивести на екран згенерований на початку словник та результат множення чисел.

import random

my_dict = {i: random.randint(1, 10) for i in range(1, 21)}

print(my_dict)

value_sum = 1
for n in my_dict:
    value_sum *= my_dict[n]

print(value_sum)
