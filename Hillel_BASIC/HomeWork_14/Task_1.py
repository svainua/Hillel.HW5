# Написати функцію сортування двовимірного списку МхМ (матриці) Значення М - задається користувачем з клавіатури. Може бути будь-яким цілим, позитивним числом більше 5.
# Функція повинна:
# 1. знайти суму елементів стовпців і відсортувати стовпці за зростанням цих сум.
# 2. відсортувати кожен непарний стовпець за зростанням значень знизу вгору, а кожен парний стовпець за зростанням значень зверху донизу.
# Також ваша програма повинна мати функцію виведення даного списку
#
# на екрані. При виведенні внизу кожного стовпця повинна виводитися сума елементів цього стовпця.
#
# Що можна використати:
# 1. для створення списку використовувати ТІЛЬКИ 'list comprehension' та
# генератор випадкових чисел. Діапазон випадкових чисел для заповнення списку від 1 до 50. Список має створюватися записом в один рядок.
# 2. Можна використовувати лише два списки. Перший це двомірний список розміром МхМ, другий, допоміжний, одномірний список розміром М. Використання інших списків (або колекцій) НЕДОПУСТИМО.
# 3. Можна використовувати ТІЛЬКИ ОДНУ змінну М для зберігання розміру списку плюс змінні циклів for.
# 4. Для сортування можна використовувати алгоритм бульбашкового сортування. Використання вбудованих функцій сортування – НЕДОПУСТИМО (та й не вийде їх використовувати)!
# 5. Рішення має включати ТІЛЬКИ ДВІ функції: функцію сортування (за правилами описаними вище) та функцію виведення на екран.
# Завдання вважається вирішеним правильно за умови дотримання всіх вимог. Охайне виведення на екран – вітається.

import random


def show(length):
    def sort(total, big_matrix):
        for i in range(len(big_matrix[0])):
            for j in range(0, len(big_matrix[0]) - i - 1):
                if total[j] > total[j + 1]:
                    for row in big_matrix:
                        row[j], row[j + 1] = row[j + 1], row[j]
                    total[j], total[j + 1] = total[j + 1], total[j]

        for j in range(len(big_matrix)):
            if (j + 1) % 2 != 0:
                for i in range(len(big_matrix) - 1):
                    for k in range(i, len(big_matrix)):
                        if big_matrix[k][j] > big_matrix[i][j]:
                            big_matrix[k][j], big_matrix[i][j] = (
                                big_matrix[i][j],
                                big_matrix[k][j],
                            )
            else:
                for i in range(len(big_matrix) - 1):
                    for k in range(i, len(big_matrix)):
                        if big_matrix[k][j] < big_matrix[i][j]:
                            big_matrix[k][j], big_matrix[i][j] = (
                                big_matrix[i][j],
                                big_matrix[k][j],
                            )

    matrix = [
        [random.randint(1, 50) for item in range(length)] for item in range(length)
    ]
    summ_list = [sum(matrix[j][i] for j in range(length)) for i in range(length)]

    print("The Matrix before sorting:")
    for internal_list in matrix:
        print(*[f"{num: >4}" for num in internal_list])
    print()
    print(*[f"{num: >4}" for num in summ_list])

    sort(summ_list, matrix)

    print()
    print("The Matrix after sorting:")
    for internal_list in matrix:
        print(*[f"{num: >4}" for num in internal_list])
    print()
    print(*[f"{num: >4}" for num in summ_list])


show(10)
