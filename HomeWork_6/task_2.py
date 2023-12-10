# Двувимірний список чисел, робота зі стовбцями.
# Запросити у користувача число  N що має бути більше 5
# Запросити у користувача число  M що має бути більше 5
# Створити 2 вимірний список  NxM заповнений випадковими числами в диапазоні 1 - 100.
# Вивести у вигляді таблиці утворений список списків у вигляді таблиці де видно стовбц і рядки
# Замінити 2 останніх стовбці місцями - так що елементи передостаннього стовбця зберігають рядок але займають місце останнього стовбця а елементи останнього стовбця стають на місце передостаннього зберігаючи індекс рядка.
# Вивести у вигляді таблиці утворений список списків у вигляді таблиці де видно стовбц і рядки

import random

n_number = int(input("Please enter the number more tha 5: \n"))
m_number = int(input("Please enter the number more tha 5: \n"))

my_list = []

for line in range(n_number):
    internal_list = []
    my_list.append(internal_list)
    for l in range(m_number):
        random_number = random.randint(1, 100)
        internal_list.append(random_number)

for p in range(n_number):
    print(*my_list[p], end="\n")

print()

line = 0
for change in my_list:
    a = my_list[line][-2]
    my_list[line][-2] = my_list[line][-1]
    my_list[line][-1] = a
    line += 1

for p in range(n_number):
    print(*my_list[p], end="\n")


