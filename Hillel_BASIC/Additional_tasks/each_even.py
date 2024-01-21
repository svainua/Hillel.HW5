# Зі списку nums вибрати парні числа та додати до списку only_even_nums
# Якщо nums пустий то в результаті роботи функції only_even_nums - пустий список

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def each_even(nums):
    only_even_nums = []
    for n in nums:
        if n % 2 == 0:
            only_even_nums.append(n)
    return only_even_nums


print(each_even(numbers))
