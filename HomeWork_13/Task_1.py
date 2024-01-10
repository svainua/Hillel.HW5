# Створити текстовий файл, записати в нього, по-рядково, дані, які вводить користувач у терміналі.
# Закінченням введення служить порожній рядок. Кожен введений рядок у файлі повинен починатися з нового рядка.

with open("new.txt", mode="a") as file:
    should_continue = True
    while should_continue:
        add_info = input("Please add what you want:\n")
        if len(add_info) < 1:
            should_continue = False
        else:
            file.write(add_info + "\n")

