# 1 . Двувимірний список чисел
# Запросити у користувача число  N що має бути більше 0
# Створити 2 вимірний список  NxN заповнений випадковими числами в диапазоні 10 - 99.
# Вивести значення 2мирного списку рядок під рядком
# Порахувати суму діагоналі  двомірного списку з ліва на право з гори у низ - вивести суму
# Порахувати суму діагоналі  двомірного списку з права на  ліво з гори у низ - вивести суму
# Вивести число яке знаходиься в центрі перетину діагоналей

import random

number = int(input("Please enter odd number higher than 0: \n"))
my_list = []

for line in range(number):
    internal_list = []
    my_list.append(internal_list)
    for l in range(number):
        random_number = random.randint(10, 99)
        internal_list.append(random_number)

for p in range(number):
    print(*my_list[p], end="\n")

diagonal_step_left = 0
diagonal_left_sum = 0

for diagonal_sum in range(number):
    digit = my_list[diagonal_step_left][diagonal_step_left]
    diagonal_left_sum += digit
    diagonal_step_left += 1

print(f"The sum of diagonal starting from up left till right down is: {diagonal_left_sum}")

diagonal_step_right_y = 0
diagonal_step_right_x = number - 1
diagonal_right_sum = 0

for diagonal_sum in range(number):
    digit = my_list[diagonal_step_right_y][diagonal_step_right_x]
    diagonal_right_sum += digit
    diagonal_step_right_y += 1
    diagonal_step_right_x -= 1

print(f"The sum of diagonal starting from up right till left down is: {diagonal_right_sum}")

central_number_pos = int((number - 1) / 2)
central_number = my_list[central_number_pos][central_number_pos]

print(f"Central number is: {central_number}")
















