# Сума натуральних чисел.
# Задається число num , потрібно вивести суму усіх чисел починаючи з 0 закінчуючи num (з цим числом включно).
# Використовуємо цикл while.


def sum_numbers(num):
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    return sum


print(sum_numbers(5))
