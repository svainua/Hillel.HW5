# Дано натуральне число n.
# Надрукуйте всі n-значні непарні натуральні числа в порядку спадання.
# Приклад:
#  ввід: 10
#  результат: [9, 7, 5, 3, 1]

number = int(input("Please choose the number: \n"))

my_list = []

if number % 2 == 0:
    for n in range(number):
        if n % 2 != 0:
            my_list.append(n)
else:
    for n in range(number + 1):
        if n % 2 != 0:
            my_list.append(n)

my_list.reverse()
print(my_list)
