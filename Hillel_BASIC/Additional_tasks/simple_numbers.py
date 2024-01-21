# Прості числа, це ті числа, які діляться без залишку тільки на 1 і на себе. Найменше просте число, це 2.
# І так, приступимо до задачі.
# simple_numbers - приймає число upper_limit яке собою являю верхню межу диапазону від 0 до upper_limit.
# Потрібно вивести прості числа з цього диапазону.
#
# simple_numbers - повертає список простих чисел з диапазону


def simple_numbers(upper_limit):
    snumbers = []
    for i in range(2, upper_limit + 1):
        is_prime = True
        for num in range(2, int(i**0.5) + 1):
            if i % num == 0:
                is_prime = False
                break
        if is_prime:
            snumbers.append(i)
    return snumbers


print(simple_numbers(100))
