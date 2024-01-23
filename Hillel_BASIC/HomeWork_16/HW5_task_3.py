""" Дано натуральне число n.
Надрукуйте всі n-значні непарні натуральні числа в порядку спадання.
Приклад:
ввід: 10
результат: [9, 7, 5, 3, 1]"""


def make_odd_list(num: int) -> list:
    """The function receives the entered by the user number and returns the descent list with odd numbers"""
    my_list = []

    if num % 2 == 0:
        for n in range(num):
            if n % 2 != 0:
                my_list.append(n)
    else:
        for n in range(num + 1):
            if n % 2 != 0:
                my_list.append(n)

    my_list.reverse()
    return my_list


# number = int(input("Please choose the number: \n"))
# result = make_odd_list(number)
# print(result)
