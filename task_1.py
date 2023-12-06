# Запросити у користувача ввести рядок з 15 символів

# Програма перевіряє що рядок не пустий :

# якщо рядок пустий - виводе відповідне повідомлення і завершує роботу
# якщо рядок менше 15 символів збільшити рядок так щоб рядок був більше 15 символів (можна збільшити рядок "my string" * 3)
# коли рядок став 15 символів і більше конвертувати рядок в список и виконати наступне:
# вивести повний список
# вивести зі списку остaнніх 5 елементів
# вивести список (зеркально обернено) в зворотній послідовності
# вивести список усіх елементів з парними індексами
# вивести список у якому 5 елементів спочатку такі ж самі як остані 5 елементів списку
# вивести елементи списку без 2 перших елементів і без 2 останніх

my_string = input("Please add a string with 15 characters: \n")

while len(my_string) < 15:
    if len(my_string) == 0:
        print("You didn't add a string with 15 characters")
        break
    else:
        my_string *= 2

if len(my_string) >= 15:
    print(my_string)
    my_list = list(my_string)
    print(my_list)
    last_5_digits = my_list[-5:]
    print(last_5_digits)
    mirror_list = my_list[::-1]
    print(mirror_list)
    even_index_list = my_list[2::2]
    print(even_index_list)
    new_list = last_5_digits
    new_list.extend(my_list)
    print(new_list)
    sliced_list = my_list[2:-2]
    print(sliced_list)









