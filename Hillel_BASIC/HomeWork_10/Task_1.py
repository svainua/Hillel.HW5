# Написати функцію яка приймає на вхід параметри: список чисел будь-якої довжини та число.
# Функція повинна перевірити чи є у списку/послідовності 2 числа сума яких еквівалентна числу переданому 2-гим параметром.
# Функція має повернути булеве значення як результат пошуку фукції.
# Для перевірки викликати двічі функцію з різними тестовими прикладами


def check_pair(my_list, number):
    """This function takes a list with a various number of numbers and one separate number. Function checks if
    there is any pair in the list, sum of which equals to the separate number"""
    result = False
    new_list = my_list
    for num in my_list:
        new_list.remove(num)
        for new_num in new_list:
            if num + new_num == number:
                result = True
            new_list = my_list
    return result


print(check_pair([1, 2, 3, 4, 5], 9))
print(check_pair([1, 2, 3, 4], 9))


