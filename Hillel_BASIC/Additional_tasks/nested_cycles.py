# Знайти всі трицифрові натуральні числа, сума цифр яких дорівнює їхньому добутку.
# nested_cycles нічого не отримує як вхідний параметр,
# але повертає список усіх трицифрових натуральних чисел що відповідаюь умові задачі.

import math


def nested_cycles():
    numbers_size3n = []
    for i in range(100, 1000):
        num_list = list(str(i))
        new_num_list = []
        for char in num_list:
            n = int(char)
            new_num_list.append(n)

        i_sum = sum(new_num_list)
        i_mult = math.prod(new_num_list)

        if i_sum == i_mult:
            numbers_size3n.append(i)

    return numbers_size3n


print(nested_cycles())
