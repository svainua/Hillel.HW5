# num містить 3х значне число.
# За допомогою циклу while і математичних оперцій поміняти в числі цифри,
# симетрично записати результуюче значення в new_num, яке функція поверне в кінці своєї роботи якщо:
#
# 809 то результат 908
# 100 то результат 1
# 234 то результат 432


#
def num_reverse(num):
    i = 3
    new_num = 0
    while i > 0:
        i -= 1
        digit = num % 10
        num = num // 10
        new_num = new_num * 10 + digit

    return new_num


print(num_reverse(123))


# num = 200
# num_list = (list(str(num)))
# revers_l = num_list[::-1]
# revers_n = int(''.join(map(str, revers_l)))
#
# print(revers_n)
