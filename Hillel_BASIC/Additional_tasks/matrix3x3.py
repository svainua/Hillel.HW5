# Згенерувати двувимірний список 3x3.
# В утвореній матриці у кутові комірки розмістити випадкові парні числа в диапазоні від 10 до 30,
# але вони не повині повторюватися.

# пирклад візуаліації матриці:
# [
# [10, , 22],
# [ , , ],
# [24, ,16]
# ]

# matrix3x3 - функція нічого не приймає, але повертає matrix розміром 3 на 3

import random


def matrix3x3():
    matrix = [["", "", ""], ["", "", ""], ["", "", ""]]

    matrix[0][0] = random.randint(10, 30)
    matrix[0][2] = random.randint(10, 30)
    matrix[2][0] = random.randint(10, 30)
    matrix[2][2] = random.randint(10, 30)

    # return matrix

    for line in matrix:
        print(line)


matrix3x3()
