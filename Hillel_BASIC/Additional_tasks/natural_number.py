# Дано натуральне число n. Надрукуйте всі n-значні непарні натуральні числа в порядку спадання.
# Приклад: ввід 10 | результат [9, 7, 5, 3, 1]
# natural_number - приймає n натуральне число , повертає список непарних натуарльних чисел у прядку спадання


def natural_number(n):
    result = []
    if n % 2 == 0:
        for num in range(n, 0, -1):
            if num % 2 != 0:
                result.append(num)
    else:
        for num in range(n, 0, -1):
            if num % 2 != 0:
                result.append(num)

    return result


print(natural_number(11))
