# Реалізувати 2 функціЇ
# Перша функція приймає 2 параметри і генерує 2 вимірний список заповнений випадковими цілими значенням в диапазлні 0 - 200.
# Парметри повинні задати кількість списків у основному списку, а також довжину елементів списку.
# Усі елементи головного списку є списками і мають однакову довжину.
# Також функція може бути запущена без параметрів з одним параметром та 2ма параметрами.
# Функція повинна повернути згенерований 2 мірний список.
# 2 га функція очікує один обовязковий парметр і це має бути 2 вимірний список симетричний.
# Вона отримує спискок і друкує симетричну табличку (у якої колонки не роз'їжаються) значень з отриманого формального парметра.
# За дпомогою 1 та 2 функції вивести 3 таблички :
# коли перша функція не отримує параметри
# коли перша фнкція отримує 1 парметр
# коли перша функція отримує 2 параметри

import random


def make_a_list(num=3, length=5):
    """This function creates and prints the matrix based on lists with a random integers from 0 till 200"""
    matrix = [[random.randint(0, 200) for n in range(length)] for i in range(num)]
    for internal_list in matrix:
        for index in range(length):
            internal_list[index] = f"{internal_list[index]: ^3}"

    for internal_list in matrix:
        print(internal_list, end="\n")


def check_my_list(function):
    """This function takes as a parameter another function and checks how it works with or without parameters"""
    function()
    print()
    function(num=4)
    print()
    function(num=5, length=5)


check_my_list(make_a_list)
